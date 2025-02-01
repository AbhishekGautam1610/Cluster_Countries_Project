import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("cluster_countries.pkl")

# Title for the app
st.title("Country Clustering Prediction")

# Input fields
child_mort = st.number_input("Child Mortality Rate", min_value=0.0, step=0.1)
income = st.number_input("Income Level", min_value=0.0, step=1.0)
life_expec = st.number_input("Life Expectancy", min_value=30.0, max_value=100.0, step=0.1)
total_fer = st.number_input("Total Fertility Rate", min_value=0.0, step=0.1)
gdpp = st.number_input("GDP per Capita", min_value=0.0, step=1.0)

# Predict button
if st.button("Predict"):
    # Format the input data
    input_data = pd.DataFrame([[child_mort,income,life_expec,total_fer,gdpp]])
    
    # Make a prediction
    prediction = model.predict(input_data)
    
    st.write(f"Predicted Cluster: {prediction[0]}")