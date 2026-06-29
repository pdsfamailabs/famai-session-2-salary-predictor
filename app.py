import streamlit as st

st.title("FamAI-Labs Salary Predictor")

years = st.slider("Years of Experience", 0, 20, 1)

predicted_salary = years * 15000

st.write(f"Estimated Salary: ₹{predicted_salary}")
