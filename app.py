
import streamlit as st

st.set_page_config(
    page_title="Academic Advisor System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Academic Advisor System")
st.write(
    "Check your course grade and identify potential academic risks."
)

st.subheader("1. Student Academic Information")

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
    "Number of failed courses / carryovers",
    min_value=0,
    max_value=100,
    value=0,
    step=1
)

st.subheader("2. Course Grading System")

score = st.number_input(
    "Enter course score (0–100)",
    min_value=0,
    max_value=100,
    value=70,
    step=1
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

if st.button("Assess Academic Performance"):
    st.divider()

    st.subheader("Course Grade")
    st.metric("Letter Grade", grade)
    st.write(f"**Score:** {score}/100")
    st.write(f"**Remark:** {remark}")

    # Academic risk assessment
    risks = []

    if cgpa < 2.5:
        risks.append(
            f"CGPA is below 2.5 (current: {cgpa:.1f})."
        )

    if attendance < 80:
        risks.append(
            f"Attendance is below 80% (current: {attendance}%)."
        )

    if failed_courses > 3:
        risks.append(
            f"You have {failed_courses} failed courses/carryovers. "
            "The maximum allowed before this risk flag is 3."
        )

    st.subheader("Academic Risk Assessment")

    if risks:
        st.error("⚠️ AT RISK")
        st.write("The following conditions require attention:")

        for risk in risks:
            st.write(f"- {risk}")

        st.info(
            "Recommended action: Meet your academic adviser, "
            "improve attendance, address outstanding courses, "
            "and work on improving your CGPA."
        )
    else:
        st.success("✅ NOT FLAGGED AS AT RISK")
        st.write(
            "You meet all three academic-risk thresholds. "
            "Continue working toward better academic performance."
        )