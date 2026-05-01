import streamlit as st
from data import show_data

def judul():
    st.title("📊 Dashboard Covid-19")
    st.write("Selamat datang di dashboard Covid-19! Di sini Anda dapat melihat data terbaru tentang kasus Covid-19 di seluruh dunia, termasuk jumlah kasus, kematian, dan pemulihan. Gunakan menu di")


st.sidebar.title("Navigasi")
menu= st.sidebar.radio("Pilih Menu",["Home","Halaman Data"])
if menu == "Home":
    judul()
elif menu == "Halaman Data":
    judul()
    show_data()


