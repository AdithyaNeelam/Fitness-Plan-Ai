import streamlit as st
from prompt_builder import build_prompt
from model_api import query_model

st.set_page_config(
    page_title="FitPlan AI",
    page_icon="🏋️",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-top: 20px;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: #1e1e1e;
    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
}
.generate-btn {
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🏋️ FitPlan AI</div>', unsafe_allow_html=True)
st.caption("AI-Powered Personalized 5-Day Workout Planner")

st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="section-title">👤 Personal Details</div>', unsafe_allow_html=True)

    name = st.text_input("Name")
    age = st.number_input("Age", 12, 80, 20)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    st.markdown('<div class="section-title">📏 Body Metrics</div>', unsafe_allow_html=True)

    height = st.number_input("Height (cm)", 100, 250, 170)
    weight = st.number_input("Weight (kg)", 30, 200, 60)

with col2:
    st.markdown('<div class="section-title">🎯 Fitness Preferences</div>', unsafe_allow_html=True)

    goal = st.selectbox(
        "Fitness Goal",
        ["Weight Loss", "Muscle Gain", "General Fitness", "Endurance Improvement"]
    )

    fitness_level = st.selectbox(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    equipment = st.multiselect(
        "Available Equipment",
        ["Barbell", "Dumbbells", "Resistance Bands", "Treadmill", "Kettlebell"]
    )

st.markdown("---")

generate = st.button("🚀 Generate My Workout Plan")

if generate:

    if not name:
        st.error("Please enter your name.")
    else:
        prompt, bmi, bmi_status = build_prompt(
            name, age, gender,
            height, weight,
            goal, fitness_level,
            equipment
        )

        with st.spinner("Generating your personalized plan..."):
            plan = query_model(prompt)

        st.markdown("## 📊 Your Fitness Summary")
        summary_col1, summary_col2 = st.columns(2)

        with summary_col1:
            st.metric("BMI", f"{bmi:.2f}")

        with summary_col2:
            st.metric("BMI Category", bmi_status)

        st.markdown("---")
        st.markdown("## 🗓 5-Day Workout Plan")

        st.text_area("", plan, height=500)
