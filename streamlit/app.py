import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from common.preprocessing import predict_yield

st.set_page_config(page_title="🌾 Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction App")

region = st.selectbox("Region", ['North', 'East', 'South', 'West'])
soil = st.selectbox("Soil Type", ['Clay', 'Sandy', 'Loam', 'Silt', 'Peaty', 'Chalky'])
crop = st.selectbox("Crop", ['Wheat', 'Rice', 'Maize', 'Barley', 'Soybean', 'Cotton'])
weather = st.selectbox("Weather Condition", ['Sunny', 'Rainy', 'Cloudy'])

rainfall = st.slider("Rainfall (mm)", 0, 1000, 300)
temperature = st.slider("Temperature (°C)", 10, 50, 25)
days = st.slider("Days to Harvest", 30, 300, 120)

fertilizer = st.checkbox("Fertilizer Used")
irrigation = st.checkbox("Irrigation Used")

if st.button("Predict Yield"):
    y = predict_yield(region, soil, crop, weather,
                      rainfall, temperature,
                      fertilizer, irrigation, days)
    st.success(f"🌱 Estimated Yield: {y:.2f} tons/hectare")
