import numpy as np
import pandas as pd
import streamlit as st
import pickle

st.title('Prediksi Harga Sewa Unit Apartment di Daegu, Korea Selatan')

if 'model' not in st.session_state:
    model = pickle.load(open('RF_Model_Daegu_Apartment.sav', 'rb'))
    st.session_state['model'] = model

st.header('Silakan Masukkan Karakteristik Unit Apartemen yang Angin Anda Sewakan!')
HallwayType_Input = st.radio('Masukkan tipe Hallway', ['Terraced', 'Corridor', 'Mixed'])
TimeToSubway_Input = st.radio('Masukkan lama waktu dari gedung apartemen anda ke stasiun terdekat', ['0-5min', '5min~10min', '10min~15min', '15min~20min', 'No Subway Station Nearby'])
SubwayStation_Input = st.radio('Masukkan nama stasiun subway terdekat', ['Myung-duk', 'Kyungbuk University Hospital', 'Sin-nam', 'Banwoldang', 'Bangoge', 'Chilsung Market', 'Daegu', 'No Subway Nearby'])
Size_input = st.number_input('Masukkan luas gedung apartemen anda (rentang 135-1796)')
BasementParking_Input = st.number_input('Masukkan jumlah total parkir basement (rentang 0-1321)')
YearBuilt_Input = st.number_input('Masukkan tahun berapa gedung apartemen itu dibangun (rentang 1978-2015)')
NearbyETC_Input = st.number_input('Masukkan jumlah fasilitas gedung lainnya (seperti mall, bank, tempat wisata, dll) yang dekat dengan gedung apartemen anda (rentang 0-5)')
FacilitiesApt_Input = st.number_input('Masukkan jumlah fitur yang ada di dalam unit apartemen anda (rentang 1-10)')
NearbyOffice_Input = st.number_input('Masukkan jumlah gedung perkantoran yang dekat dengan gedung apartemen anda (rentang 0-7)')
NearbyUniversity_Input = st.number_input('Masukkan jumlah universitas yang dekat dengan gedung apartemen anda (rentang 0-5)')

if (HallwayType_Input == 'Terraced'):
    HallwayType_Input = 'terraced'
elif (HallwayType_Input == 'Mixed'):
    HallwayType_Input = 'mixed'
else:
    HallwayType_Input = 'corridor'

if (TimeToSubway_Input == 'No Subway Station Nearby'):
    TimeToSubway_Input = 'no_subway_station_nearby'

if (SubwayStation_Input == 'Kyungbuk University Hospital'):
    SubwayStation_Input = 'Kyungbuk_uni_hospital'
elif(SubwayStation_Input == 'Chilsung Market'):
    SubwayStation_Input = 'Chil-sung-market'
else:
    SubwayStation_Input = 'no_subway_nearby'

if st.button('Prediksi Harga'):
    data_dict = {'HallwayType' : HallwayType_Input, 
                 'TimeToSubway' : TimeToSubway_Input, 
                 'SubwayStation' : SubwayStation_Input,
                 'N_FacilitiesNearBy(ETC)' : NearbyETC_Input,
                 'N_FacilitiesNearBy(PublicOffice)' : NearbyOffice_Input,
                 'N_SchoolNearBy(University)' : NearbyUniversity_Input,
                 'N_Parkinglot(Basement)' : BasementParking_Input, 
                 'YearBuilt' : YearBuilt_Input,
                 'N_FacilitiesInApt' : FacilitiesApt_Input,
                 'Size(sqf)' : Size_input
                 }
    data = pd.DataFrame(data_dict, index=[0])

    result = st.session_state['model'].predict(data)
    st.write(f'Perkiraan harga sewa unit apartemen Anda per bulan adalah: ₩{result[0]:.2f} atau sekitar Rp{result[0]*11.87:.2f}') # 1 Won = Rp. 11.87
else:
    st.write('Masukkan data diri Anda dan model akan memprediksi harga sewa apartemen Anda!')