import streamlit as st

def halaman_hasil():
    
    st.title("Halaman Hasil Data")

    if "nama" in st.session_state and "umur" in st.session_state:
        st.write(f"Nama: {st.session_state['nama']}")
        st.write(f"Umur: {st.session_state['umur']}")
    else:
        st.warning("Belum ada data yang disimpan. Silakan masukkan data terlebih dahulu di halaman Input Data.")
