# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_pLrDnR-ADs_dQDlbDOdW0Pb_xbDn6MZ
"""

import pickle
import streamlit as st

pickle_in = open("Power_geneartion.pkl","rb")
model=pickle.load(pickle_in)

def predict_note_authentication(sky_cover_1, sky_cover_2, sky_cover_3, sky_cover_4, distance_to_solar_noon, temperature, wind_direction, wind_speed,
                                visibility, humidity, average_wind_speed_period,average_pressure_period):
    prediction=model.predict([[sky_cover_1, sky_cover_2, sky_cover_3, sky_cover_4, distance_to_solar_noon, temperature, wind_direction, wind_speed,
                               visibility, humidity, average_wind_speed_period,average_pressure_period]])
    print(prediction)
    return prediction

def main():
    st.title("SOLAR POWER GENERATION PREDICTION SYSTEM")
    sky_cover_1 = st.number_input("Sky Cover 1", value=0, step=1)
    sky_cover_2 = st.number_input("Sky Cover 2", value=0, step=1)
    sky_cover_3 = st.number_input("Sky Cover 3", value=0, step=1)
    sky_cover_4 = st.number_input("Sky Cover 4", value=0, step=1)
    distance_to_solar_noon = st.number_input("Distance to Solar Noon", value=0, step=1)
    temperature = st.number_input("Temperature", value=0, step=1)
    wind_direction = st.number_input("Wind Direction", value=0, step=1)
    wind_speed = st.number_input("Wind Speed", value=0, step=1)
    visibility = st.number_input("Visibility", value=0, step=1)
    humidity = st.slider("Humidity", 0, 100, 50)
    average_wind_speed_period = st.number_input("Average Wind Speed Period", value=0, step=1)
    average_pressure_period = st.number_input("Average Pressure Period", value=0, step=1)

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(sky_cover_1, sky_cover_2, sky_cover_3, sky_cover_4, distance_to_solar_noon, temperature, wind_direction, wind_speed,
                                visibility, humidity, average_wind_speed_period,average_pressure_period)
    st.success('The output is {}'.format(result))


if __name__=='__main__':
    main()

