
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Academic Advisor System",
    page_icon="🎓",
    layout="centered"
)

@st.cache_resource
def load_model():
    with open("academic_advisor_model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()

st.title("🎓 Academic Advisor System")
st.write("Check your grades and academic risk.")

st.subheader("Student Academic Information")

cgpa = st.number_input(
    "Current GPA / CGPA (out of 5.0)",
    min_value=0.0,
    max_value=5.0,
    value=3.0,
    step=0.1
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=80
)

failed_courses = st.number_input(
    "Failed courses / carryovers",
    min_value=0,
    max_value=100,
    value=0
)

st.subheader("Course Grading System")

score = st.number_input(
    "Course score (0–100)",
    min_value=0,
    max_value=100,
    value=70
)

if score >= 70:
    grade = "A"
    remark = "Excellent"
elif score >= 60:
    grade = "B"
    remark = "Very Good"
elif score >= 50:
    grade = "C"
    remark = "Good"
elif score >= 45:
    grade = "D"
    remark = "Pass"
elif score >= 40:
    grade = "E"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"

st.write(f"**Grade:** {grade}")
st.write(f"**Remark:** {remark}")

if st.button("Assess Academic Performance"):
    risks = []

    if cgpa < 2.5:
        risks.append("CGPA is below 2.5.")

    if attendance < 80:
        risks.append("Attendance is below 80%.")

    if failed_courses > 3:
        risks.append("You have more than 3 failed courses/carryovers.")

    st.subheader("Academic Risk Assessment")

    if risks:
        st.error("⚠️ AT RISK")
        for risk in risks:
            st.write(f"- {risk}")
    else:
        st.success("✅ NOT FLAGGED AS AT RISK")

    st.subheader("Machine Learning Prediction")

    try:
        model_input = pd.DataFrame(
            [[cgpa, attendance, failed_courses]],
            columns=["cgpa", "attendance", "failed_courses"]
        )

        prediction = model.predict(model_input)[0]

        if prediction == 1:
            st.warning("Model prediction: At risk")
        else:
            st.success("Model prediction: Not flagged as at risk")

    except Exception as error:
        st.error(f"Model prediction failed: {error}")
        st.info(
            "Check that academic_advisor_model.pkl was retrained "
            "using the three inputs shown above."
        )