import streamlit as st
import requests

'''
# TaxiFareModel for HEroku
'''

st.text_input("Date & Time", key="datetime")
st.text_input("Pickup Longitude", key="picklong")
st.text_input("Pickup Latitude", key="picklat")
st.text_input("Dropoff Longitude", key="droplong")
st.text_input("Dropoff Latitude", key="droplat")
st.text_input("Passenger Count", key="passenger")

selected_date = st.session_state.datetime
selected_picklong = st.session_state.picklong
selected_picklat = st.session_state.picklat
selected_droplong = st.session_state.droplong
selected_droplat = st.session_state.droplat
selected_passenger = st.session_state.passenger


def return_prediction():
    url = 'https://taxifare.lewagon.ai/predict'
    predict_url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={selected_date}&pickup_longitude={selected_picklong}&pickup_latitude={selected_picklat}&dropoff_longitude={selected_droplong}&dropoff_latitude={selected_droplat}&passenger_count={selected_passenger}'
    response = requests.get(predict_url)
    prediction = response.json()
    return prediction['prediction']

if st.button('Predict'):
    price = return_prediction()
    st.write(f'Your estimated price is: {price}')
else:
    st.write('Fill the parameters to predict the price')
