import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib



model_file_path = 'heartdisease.pkl'
loaded_model = joblib.load(model_file_path)


# Define the function to predict heart disease
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = (age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    return prediction[0]

st.title("CardioGuard - A Heart Disease Prediction App")

# Add custom CSS for background image
st.markdown(
    """
    <style>
    body {
        background-image: url('background.jpeg');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write("----")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    age = st.slider("Age", 29, 77, 50)

with col2:
    sex = st.selectbox("Sex", ("Male", "Female"))

with col3:
    cp = st.selectbox("Chest Pain Type", (0, 1, 2, 3))

with col4:
    trestbps = st.slider("Resting Blood Pressure (mm Hg)", 94, 200, 120)

with col5:
    chol = st.slider("Cholesterol (mg/dl)", 126, 564, 200)

with col6:
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ("No", "Yes"))

col7, col8, col9, col10, col11, col12 = st.columns(6)

with col7:
    restecg = st.selectbox("Resting Electrocardiographic Results", (0, 1, 2))
    thal = st.selectbox("Thalassemia Type", (0, 1, 2, 3))

with col8:
    thalach = st.slider("Maximum Heart Rate Achieved", 71, 202, 150)

with col9:
    exang = st.selectbox("Exercise-Induced Angina", ("No", "Yes"))

with col10:
    oldpeak = st.slider("ST Depression Induced by Exercise", 0.0, 6.2, 0.0)

with col11:
    slope = st.selectbox("Slope of the Peak Exercise ST Segment", (0, 1, 2))

with col12:
    ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", (0, 1, 2, 3, 4))

col13, col14, col15, col16, col17, col18 = st.columns(6)

with col16:
    if st.button("Clear Form"):
        st.experimental_rerun()

prediction = None

with col15:
    if st.button("Submit"):

        sex = 1 if sex == "Male" else 0
        fbs = 1 if fbs == "Yes" else 0
        exang = 1 if exang == "Yes" else 0

        prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)

if prediction is not None:
    st.markdown(
        f"""
        <style>
        /* Create a modal popup */
        .modal {{
            position: fixed;
            top: 55%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 200px;
            background-color: rgba(0, 0, 0, 0.9); /* Background color with transparency for blur effect */
            border-radius: 30px;
            text-align: center;
            color: white;
            z-index: 9999;
        }}
        </style>
        <div class="modal">
            <h1>Result</h1>
            <p>{"The person is predicted to be Healthy." if prediction == 0 else "The person is predicted to have Heart Disease."}</p>
        </div>
        <script>
        function hidePopup() {{
            document.querySelector('.modal').style.display = 'none';
            document.body.style.filter = 'none';
        }}
        </script>
        """,
        unsafe_allow_html=True,
    )
