Front-End Fitness Form & BMI Calculation
🎯 Objective

The objective of Milestone 1 is to develop the foundational web application interface for the FitPlan AI: Personalized Fitness Plan Generator project.

This milestone focuses on:

Building a structured fitness profile form

Collecting essential health information

Implementing accurate BMI calculation logic

Categorizing BMI into standard health classifications

Deploying the application on Hugging Face Spaces

📌 BMI Formula Explanation

BMI (Body Mass Index) is calculated using the formula:

BMI = weight (kg) / (height (m))²

Steps Performed:

Convert height from centimeters to meters

height_m = height_cm / 100


Apply BMI formula

bmi = weight / (height_m ** 2)


Round BMI to two decimal places

Categorize BMI:

Underweight: BMI < 18.5

Normal: 18.5 ≤ BMI < 25

Overweight: 25 ≤ BMI < 30

Obese: BMI ≥ 30

🛠 Steps Performed
1️⃣ Form Creation

A user-friendly fitness form was built using Streamlit.

Input Fields:
Personal Information

Name (Required)

Height (cm) (Required)

Weight (kg) (Required)

Fitness Details

Fitness Goal (Build Muscle, Weight Loss, Strength Gain, Abs Building, Flexible)

Available Equipment (Multiple Selection Allowed)

Fitness Level (Beginner, Intermediate, Advanced)

2️⃣ Input Validation

The application ensures:

Required fields are not empty

Height and weight are positive values

Zero or negative inputs are rejected

Appropriate error messages are displayed

3️⃣ BMI Logic Implementation

Height is converted from cm to meters

BMI is calculated using the standard formula

BMI is rounded to two decimal places

BMI category is displayed

User’s name is displayed along with BMI and category

🚀 Deployment

The application is deployed using:

Python

Streamlit

Hugging Face Spaces

GitHub

🔗 Live Application

👉 Add your Hugging Face Space link here

📂 Project Structure
FitPlan-AI/
└── Milestone1/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    └── screenshots/

📸 Screenshots

Screenshots of the running application are available in the screenshots/ folder.

⚙️ How to Run Locally

Clone the repository:

git clone <your-repo-link>


Navigate to Milestone1:

cd Milestone1


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

📦 Requirements
streamlit==1.32.0
