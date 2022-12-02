import pickle
import streamlit as st

# load save model
model = pickle.load(open('gagal_jantung.sav', 'rb'))

# Judul Untuk Web
st.title('Prediksi Kematian Pasien Gagal Jantung')
st.text('Nama : Rendra Faisal Jatnika')
st.text('Nim : 191351192')
st.text('Matkul : Business Intelligence')
st.text('Keterangan : Untuk Inputan 1 dan 0 itu menyatakan true dan false')

# Form Input
col1, col2 = st.columns(2)

with col1:
    age = st.slider('Umur Pasien Dengan (Range 40 - 95)', 40, 95)
with col2:
    anemia = st.selectbox('Apakah Pasien Mengalami Anemia Inputkan (1/0)', ('0', '1',))
with col1:
    creatinine_phosphokinase = st.text_input('Jumlah Creatinine_Phosphokinase (23, ..., 7861)')
with col2:
    diabetes = st.selectbox('Apakah Pasien Penderita Diabetes Inputkan Inputkan (1/0)', ('0', '1',))
with col1:
    ejection_fraction = st.text_input('Ejection Fraction (14, …, 80)')
with col2:
    high_blood_pressure = st.selectbox('Apakah Pasein Mengalami Tekanan Dahar Tinggi Inputkan (1/0)', ('0', '1'))
with col1:
    platelets = st.text_input('Masukan Jumlah Trombobit Dengan Range (25100, ..., 850000)')
with col2:
    serum_creatinine = st.number_input('Serum Creatinine Dengan Range (0.50, ..., 9.40)')
with col1:
    serum_sodium = st.text_input('Serum Sodium Dengan Range (114, ..., 148)')
with col2:
    sex = st.selectbox('Jenis Kelamin Pasien Inputkan (0/1)', ('0', '1',))
with col1:
    smoking = st.selectbox('Apakah Pasien Perokok Inputkan (1/0)', ('0', '1',))
with col2:
    time = st.slider('Masa Periode Pasien Dirawat Jumlah hari (Range 4,…,285)', 4, 285)

# kode Prediksi
heartfailure_diagnosis =''

#Button Prediksi
if st.button('Prediksi Kematian Pasien Gagal Jantung'):
    heartfailure_prediction = model.predict([[age, anemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets, serum_creatinine, serum_sodium, sex, smoking, time]])

    if(heartfailure_prediction[0]==1):
        heartfailure_diagnosis = 'Pasien Meninggal Karena Gagal Jantung'
    else:
        heartfailure_diagnosis = 'Pasien Tidak Meninggal Karena Gagal Jantung'

st.success(heartfailure_diagnosis)