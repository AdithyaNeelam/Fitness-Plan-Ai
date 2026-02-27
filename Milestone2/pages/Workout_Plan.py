import streamlit as st

st.set_page_config(
    page_title="Your Workout Plan",
    page_icon="🗓",
    layout="wide"
)

# If user directly opens page without generating
if "plan" not in st.session_state:
    st.warning("No workout plan found. Please generate one first.")
    if st.button("Go Back"):
        st.switch_page("app.py")
    st.stop()

st.markdown("## 🗓 Your Personalized 5-Day Workout Plan")
st.caption(f"Generated for {st.session_state['name']}")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.metric("BMI", f"{st.session_state['bmi']:.2f}")

with col2:
    st.metric("BMI Category", st.session_state["bmi_status"])

st.markdown("---")

st.markdown(st.session_state["plan"])

st.markdown("---")

if st.button("← Back to Input Page"):
    st.switch_page("app.py")
