import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("data/Salary_Data.csv")

# Prepare data
X = df[['YearsExperience']]
y = df['Salary']

# Train model
model = LinearRegression()
model.fit(X, y)

# App title
st.title("💼 FamAI-Labs Salary Predictor")

# Description
st.write(
    "This Machine Learning app predicts salary based on years of experience."
)

# Slider input
years = st.slider(
    "Select Years of Experience",
    0.0,
    20.0,
    1.0
)

# Prediction
prediction = model.predict([[years]])

# Show result
st.subheader("📈 Predicted Salary")

st.success(f"Estimated Salary: ₹ {prediction[0]:,.2f}")

# Show dataset
if st.checkbox("Show Dataset"):
    st.write(df)

# Footer
st.markdown("---")
st.caption("Built with ❤️ by FamAI-Labs")
