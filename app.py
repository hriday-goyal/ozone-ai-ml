import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Ozone Generator AI Dashboard", page_icon="🧪")

# Title
st.title("🔬 AI-Powered Ozone Generator Dashboard")

st.markdown("Enter the input parameters to estimate ozone output, safety classification, and air purification efficiency.")

# User Inputs
voltage = st.slider("Input Voltage (kV)", 3.0, 10.0, 6.5, 0.1)
time = st.slider("Operation Time (minutes)", 1, 30, 10)
gap = st.slider("Electrode Gap (mm)", 1.0, 5.0, 2.0, 0.1)
temperature = st.slider("Ambient Temperature (°C)", 20, 35, 25)
humidity = st.slider("Humidity (%)", 30, 80, 50)
room_volume = 1.6  # fixed: your ozone box size in cubic feet

# --- MODEL 1: Ozone Output Estimation ---
ozone_ppm = voltage * time / (gap + 1)
temp_factor = 1 - abs(temperature - 25) * 0.02
humidity_factor = 1 - (humidity - 50) * 0.01
ozone_ppm *= temp_factor * humidity_factor
ozone_ppm = max(0, round(ozone_ppm, 3))

# --- MODEL 2: Safety Classification ---
is_safe = "✅ Safe" if ozone_ppm <= 0.05 else "⚠️ Unsafe (Above WHO limit)"

# --- MODEL 3: Purification Efficiency Estimation ---
ozone_factor = ozone_ppm * time
humidity_eff = 1 - (humidity - 50) * 0.005
temp_eff = 1 - abs(temperature - 25) * 0.01
eff_score = ozone_factor * humidity_eff * temp_eff / room_volume
efficiency = min(100, max(0, round(eff_score * 10, 1)))

# Display Results
st.subheader("📊 Results")
st.markdown(f"**Predicted Ozone Output:** `{ozone_ppm} ppm`")
st.markdown(f"**Safety Classification:** `{is_safe}`")
st.markdown(f"**Estimated Purification Efficiency:** `{efficiency}%`")

st.markdown("---")
st.caption("Built by Hriday Goyal · Powered by Streamlit · Project Year: 2025")