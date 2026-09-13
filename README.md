# 🩺 Diabetes Prediction Web App

A Machine Learning-powered web application that predicts whether a person is likely to have **diabetes** based on various medical diagnostic parameters.

The application is built using **Python, Machine Learning, and Streamlit**, providing a simple and interactive interface for users to enter patient information and receive a prediction.

---

## 🚀 Features

* 🧠 Machine Learning-based diabetes prediction
* 🖥️ Interactive and user-friendly Streamlit interface
* 📊 Uses medical diagnostic parameters for prediction
* ⚡ Fast prediction results
* 🔢 Accepts numerical patient data
* 📱 Simple interface that can be accessed through a web browser
* 💾 Uses a pre-trained model saved using Pickle

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Pickle**

---

## 📁 Project Structure

```text
Diabetes-Prediction/
│
├── diabetes_prediction.py      # Main Streamlit application
├── trained_model.sav            # Trained Machine Learning model
├── requirements.txt             # Required Python libraries
├── README.md                    # Project documentation
└── dataset/                     # Dataset (if included)
```

---

## 📋 Input Parameters

The model uses the following parameters to make the prediction:

| Parameter                  | Description                    |
| -------------------------- | ------------------------------ |
| Pregnancies                | Number of times pregnant       |
| Glucose                    | Plasma glucose concentration   |
| Blood Pressure             | Diastolic blood pressure       |
| Skin Thickness             | Triceps skin fold thickness    |
| Insulin                    | 2-Hour serum insulin           |
| BMI                        | Body Mass Index                |
| Diabetes Pedigree Function | Diabetes hereditary risk score |
| Age                        | Age of the patient             |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/diabetes-prediction.git
```

Navigate to the project directory:

```bash
cd diabetes-prediction
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run diabetes_prediction.py
```

After running the command, Streamlit will provide a local URL similar to:

```text
http://localhost:8501
```

Open the URL in your web browser.

---

## 🧠 Machine Learning Workflow

The project follows a standard Machine Learning workflow:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Web Application
   ↓
Diabetes Prediction
```

The trained model is saved as:

```text
trained_model.sav
```

and loaded into the Streamlit application using Python's `pickle` module.

---

## 🔮 How the Prediction Works

1. The user enters their medical information in the web application.
2. The entered values are converted into a numerical array.
3. The input data is passed to the trained Machine Learning model.
4. The model analyzes the input features.
5. The application displays the prediction result.

Example:

```text
Patient Information
        ↓
Input Features
        ↓
Preprocessing
        ↓
Trained ML Model
        ↓
Prediction
        ↓
Diabetes / No Diabetes
```

---

## 📊 Model

The application uses a pre-trained Machine Learning classification model.

The model is trained using diabetes-related medical data and saved using Pickle.

Example model loading:

```python
import pickle

loaded_model = pickle.load(
    open("trained_model.sav", "rb")
)
```

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
numpy
pandas
scikit-learn
streamlit
```

Install them using:

```bash
pip install -r requirements.txt
```

---

## 🖥️ Application Preview

The application provides an easy-to-use interface where users can enter patient information and click the prediction button.

Example:

```text
┌─────────────────────────────────────┐
│       🩺 Diabetes Prediction        │
├─────────────────────────────────────┤
│ Pregnancies:              [  2  ]   │
│ Glucose:                  [120  ]   │
│ Blood Pressure:           [ 70  ]   │
│ Skin Thickness:           [ 25  ]   │
│ Insulin:                  [ 79  ]   │
│ BMI:                      [ 32.0]   │
│ Diabetes Pedigree:        [0.47 ]   │
│ Age:                      [ 33  ]   │
│                                     │
│          [ Predict Diabetes ]       │
└─────────────────────────────────────┘
```

---

## 🌐 Deployment

The application can be deployed using platforms that support Streamlit applications.

Before deployment, make sure your repository contains:

```text
diabetes_prediction.py
trained_model.sav
requirements.txt
README.md
```

You can then configure your deployment platform to run:

```bash
streamlit run diabetes_prediction.py
```

---

## 🔐 Important Note

This application is developed for **educational and demonstration purposes only**.

The prediction generated by this application should **not be considered a medical diagnosis**. Medical decisions should always be made by a qualified healthcare professional.

---

## 🔮 Future Improvements

Possible improvements include:

* [ ] Improve model accuracy
* [ ] Add multiple Machine Learning algorithms
* [ ] Display prediction probability
* [ ] Add data visualization
* [ ] Add model performance metrics
* [ ] Add Explainable AI (XAI)
* [ ] Improve UI/UX design
* [ ] Add patient history
* [ ] Deploy the application online
* [ ] Add authentication and user management

---

## 👨‍💻 Author

**Arnab Mallick**

This project was developed as a Machine Learning / Web Application project using Python and Streamlit.

---

## ⭐ Contributing

Contributions, suggestions, and improvements are welcome.

If you would like to contribute:

```bash
git fork
```

Create a new branch:

```bash
git checkout -b feature/new-feature
```

Commit your changes:

```bash
git commit -m "Add new feature"
```

Push the branch:

```bash
git push origin feature/new-feature
```

Then create a Pull Request.

---

## 📄 License

This project is intended for educational purposes. You may modify and use the project according to your requirements.
