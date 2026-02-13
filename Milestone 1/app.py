import streamlit as st

st.set_page_config(
    page_title="FitPlan AI",
    page_icon="💪",
    layout="wide"
)

st.sidebar.title("💪 FitPlan AI")
st.sidebar.caption("Personalized Fitness Profile")
st.sidebar.markdown("---")
st.sidebar.info("Milestone 1 – BMI Calculator")

st.markdown(
    """
    <h1 style='text-align: center;'>💪 FitPlan AI</h1>
    <p style='text-align: center; color: grey;'>Build your personalized fitness profile</p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

left, center, right = st.columns([1, 2, 1])

with center:

    st.subheader("📝 Enter Your Details")

    name = st.text_input("Name *")

    col1, col2 = st.columns(2)
    with col1:
        height_cm = st.number_input("Height (cm) *", min_value=0.0, step=0.1)
    with col2:
        weight_kg = st.number_input("Weight (kg) *", min_value=0.0, step=0.1)

    goal = st.selectbox(
        "Fitness Goal",
        ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
    )

    equipment = st.multiselect(
        "Available Equipment",
        ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment"]
    )

    level = st.radio(
        "Fitness Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    calculate = st.button("🚀 Calculate BMI", use_container_width=True)

st.markdown("---")

if calculate:

    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please enter valid values for all required fields.")

    else:
        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        st.subheader(f"👤 {name}'s Fitness Summary")

        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("BMI", bmi)
        with col_b:
            st.metric("Category", category)

        st.markdown("---")

        st.subheader("🏋️ Preferences")

        c1, c2, c3 = st.columns(3)
        with c1:
            st.write("**Goal**")
            st.write(goal)

        with c2:
            st.write("**Equipment**")
            st.write(", ".join(equipment) if equipment else "None")

        with c3:
            st.write("**Fitness Level**")
            st.write(level)
