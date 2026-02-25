def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def build_prompt(name, age, gender, height, weight, goal, fitness_level, equipment):
    bmi = calculate_bmi(weight, height)
    bmi_status = bmi_category(bmi)

    equipment_list = ", ".join(equipment) if equipment else "No Equipment"

    prompt = f"""
You are a certified professional fitness trainer.

Generate ONLY a structured 5-day workout plan.

User Profile:
Name: {name}
Age: {age}
Gender: {gender}
Height: {height} cm
Weight: {weight} kg
BMI: {bmi:.2f} ({bmi_status})
Goal: {goal}
Fitness Level: {fitness_level}
Available Equipment: {equipment_list}

STRICT RULES:
1. Output exactly 5 days.
2. Each day must contain 4–5 exercises.
3. Format exactly:
Day 1:
Exercise - Sets x Reps - Rest
4. No introduction paragraph.
5. No nutrition advice.
6. No explanations.
7. Keep output concise.
"""

    return prompt, bmi, bmi_status
