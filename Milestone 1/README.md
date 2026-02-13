🎯 Objective of the Milestone

  The objective of Milestone 1 is to develop the foundational web application interface for the FitPlan AI: Personalized Fitness Plan Generator project.
  
  This milestone focuses on:
  
  Creating a structured fitness profile form
  
  Collecting essential user health data
  
  Implementing accurate BMI calculation logic
  
  Classifying BMI into standard health categories

Deploying the application using Streamlit on Hugging Face Spaces

📌 BMI Formula Explanation

BMI (Body Mass Index) is calculated using the formula:

  BMI = Weight(kg)​/(Height(m))2​


Steps performed in the application:

  Convert height from centimeters to meters
  Height (m) = Height (cm) / 100
  
  Apply BMI formula
  BMI = weight / (height in meters)^2
  
  Round BMI to two decimal places
  
  Categorize BMI as:
  
  Underweight: BMI < 18.5
  
  Normal: 18.5 ≤ BMI < 25
  
  Overweight: 25 ≤ BMI < 30

Obese: BMI ≥ 30

🛠 Steps Performed
1. Form Creation

A structured Streamlit form was developed to collect:

Personal Information:

Name

Height (cm)

Weight (kg)

Fitness Details:

Fitness Goal

Available Equipment (Multiple Selection)

Fitness Level

2. Input Validation

The application ensures:

Required fields are not empty

Height and weight are positive values

Zero or negative inputs are rejected

Proper user error messages are displayed

3. BMI Calculation Logic

Height is converted from centimeters to meters

BMI is calculated using the standard formula

BMI is rounded to two decimal places

BMI category is determined based on WHO classification

4. Deployment

The application was deployed using:

Streamlit

Hugging Face Spaces

💻 Technologies Used

Python

Streamlit
