import streamlit as st
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_model.joblib')

# Set app title and header
st.set_page_config(page_title="Water Potability Predictor", layout="centered")
st.markdown("# 💧 Water Potability Prediction")

# Sidebar information
st.sidebar.image("https://img.icons8.com/ios-filled/100/water.png", width=100)
st.sidebar.title("🔍 Model Info")
st.sidebar.markdown("**Model:** Random Forest Classifier")
st.sidebar.markdown("**Balancing:** Random OverSampler")
st.sidebar.markdown("**Framework:** Streamlit")

# Input fields in two columns
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, step=0.1)
    solids = st.number_input("Solids (ppm)", min_value=0.0)
    sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0)
    organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0)
    turbidity = st.number_input("Turbidity (NTU)", min_value=0.0)

with col2:
    hardness = st.number_input("Hardness (mg/L)", min_value=0.0)
    chloramines = st.number_input("Chloramines (ppm)", min_value=0.0)
    conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0)
    trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0)

# Predict button
if st.button("💡 Predict Potability"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ The water is **Safe to Drink**.")
    else:
        st.error("❌ The water is **Not Safe to Drink**.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Author: Mustafa Ibrahim")