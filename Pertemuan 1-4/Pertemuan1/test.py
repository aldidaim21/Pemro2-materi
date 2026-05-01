import pandas as pd
import streamlit as st

# # judul aplikasi
# st.title("ini adalah aplikasi membaca data")

# # data frame
# data = {
#     "nama" : ["andi", "budi", "caca"],
#     "umur" : [20, 21, 22],
#     "kota" : ["jakarta", "bandung", "surabaya"]
# }

# df = pd.DataFrame(data)

# st.write("Tabel Siswa")
# st.dataframe(df)




#aplikasi sederhana kedua
#input user

nama = st.text_input("Masukan nama Anda:")
pekerjaan = st.selectbox("Pilih pekerjaan Anda:", ["Pelajar", "Mahasiswa", "Pekerja","Nganggur"])

st.write(f"Halo {nama}, pekerjaan Anda adalah {pekerjaan}.")

