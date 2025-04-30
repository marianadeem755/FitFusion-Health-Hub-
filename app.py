import streamlit as st
from datetime import date
import random

# ---- Page Config ----
st.set_page_config(page_title="Health App", layout="centered", page_icon="🧮")

# ---- Custom Global CSS ----
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://i.pinimg.com/736x/d5/f2/84/d5f284d6d139dad2eecee48f935aad43.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    [data-testid="stSidebar"] {
        background-image: url('https://img.freepik.com/free-vector/abstract-background_53876-90689.jpg?semt=ais_hybrid&w=740');
        background-size: cover;
        background-position: center;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        box-shadow: 0 0 15px rgba(0,0,0,0.1);
    }

    h1, h2, h3 {
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
    }

    .stButton>button {
        background-color: #6a1b9a;
        color: white;
        border-radius: 12px;
        padding: 0.5em 1em;
        font-weight: bold;
        transition: 0.3s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #ab47bc;
        transform: scale(1.05);
    }

    .stSelectbox, .stNumberInput, .stDateInput, .stTextInput {
        border-radius: 10px;
        padding: 10px;
        background-color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }

    .metric-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---- Title ----
st.title("🧮  FitFusion: Your Health Hub!")
st.caption("✨ BMI, Age, BMR, Water Intake & Ideal Weight Calculator & Tips Recommender")

# ---- Sidebar Navigation ----
menu = st.sidebar.selectbox(
    "🔍 Select a Feature",
    [
        "🏋️ BMI Calculator", "📅 Age Calculator", "⚖️ Ideal Weight",
        "🔥 BMR Calculator", "💧 Water Intake", "💡 Health Tip"
    ]
)

# ---- Sidebar Info ----
st.sidebar.markdown("## 🔗 Connect With Me")
st.sidebar.markdown("""
<a href="https://github.com/marianadeem755" target="_blank">🌐 GitHub</a><br>
<a href="https://www.kaggle.com/marianadeem755" target="_blank">📊 Kaggle</a><br>
<a href="mailto:marianadeem755@gmail.com">📧 Email</a><br>
<a href="https://huggingface.co/maria355" target="_blank">🤗 Hugging Face</a>
""", unsafe_allow_html=True)

# ---- BMI Calculator ----
if menu == "🏋️ BMI Calculator":
    st.header("🏋️‍♂️ BMI Calculator")
    col1, col2 = st.columns(2)
    with col1:
        height_type = st.selectbox("Height Type", ["Feet/Inches", "Centimeters"])
    if height_type == "Feet/Inches":
        with col1:
            feet = st.number_input("Height (feet)", min_value=1, max_value=8, value=5)
        with col2:
            inches = st.number_input("Height (inches)", min_value=0, max_value=11, value=7)
    else:
        height_cm = st.number_input("Height (cm)", min_value=50, max_value=300, value=170)
    weight = st.number_input("Weight (kg)", min_value=1, max_value=300, value=70)

    if st.button("Calculate BMI"):
        if height_type == "Feet/Inches":
            total_inches = feet * 12 + inches
            height_m = total_inches * 0.0254
        else:
            height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        st.markdown(f"<div class='metric-box'><h2>Your BMI: {bmi:.2f}</h2></div>", unsafe_allow_html=True)
        if bmi < 18.5:
            st.warning("⚠️ You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight.")
        else:
            st.error("❗ You are obese.")

# ---- Age Calculator ----
elif menu == "📅 Age Calculator":
    st.header("📅 Age Calculator")
    birth_date = st.date_input("Enter your birthdate", min_value=date(1900, 1, 1), max_value=date.today())
    if st.button("Calculate Age"):
        today = date.today()
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day
        
        # Adjust months and days if necessary
        if age_months < 0:
            age_years -= 1
            age_months += 12
        if age_days < 0:
            if age_months == 0:
                age_years -= 1
                age_months = 11
            age_days += (today.replace(year=today.year, month=today.month) - today.replace(year=today.year, month=today.month-1)).days
        
        st.markdown(f"<div class='metric-box'><h2>Your Age: {age_years} years, {age_months} months, {age_days} days</h2></div>", unsafe_allow_html=True)

