import streamlit as st

def halaman_hasil():
    st.title("Halaman Hasil")

    if "nama" in st.session_state and  "usia" in st.session_state:
        st.write(f"Nama Anda: {st.session_state['nama']}")
        st.write(f"Usia Anda: {st.session_state['usia']}")
    else:
        st.warning("Data belum tersedia. Silakan masukkan data di halaman input terlebih dahulu.")
        