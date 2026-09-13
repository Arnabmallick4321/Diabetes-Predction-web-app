# -*- coding: utf-8 -*-
"""
Diabetes Prediction Web App

Created on Sat Sep 12 20:57:54 2026
@author: arnab
"""

import numpy as np
import pickle
import streamlit as st
from pathlib import Path


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)


# --------------------------------------------------
# Load the trained model
# --------------------------------------------------
@st.cache_resource
def load_model():

    # Get the folder where this Python file is located
    model_path = Path(__file__).parent / "trained_model.sav"

    # Load the trained model
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    return model


# --------------------------------------------------
# Diabetes Prediction Function
# --------------------------------------------------
def diabetes_prediction(input_data, model):

    # Convert input data into NumPy array
    input_data_as_numpy_array = np.asarray(
        input_data,
        dtype=float
    )

    # Reshape the data for one prediction
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_data_reshaped)

    # Return result
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
    # Load Model
    # --------------------------------------------------
    try:

        loaded_model = load_model()

    except FileNotFoundError:

        st.error(
            "❌ trained_model.sav was not found."
        )

        st.info(
            "Make sure trained_model.sav is uploaded "
            "to the same folder as this Python file."
        )

        return

    except Exception as e:

        st.error(
            "❌ Error loading the trained model."
        )

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

        # Store all input values
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
                loaded_model
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