# ---- Ideal Weight ----
elif menu == "⚖️ Ideal Weight":
    st.header("⚖️ Ideal Weight Calculator")
    gender = st.selectbox("Select Gender", ["Male", "Female"])
    height_type = st.selectbox("Height Type", ["Feet/Inches", "Centimeters"])
    if height_type == "Feet/Inches":
        col1, col2 = st.columns(2)
        with col1:
            feet = st.number_input("Height (feet)", 1, 8, 5)
        with col2:
            inches = st.number_input("Height (inches)", 0, 11, 7)
    else:
        height_cm = st.number_input("Height (cm)", min_value=50, max_value=300, value=170)

    if st.button("Calculate Ideal Weight"):
        if height_type == "Feet/Inches":
            total_inches = feet * 12 + inches
            if gender == "Male":
                ideal_weight = 50 + 2.3 * (total_inches - 60)
            else:
                ideal_weight = 45.5 + 2.3 * (total_inches - 60)
        else:
            if gender == "Male":
                ideal_weight = 50 + 2.3 * ((height_cm / 2.54) - 60)
            else:
                ideal_weight = 45.5 + 2.3 * ((height_cm / 2.54) - 60)
        
        st.markdown(f"<div class='metric-box'><h2>Ideal Weight: {ideal_weight:.2f} kg</h2></div>", unsafe_allow_html=True)

# ---- BMR ----
elif menu == "🔥 BMR Calculator":
    st.header("🔥 BMR (Calories Needed)")
    gender = st.selectbox("Gender", ["Male", "Female"])
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    height_type = st.selectbox("Height Type", ["Feet/Inches", "Centimeters"])
    col1, col2 = st.columns(2)
    with col1:
        if height_type == "Feet/Inches":
            feet = st.number_input("Height (feet)", 1, 8, 5, key="bmr_ft")
        else:
            height_cm = st.number_input("Height (cm)", 50, 300, 170, key="bmr_cm")
    with col2:
        if height_type == "Feet/Inches":
            inches = st.number_input("Height (inches)", 0, 11, 7, key="bmr_in")
    
    age = st.number_input("Age (years)", 1, 120, 25)

    if st.button("Calculate BMR"):
        if height_type == "Feet/Inches":
            total_inches = feet * 12 + inches
            height_cm = total_inches * 2.54
        height_m = height_cm / 100
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
        st.markdown(f"<div class='metric-box'><h2>Your BMR: {bmr:.2f} cal/day</h2></div>", unsafe_allow_html=True)

# ---- Water Intake ----
elif menu == "💧 Water Intake":
    st.header("💧 Daily Water Intake")
    weight = st.number_input("Weight (kg)", 30, 200, 70)
    if st.button("Get Recommendation"):
        water_liters = weight * 0.033
        st.markdown(f"<div class='metric-box'><h2>{water_liters:.2f} liters/day</h2></div>", unsafe_allow_html=True)

# ---- Health Tip ----
elif menu == "💡 Health Tip":
    st.header("💡 Daily Health Tips")
    tips = [
        "🚰 Drink at least 2L of water daily.",
        "🥦 Eat more veggies and fruits.",
        "🚶 Walk at least 30 minutes daily.",
        "🍫 Cut down sugar and processed foods.",
        "🛌 Sleep 6-7 hours every night.",
        "🧘 Practice mindfulness regularly.",
        "👀 Take screen breaks for your eyes.",
        "🏋️ Add strength training weekly.",
        "🥗 Balance your diet with proteins.",
        "🌞 Get sunlight—vitamin D matters!",
    ]
    if st.button("Get a Tip"):
        selected_tips = random.sample(tips, 3)
        for tip in selected_tips:
            st.success(tip)
