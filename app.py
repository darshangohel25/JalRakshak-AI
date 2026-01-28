import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="JalRakshak AI",
    page_icon="💧",
    layout="centered"
)

st.title("💧 JalRakshak AI – Drought Risk Predictor")
st.write("Early Warning System for Drought Risk")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    with open("jalrakshak_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# -----------------------------
# User Inputs
# -----------------------------
st.subheader("Enter Environmental Data")

rainfall = st.number_input(
    "Rainfall (mm)",
    min_value=0.0,
    max_value=2000.0,
    step=1.0
)

groundwater = st.number_input(
    "Groundwater Level (%)",
    min_value=0.0,
    max_value=100.0,
    step=1.0
)

temperature = st.number_input(
    "Temperature (°C)",
    min_value=-50.0,
    max_value=60.0,
    step=0.1
)

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Drought Risk"):
    # Input dataframe must match model feature names
    input_data = pd.DataFrame(
        [[rainfall, groundwater, temperature]],
        columns=["rainfall", "groundwater", "temperature"]
    )

    prediction = model.predict(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == "High" or prediction == 2:
        st.error("🚨 HIGH Drought Risk")
    elif prediction == "Medium" or prediction == 1:
        st.warning("⚠️ MEDIUM Drought Risk")
    else:
        st.success("✅ LOW Drought Risk")
