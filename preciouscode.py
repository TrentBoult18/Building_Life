# -*- coding: utf-8 -*-
"""PreciousCode.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tsVdrKoG5uv-FXhqijMZNoO0rHohwggz
"""

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

st.title("Building Life Cycle Prediction Model")
st.write("This app predicts the compressive strength of concrete as a proxy for the life cycle of buildings.")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    data = pd.read_excel(uploaded_file)
    st.write("Preview of the uploaded data:")
    st.dataframe(data.head())

    data.columns = ['Cement', 'Blast_furnace_Slag', 'Fly_Ash', 'Water', 'Super_plasticizer',
                    'Coarse_Aggregate', 'Fine_Aggregate', 'Age_of_testing', 'Compressive_Strength']

    X = data.drop('Compressive_Strength', axis=1)
    y = data['Compressive_Strength']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    st.write(f"Mean Squared Error (MSE): {mse}")
    st.write(f"R-squared (R2): {r2}")

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_test, y=y_pred)
    plt.xlabel("Actual Compressive Strength")
    plt.ylabel("Predicted Compressive Strength")
    plt.title("Actual vs Predicted Compressive Strength")
    st.pyplot(plt)

# Commented out IPython magic to ensure Python compatibility.
# # Step 1: Create the requirements.txt file manually
# %%writefile requirements.txt
# pandas==1.5.0
# numpy>=1.20
# seaborn==0.11.2
# matplotlib
# scikit-learn
# streamlit
# 
# # Step 2: Verify the contents of requirements.txt
# !cat requirements.txt
# 
# # Step 3: Download the requirements.txt file
# from google.colab import files
# files.download('requirements.txt')
#