import streamlit as st

def halaman_input():
    st.title("Halaman Input data")

    # Input Pengguna
    nama= st.text_input("Masukan Nama Anda:")
    usia = st.number_input("Masukan Usia Anda:", min_value=0, max_value=200)

    if st.button("Simpan Data"):
        st.session_state["nama"] = nama
        st.session_state["usia"] = usia
        st.success("Nama dan Usia berhasil disimpan!")