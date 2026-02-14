# FitPlan AI – Milestone 1
## Front-End Fitness Form & BMI Calculation

---

## 🎯 Objective

The objective of **Milestone 1** is to develop the foundational web application interface for the **FitPlan AI: Personalized Fitness Plan Generator** project.

This milestone focuses on:

- Building a structured fitness profile form  
- Collecting essential user health details  
- Implementing accurate BMI calculation logic  
- Classifying BMI into standard health categories  
- Deploying the application on Hugging Face Spaces  

---

## 📌 BMI Formula Explanation

Body Mass Index (BMI) is calculated using the standard formula:


### Calculation Steps

1. Convert height from centimeters to meters  

2. Apply BMI formula  

3. Round BMI to two decimal places  

4. Categorize BMI as:

| BMI Range | Category |
|----------|----------|
| < 18.5 | Underweight |
| 18.5 – 24.9 | Normal |
| 25 – 29.9 | Overweight |
| ≥ 30 | Obese |

---

## 🛠 Implementation Details

### 1️⃣ Form Creation

A user-friendly fitness profile form was built using **Streamlit**.

#### Personal Information
- Name (Required)
- Height in centimeters (Required)
- Weight in kilograms (Required)

#### Fitness Details
- Fitness Goal (Build Muscle, Weight Loss, Strength Gain, Abs Building, Flexible)
- Available Equipment (Multiple Selection Allowed)
- Fitness Level (Beginner, Intermediate, Advanced)

---

### 2️⃣ Input Validation

The application ensures:

- Required fields are not left empty  
- Height and weight are positive values  
- Zero or negative inputs are rejected  
- Clear error messages are displayed for invalid inputs  

---

### 3️⃣ BMI Logic Implementation

- Height is converted from centimeters to meters  
- BMI is calculated using the standard formula  
- BMI is rounded to two decimal places  
- BMI category is determined correctly  
- User’s name, BMI, and category are displayed together  

## 🔗 Live Application (Hugging Face)

👉 **https://huggingface.co/spaces/Adithya-Neelam/Ai-Fitness-Plan**
