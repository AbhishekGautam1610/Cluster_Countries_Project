import streamlit as st
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the saved model and scaler
with open("clustering_model.pkl", "rb") as file:
    scaler, kmeans = pickle.load(file)

# Streamlit UI
st.title("🌍 Country Clustering App")
st.write("Enter country details to predict its cluster.")

# User inputs for clustering
child_mort = st.number_input("Child Mortality Rate", min_value=0.0, step=0.1)
exports = st.number_input("Exports (% of GDP)", min_value=0.0, step=0.1)
health = st.number_input("Health Expenditure", min_value=0.0, step=0.1)
imports = st.number_input("Imports (% of GDP)", min_value=0.0, step=0.1)
income = st.number_input("Income Level", min_value=0.0, step=1.0)
inflation = st.number_input("Inflation Rate", min_value=-10.0, max_value=50.0, step=0.1)
life_expec = st.number_input("Life Expectancy", min_value=30.0, max_value=100.0, step=0.1)
total_fer = st.number_input("Total Fertility Rate", min_value=0.0, step=0.1)
gdpp = st.number_input("GDP per Capita", min_value=0.0, step=1.0)

# Prediction Button
if st.button("Predict Cluster"):
    # Prepare input data
    input_data = np.array([[child_mort, exports, health, imports, income, inflation, life_expec, total_fer, gdpp]])
    input_scaled = scaler.transform(input_data)

    # Predict cluster
    cluster = kmeans.predict(input_scaled)[0]
    
    st.success(f"🌍 This country belongs to **Cluster {cluster}**!")