import streamlit as st

st.set_page_config(
    page_title="AI Symptom Risk Checker",
    page_icon="🩺",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
        .main {
            background-color: #f4f8fb;
        }
        .stButton>button {
            background-color: #0077b6;
            color: white;
            border-radius: 8px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #023e8a;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🩺 AI Symptom Risk Checker")
st.markdown("### Intelligent Symptom-Based Risk Assessment System")

st.info("⚠️ This tool is for educational purposes only. It does NOT provide medical diagnosis.")

st.markdown("---")

st.subheader("Select Your Symptoms")

col1, col2 = st.columns(2)

with col1:
    fever = st.checkbox("Fever")
    cough = st.checkbox("Cough")
    fatigue = st.checkbox("Fatigue")
    headache = st.checkbox("Headache")

with col2:
    nausea = st.checkbox("Nausea")
    dizziness = st.checkbox("Dizziness")
    chest_pain = st.checkbox("Chest Pain")
    shortness_breath = st.checkbox("Shortness of Breath")

st.markdown("---")

if st.button("🔍 Analyze Risk Level"):

    score = 0

    weights = {
        "fever": 2,
        "cough": 2,
        "fatigue": 1,
        "headache": 1,
        "nausea": 1,
        "dizziness": 2,
        "chest_pain": 4,
        "shortness_breath": 4
    }

    if fever: score += weights["fever"]
    if cough: score += weights["cough"]
    if fatigue: score += weights["fatigue"]
    if headache: score += weights["headache"]
    if nausea: score += weights["nausea"]
    if dizziness: score += weights["dizziness"]
    if chest_pain: score += weights["chest_pain"]
    if shortness_breath: score += weights["shortness_breath"]

    st.markdown("## 🧾 Assessment Result")

    st.progress(min(score/12, 1.0))

    st.write(f"### Total Risk Score: {score}")

    if score <= 3:
        st.success("🟢 Low Risk")
        st.write("Recommendation: Rest, stay hydrated, and monitor symptoms.")
    elif 4 <= score <= 7:
        st.warning("🟡 Moderate Risk")
        st.write("Recommendation: Monitor closely and consult a doctor if symptoms persist.")
    else:
        st.error("🔴 High Risk")
        st.write("Recommendation: Seek immediate medical attention.")

    st.markdown("---")
    st.caption("AI Symptom Risk Checker • Built with Streamlit")
