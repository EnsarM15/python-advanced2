import streamlit as st
from datetime import datetime

st.set_page_config(page_title="BMI Calculator", layout="centered")

st.title("BMI Calculator")

# Session state to store entries
if "people" not in st.session_state:
    st.session_state.people = []

# Input fields
name = st.text_input("Enter name:")
age = st.number_input("Enter age:", min_value=1, max_value=120, value=24)
weight = st.number_input("Enter weight in kilograms:", min_value=1.0, value=85.0)
height = st.number_input("Enter height in meters:", min_value=0.5, value=1.80)

# BMI function
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Category function
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Button
if st.button("Add Person"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.session_state.people.append({
        "date": datetime.now().strftime("%a, %b %d"),
        "name": name,
        "age": age,
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "category": category
    })

    st.success("A new person has been added!")

# Results section
st.subheader("Results")

for person in st.session_state.people:
    st.write(
        f"{person['date']}, "
        f"Weight: {person['weight']} kg, "
        f"Height: {person['height']} m, "
        f"BMI: {person['bmi']}, "
        f"Category: {person['category']}"
    )