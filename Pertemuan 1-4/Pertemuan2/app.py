import streamlit as st
from inputdata import halaman_input
from hasildata import halaman_hasil

st.sidebar.title("Menu Navigasi")
menu = st.sidebar.radio("Pilih Halaman:",["Input Data", "Hasil Data"])

if menu == "Input Data":
    halaman_input()
if menu == "Hasil Data":
    halaman_hasil()


