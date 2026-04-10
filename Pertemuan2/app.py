import streamlit as st
from inputdata import halaman_input
from hasildata import halaman_hasil


st.sidebar.title("List Halaman")
menu = st.sidebar.radio("Pilih Halaman",["Input Data", "Data User"])

if menu == "Input Data":
    halaman_input()
elif menu == "Data User":
    halaman_hasil()