import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Symptom Risk Checker",
    page_icon="🩺",
    layout="centered"
)

st.title("🩺 AI Symptom Risk Checker")
st.write("Select your symptoms below to assess your health risk level.")

st.warning("⚠️ Disclaimer: This tool is for educational purposes only and is NOT a medical diagnosis.")

st.subheader("Select Your Symptoms:")

# Symptom checkboxes
fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
fatigue = st.checkbox("Fatigue")
headache = st.checkbox("Headache")
nausea = st.checkbox("Nausea")
dizziness = st.checkbox("Dizziness")
chest_pain = st.checkbox("Chest Pain")
shortness_breath = st.checkbox("Shortness of Breath")

if st.button("Check Risk Level"):

    score = 0

    # Assign weights
    if fever:
        score += 2
    if cough:
        score += 2
    if fatigue:
        score += 1
    if headache:
        score += 1
    if nausea:
        score += 1
    if dizziness:
        score += 2
    if chest_pain:
        score += 4
    if shortness_breath:
        score += 4

    st.subheader("🔍 Risk Assessment Result")
    st.write(f"### Total Risk Score: {score}")

    # Risk classification
    if score <= 3:
        st.success("🟢 Low Risk")
        st.write("Recommendation: Rest, stay hydrated, and monitor your symptoms.")
    elif 4 <= score <= 7:
        st.warning("🟡 Moderate Risk")
        st.write("Recommendation: Monitor closely and consider consulting a doctor.")
    else:
        st.error("🔴 High Risk")
        st.write("Recommendation: Seek medical attention immediately.")

    st.info("If symptoms worsen or persist, please consult a healthcare professional.")
