# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 20:57:54 2026

@author: arnab
"""

import numpy as np
import pickle
import streamlit as st


# --------------------------------------------------
# Load the trained model
# --------------------------------------------------
@st.cache_resource
def load_model():
    with open('E:/ML/trained_model.sav', 'rb') as file:
        model = pickle.load(file)
    return model


# --------------------------------------------------
# Diabetes Prediction
# --------------------------------------------------
def diabetes_prediction(input_data, model):

    # Convert input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape for one prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Prediction
    prediction = model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return "The person is non-diabetic"
    else:
        return "The person is diabetic"


# --------------------------------------------------
# Main application
# --------------------------------------------------
def main():

    st.title("Diabetes Prediction Web App")

    st.write("Enter the following details to predict diabetes.")

    # Load model
    try:
        loaded_model = load_model()
    except Exception as e:
        st.error("Error loading the trained model.")
        st.exception(e)
        return

    # --------------------------------------------------
    # User Inputs
    # --------------------------------------------------

    Pregnancies = st.number_input(
        "Number of Pregnancies",
        min_value=0,
        max_value=20,
        value=0
    )

    Glucose = st.number_input(
        "Amount of Glucose",
        min_value=0.0,
        max_value=300.0,
        value=120.0
    )

    BloodPressure = st.number_input(
        "Amount of Blood Pressure",
        min_value=0.0,
        max_value=200.0,
        value=70.0
    )

    SkinThickness = st.number_input(
        "Skin Thickness",
        min_value=0.0,
        max_value=100.0,
        value=20.0
    )

    Insulin = st.number_input(
        "Insulin",
        min_value=0.0,
        max_value=1000.0,
        value=80.0
    )

    BMI = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0
    )

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5
    )

    Age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30
    )

    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    if st.button("Diabetes Test Result"):

        input_data = [
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age
        ]

        try:
            diagnosis = diabetes_prediction(
                input_data,
                loaded_model
            )

            st.success(diagnosis)

        except Exception as e:
            st.error("Error while making prediction.")
            st.exception(e)


# --------------------------------------------------
# Run application
# --------------------------------------------------

if __name__ == "__main__":
    main()