import streamlit as st
import os

# Mengatur layout agar lebar (wide mode) supaya peta dan input bisa bersandingan
st.set_page_config(layout="wide")

st.markdown("# 🌋 Identifikasi Penentuan Zonasi & Potensi REE")
st.markdown("### Wilayah Tapanuli Selatan")
st.markdown("---")

# Membagi halaman menjadi 2 kolom: Kiri untuk Input/Output, Kanan untuk Peta
kolom_kiri, kolom_kanan = st.columns([1, 1.2])

with kolom_kiri:
    # 1. Dropdown Input
    ph = st.selectbox("1. Pilih pH Fluida:", ["-- Pilih Parameter --", "Sangat Asam (pH < 4)", "Asam", "Netral"])
    suhu = st.selectbox("2. Pilih Suhu Fluida:", ["-- Pilih Parameter --", "Suhu Tinggi (200°C - 350°C)", "Suhu Rendah"])
    kurva = st.selectbox("3. Pilih Pola Kurva REE:", ["-- Pilih Parameter --", "Depresi / Defisit", "Pengayaan"])
    
    st.markdown(" ")
    tombol_analisis = st.button("🔷 JALANKAN ANALISIS", use_container_width=True)
    
    if tombol_analisis:
        if ph == "Sangat Asam (pH < 4)" and suhu == "Suhu Tinggi (200°C - 350°C)" and kurva == "Depresi / Defisit":
            st.markdown("### 📊 HASIL DIAGNOSIS SISTEM")
            st.error("**Zona Alterasi Terdeteksi:** Advanced Argilik")
            
            st.markdown("**🔬 Karakteristik Mobilitas REE:**")
            st.write("Sangat Mobil (Terlindi): Cairan asam kuat melarutkan REE batuan asal. REE terbawa menjauhi inti sistem.")
            
            st.markdown("**💎 Mineral Pembawa Utama:**")
            st.write("Minimal. Sebagian kecil LREE terikat di dalam struktur mineral Alunita.")
            
            st.markdown("**💎 Rekomendasi Potensi REE:**")
            st.warning("RENDAH: Zona ini kaya emas-tembaga, tetapi miskin LREE karena pencucian geokimia yang masif.")
        else:
            st.info("Silakan pilih kombinasi parameter yang sesuai untuk melihat hasil diagnosis.")

with kolom_kanan:
    # Menampilkan gambar peta jika ada di repository
    nama_gambar = "alterasi-tapselA1.jpg.jpeg"
    if os.path.exists(nama_gambar):
        st.image(nama_gambar, caption="Hydrothermal Alteration South Tapanuli Regency", use_container_width=True)
    else:
        st.error("File gambar peta tidak ditemukan di repository GitHub.")
