import streamlit as st
import pickle
import numpy as np

# Load the model
with open("academic_advisor_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🎓 Academic Advisor System")
st.write("Enter your details below to get academic advice")

# Input fields
gpa = st.number_input("Current GPA", min_value=0.0, max_value=5.0, value=3.0, step=0.1)
failed = st.number_input("Number of courses failed", min_value=0, max_value=10, value=0)
hours = st.number_input("Study hours per week", min_value=0, max_value=60, value=15)
attendance = st.number_input("Attendance percentage", min_value=0, max_value=100, value=80)

if st.button("Get Advice"):
    features = np.array([[gpa, failed, hours, attendance]])
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.error("⚠️ You are AT RISK. Advice: Reduce your course load and increase study hours.")
    else:
        st.success("✅ You are doing well. Keep up the good work!")