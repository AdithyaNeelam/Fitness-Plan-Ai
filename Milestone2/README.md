# Milestone 2 – Core AI Model Integration
## FitPlan AI: Personalized Fitness Plan Generator

## Objective
This milestone focuses on integrating a Large Language Model (LLM) into the application to dynamically generate personalized 5-day workout plans based on user inputs.

## Model Used
- Model: mistralai/Mistral-7B-Instruct-v0.2
- Accessed via Hugging Face Inference API

## Prompt Design
The prompt dynamically injects:
- Name
- Age
- Gender
- Height & Weight
- BMI and BMI Category
- Fitness Goal
- Fitness Level
- Available Equipment

Strict formatting rules were included to:
- Ensure exactly 5 workout days
- Maintain structured output
- Prevent unnecessary explanations

## Steps Performed
1. Loaded Hugging Face model using InferenceClient
2. Configured authentication using HF_TOKEN environment variable
3. Built dynamic structured prompts
4. Tested inference with multiple user scenarios
5. Integrated model with Streamlit UI
6. Deployed application to Hugging Face Spaces

## Sample Output
Example:
Day 1:
Barbell Bench Press - 4x8 - 2 min
Overhead Press - 3x10 - 90 sec
...

## Deployment
Hugging Face Space Link:
(Add your Space URL here)

## How to Run Locally
1. Set environment variable:
   - Windows: setx HF_TOKEN "your_token"
2. Install requirements:
   pip install -r requirements.txt
3. Run:
   streamlit run app.py
