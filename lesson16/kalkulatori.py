import streamlit as st

def kalkulo(num1,num2,operation):
    if operation=="mbledhje":
        result = num1+num2
    elif operation=="zbritje":
        result = num1-num2

    return result

st.title("simple claculator")

num1 = st.number_input("enter the first number", step=1)
num2 = st.number_input("enter the first number", step=1)



opeartion = st.radio("select operation",["mbledhje","zbritje","shumezim","pjestim"])

result = kalkulo(num1,num2,opeartion)

st.write( result)