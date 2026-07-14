import streamlit as st
import os

# Mengatur layout agar lebar (wide mode) supaya peta dan input bisa bersandingan
st.set_page_config(layout="wide", page_title="Sistem Pakar REE Tapanuli Selatan")

st.markdown("# 🌋 Identifikasi Penentuan Zonasi & Potensi REE")
st.markdown("### Sistem Pakar Wilayah Tapanuli Selatan")
st.markdown("---")

# Membagi halaman menjadi 2 kolom: Kiri untuk Input/Output, Kanan untuk Peta
kolom_kiri, kolom_kanan = st.columns([1, 1.2])

with kolom_kiri:
    # 1. DROP-DOWN INPUT (Menampung semua opsi parameter geokimia)
    ph = st.selectbox(
        "1. Pilih pH Fluida:", 
        ["-- Pilih Parameter --", "Sangat Asam (pH < 4)", "Asam Lemah", "Netral–Basa", "Oksidatif"]
    )
    suhu = st.selectbox(
        "2. Pilih Suhu Fluida:", 
        ["-- Pilih Parameter --", "Suhu Tinggi (200°C–350°C)", "Suhu Sedang", "Suhu Rendah"]
    )
    kurva = st.selectbox(
        "3. Pilih Pola Kurva REE:", 
        ["-- Pilih Parameter --", "Depresi / Defisit", "Pengayaan LREE", "Pola Normal", "Anomali Ce Positif"]
    )
    
    st.markdown(" ")
    tombol_analisis = st.button("🔷 JALANKAN ANALISIS", use_container_width=True)
    
    # Tempat penampung variabel output
    zona = ""
    mobilitas = ""
    mineral = ""
    potensi = ""
    flag_match = False
    warna_bg = "#ffffff"  # Default putih

    if tombol_analisis:
        # Validasi jika ada input yang belum dipilih
        if ph == "-- Pilih Parameter --" or suhu == "-- Pilih Parameter --" or kurva == "-- Pilih Parameter --":
            st.warning("⚠️ Mohon lengkapi semua parameter input terlebih dahulu!")
        else:
            # 2. LOGIKA SISTEM PAKAR BERDASARKAN ATURAN GEOKIMIA (Translasi dari InStr VBA)
            
            # Opsi A: Advanced Argilik
            if "Sangat Asam" in ph and "Depresi" in kurva:
                zona = "Advanced Argilik"
                mobilitas = "Sangat Mobil (Terlindi): Cairan asam kuat melarutkan REE dari batuan asal. REE terbawa menjauhi inti sistem."
                mineral = "Minimal. Sebagian kecil LREE terikat di dalam struktur mineral Alunita."
                potensi = "RENDAH: Zona ini kaya emas-tembaga, tetapi miskin LTJ karena pencucian geokimia yang masif."
                flag_match = True
                warna_bg = "#FFE6E6" # Merah muda tipis (RGB 255, 230, 230)
                
            # Opsi B: Argilik
            elif "Asam Lemah" in ph and "Pengayaan LREE" in kurva:
                zona = "Argilik"
                mobilitas = "Imobil Sebagian (Terjebak): REE yang terlarut dari zona inti mulai mengendap kembali karena penurunan keasaman fluida."
                mineral = "Mineral lempung Ilit dan Smektit melalui proses adsorpsi ion pada permukaan lempung."
                potensi = "SEDANG: Mulai terjadi akumulasi REE jenis adsorpsi ion (ion-adsorption clay)."
                flag_match = True
                warna_bg = "#FFFFCC" # Kuning tipis (RGB 255, 255, 204)
                
            # Opsi C: Propilitik
            elif "Netral–Basa" in ph and "Pola Normal" in kurva:
                zona = "Propilitik"
                mobilitas = "Imobil / Isokimia: REE cenderung stabil karena fluida tidak cukup asam untuk merusak struktur batuan secara total."
                mineral = "Epidot, Kalsit, dan Apatit sekunder pembawa REE hasil substitusi kalsium (Ca)."
                potensi = "RENDAH HINGGA SEDANG: REE tertahan di dalam kisi kristal mineral silikat primer/sekunder (sulit diekstraksi)."
                flag_match = True
                warna_bg = "#F0F0F0" # Abu-abu tipis (RGB 240, 240, 240)
                
            # Opsi D: Tudung Oksidasi
            elif "Oksidatif" in ph and "Anomali Ce Positif" in kurva:
                zona = "Tudung Oksidasi (Supergen / Laterit)"
                mobilitas = "Imobilisasi & Pengayaan Residual: Pelapukan intensif melarutkan unsur mayor (Na, Ca, Mg), menyisakan REE yang tidak larut di permukaan."
                mineral = "Oksida besi (Geotit, Hematit) melalui penyerapan permukaan, serta sisa mineral resisten (Monasit, Xenotim)."
                potensi = "SANGAT TINGGI: Merupakan zona target utama untuk tipe endapan LTJ Laterit (paling ekonomis diolah)."
                flag_match = True
                warna_bg = "#CCFFCC" # Hijau tipis (RGB 204, 255, 204)

            # 3. MENAMPILKAN HASIL CETAK OUTPUT ATAU PESAN ERROR
            if flag_match:
                st.success(f"🎉 Analisis Geokimia Selesai! Zona Teridentifikasi: {zona}")
                
                # Container khusus dengan background warna dinamis sesuai zona
                st.markdown(
                    f"""
                    <div style="background-color: {warna_bg}; padding: 20px; border-radius: 10px; border: 1px solid #ddd; color: #000000;">
                        <h4 style="margin-top: 0; color: #111;">📋 HASIL DIAGNOSIS SISTEM</h4>
                        <hr style="margin: 10px 0; border-color: #bbb;">
                        <p><b>Zona Alterasi Terdeteksi:</b><br><span style="font-size: 1.2em; font-weight: bold;">{zona}</span></p>
                        <p><b>Karakteristik Mobilitas REE:</b><br>{mobilitas}</p>
                        <p><b>Mineral Pembawa Utama:</b><br>{mineral}</p>
                        <p><b>Rekomendasi Potensi REE:</b><br><b>{potensi}</b></p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            else:
                # Menggantikan MsgBox vbCritical jika kombinasi parameter acak/salah
                st.error("❌ Kombinasi parameter tidak sesuai dengan model zonasi geokimia Tapanuli Selatan. Silakan tinjau kembali data observasi Anda.")

with kolom_kanan:
    # Menampilkan gambar peta
    nama_gambar = "alterasi-tapselA1.jpg.jpeg"
    if os.path.exists(nama_gambar):
        st.image(nama_gambar, caption="Hydrothermal Alteration South Tapanuli Regency", use_container_width=True)
    else:
        st.info("💡 Pastikan file gambar 'alterasi-tapselA1.jpg.jpeg' berada di repository GitHub Anda agar peta tampil di sini.")
