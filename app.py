import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('fault_detection_model.pkl')
st.title("Fault Detection in Sensors ")

# Streamlit form
air_temp = st.number_input('Air temperature [K]', min_value=250.0, max_value=500.0, value=300.0)
proc_temp = st.number_input('Process temperature [K]', min_value=250.0, max_value=500.0, value=320.0)
rot_speed = st.number_input('Rotational speed [rpm]', min_value=100.0, max_value=3000.0, value=1500.0)
torque = st.number_input('Torque [Nm]', min_value=0.0, max_value=200.0, value=50.0)
tool_wear = st.number_input('Tool wear [min]', min_value=0.0, max_value=300.0, value=100.0)

# Predict button
if st.button("Predict Machine Failure"):
    input_data = pd.DataFrame({
        'Air temperature [K]': [air_temp],
        'Process temperature [K]': [proc_temp],
        'Rotational speed [rpm]': [rot_speed],
        'Torque [Nm]': [torque],
        'Tool wear [min]': [tool_wear]
    })

    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ Machine Failure Detected!")
    else:
        st.success("✅ Machine Operating Normally.")
