import streamlit as st

st.write('indi')
st.write('indana')
st.write('Hello, *World!* :sunglasses:')
st.header('agenda hari ini')

st.header('aplikasi penjumlahan bilangan numerik')

angka_pertama = st.number_input('masukkan angka pertama')
st.write('the current number is ', angka_pertama)

angka_kedua = st.number_input('masukkan angka kedua')
st.write('thecurrent number is ', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f'angka pertama {angka_pertama} x {angka_kedua} = {operasi_matematika}')