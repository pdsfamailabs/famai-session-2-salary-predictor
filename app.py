import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="FamAI-Labs Salary Predictor",
    page_icon="📊",
    layout="centered"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚀 FamAI-Labs")

st.sidebar.info(
    """
    Session 2 Project
    
    Machine Learning Salary Predictor
    
    Learn AI by building practical projects.
    """
)

# -----------------------------
# Load Dataset
# -----------------------------
import os  # import os module in python

Filepath=os.path.join(base_path,'datasource/input')
base_path='/content/drive/MyDrive/15d-ML-FamAILabs/'
df_salary=pd.read_csv(f'{Filepath}/Salary_Data.csv')  

# -----------------------------
# Prepare Data
# -----------------------------
X = df_salary[['YearsExperience']]
y = df_salary['Salary']

# -----------------------------
# Train Model
# -----------------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------------
# Main Title
# -----------------------------
st.title("💼 AI Salary Prediction App")

st.write("""
This Machine Learning app predicts salary based on years of experience.

Built as part of the FamAI-Labs practical AI learning series.
""")

# -----------------------------
# ML Workflow
# -----------------------------
st.subheader("🧠 How This Works")

st.markdown("""
1. Historical salary data is collected  
2. Machine Learning learns patterns  
3. User selects experience  
4. Model predicts estimated salary  
""")

# -----------------------------
# User Input
# -----------------------------
years = st.slider(
    "📅 Select Years of Experience",
    0.0,
    20.0,
    1.0
)

# -----------------------------
# Prediction
# -----------------------------
prediction = model.predict([[years]])

# -----------------------------
# Output
# -----------------------------
st.subheader("📈 Predicted Salary")

st.success(f"Estimated Salary: ₹ {prediction[0]:,.2f}")

# -----------------------------
# Dataset Viewer
# -----------------------------
if st.checkbox("📂 Show Dataset"):
    st.write(df)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption("Built with ❤️ by FamAI-Labs")
