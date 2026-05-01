import streamlit as st

def halaman_input():

    nama = st.text_input("Masukkan Nama")
    umur = st.number_input("Masukan Numur", min_value=0, max_value=200, step=1)
    submit = st.button("Simpan Data")

    if submit:
        if not nama:
            st.warning("Nama tidak boleh kosong!")
        else:
            st.session_state["nama"] = nama
            st.session_state["umur"] = umur
            st.success("Data berhasil disimpan!")
 

    