import streamlit as st
import joblib

model = joblib.load("model/marks_model.pkl")

st.title("📚 Student Marks Predictor")
hours = st.slider("Hours Studied:", 1.0, 10.0, step=0.5)
if st.button("Predict Marks"):
    marks = model.predict([[hours]])
    st.success(f"Predicted Marks: {marks[0]:.2f}")
