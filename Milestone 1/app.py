import streamlit as st

st.set_page_config(
page_title="FitPlan AI",
page_icon="💪",
layout="wide"
)

st.title("💪 FitPlan AI")
st.caption("Personalized Fitness Profile — Milestone 1")

st.sidebar.header("📝 Enter Your Details")

name = st.sidebar.text_input("Name *")

col_h, col_w = st.sidebar.columns(2)
with col_h:
    height_cm = st.number_input("Height (cm) *", min_value=0.0, step=0.1)
with col_w:
    weight_kg = st.number_input("Weight (kg) *", min_value=0.0, step=0.1)

goal = st.sidebar.selectbox(
"Fitness Goal",
["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"]
)

equipment = st.sidebar.multiselect(
"Available Equipment",
["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment"]
)

level = st.sidebar.radio(
"Fitness Level",
["Beginner", "Intermediate", "Advanced"]
)

calculate = st.sidebar.button("🚀 Calculate BMI")

st.divider()

if calculate:

    if name.strip() == "" or height_cm <= 0 or weight_kg <= 0:
        st.error("Please enter valid values for all required fields.")
    
    else:
        height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)
    
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 24.9:
            category = "Normal"
        elif bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"
    
        st.subheader(f"👤 {name}'s Fitness Summary")
    
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="BMI", value=bmi)
        with m2:
            st.metric(label="Category", value=category)
    
        st.divider()
    
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
