# -*- coding: utf-8 -*-
"""
Diabetes Prediction Web App

@author: arnab
"""

import numpy as np
import pickle
import streamlit as st
from pathlib import Path
from sklearn.preprocessing import StandardScaler
import pandas as pd


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)


# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------

@st.cache_resource
def load_model():

    model_path = Path(__file__).parent / "trained_model.sav"

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    return model


# --------------------------------------------------
# Load Dataset and Create Scaler
# --------------------------------------------------

@st.cache_resource
def load_scaler():

    # Dataset path
    dataset_path = Path(__file__).parent / "diabetes.csv"

    # Load dataset
    diabetes_dataset = pd.read_csv(dataset_path)

    # Separate features from target
    X = diabetes_dataset.drop(columns="Outcome")

    # Create scaler
    scaler = StandardScaler()

    # Fit scaler on the same dataset used for training
    scaler.fit(X)

    return scaler


# --------------------------------------------------
# Diabetes Prediction
# --------------------------------------------------

def diabetes_prediction(input_data, model, scaler):

    # Convert input data to NumPy array
    input_data_as_numpy_array = np.asarray(
        input_data,
        dtype=float
    )

    # Reshape for one prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # IMPORTANT:
    # Scale input using the same StandardScaler
    # used during model training
    input_data_scaled = scaler.transform(
        input_data_reshaped
    )

    # Prediction
    prediction = model.predict(input_data_scaled)

    if prediction[0] == 0:
        return "The person is non-diabetic"
    else:
        return "The person is diabetic"


# --------------------------------------------------
# Main Application
# --------------------------------------------------

def main():

    # Title
    st.title("🩺 Diabetes Prediction Web App")

    st.write(
        "Enter the following details to predict whether "
        "a person is diabetic or non-diabetic."
    )

    # --------------------------------------------------
    # Load Model and Scaler
    # --------------------------------------------------

    try:

        loaded_model = load_model()
        scaler = load_scaler()

    except FileNotFoundError as e:

        st.error("❌ Required file was not found.")

        st.write(
            "Make sure the following files are in the "
            "same folder as this Python file:"
        )

        st.code(
            """
trained_model.sav
diabetes.csv
            """
        )

        st.exception(e)

        return

    except Exception as e:

        st.error("❌ Error loading the model or dataset.")

        st.exception(e)

        return


    # --------------------------------------------------
    # User Input
    # --------------------------------------------------

    st.subheader("Enter Patient Details")

    Pregnancies = st.number_input(
        "Number of Pregnancies",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    Glucose = st.number_input(
        "Glucose Level",
        min_value=0.0,
        max_value=300.0,
        value=120.0,
        step=1.0
    )

    BloodPressure = st.number_input(
        "Blood Pressure",
        min_value=0.0,
        max_value=200.0,
        value=70.0,
        step=1.0
    )

    SkinThickness = st.number_input(
        "Skin Thickness",
        min_value=0.0,
        max_value=100.0,
        value=20.0,
        step=1.0
    )

    Insulin = st.number_input(
        "Insulin Level",
        min_value=0.0,
        max_value=1000.0,
        value=80.0,
        step=1.0
    )

    BMI = st.number_input(
        "BMI",
        min_value=0.0,
        max_value=70.0,
        value=25.0,
        step=0.1
    )

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.0,
        max_value=3.0,
        value=0.5,
        step=0.01
    )

    Age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=30,
        step=1
    )


    # --------------------------------------------------
    # Prediction Button
    # --------------------------------------------------

    st.write("")

    if st.button(
        "🔍 Diabetes Test Result",
        use_container_width=True
    ):

        # Store input values
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

        # Make prediction
        try:

            diagnosis = diabetes_prediction(
                input_data,
                loaded_model,
                scaler
            )

            # Display result
            if diagnosis == "The person is diabetic":

                st.error(
                    "⚠️ The person is diabetic."
                )

            else:

                st.success(
                    "✅ The person is non-diabetic."
                )

        except Exception as e:

            st.error(
                "❌ Error while making prediction."
            )

            st.exception(e)


# --------------------------------------------------
# Run Application
# --------------------------------------------------

if __name__ == "__main__":
    main()
