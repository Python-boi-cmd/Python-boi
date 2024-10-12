import streamlit as st


my_list = ["Addition", "Subtraction", "Multiplication", "Division"]


item = st.selectbox("Select your Math Operation", my_list)

x = st.number_input("Enter your number here: ")
y = st.number_input("Enter your second number here: ")
sum_result = x + y
difference_result = x / y
product_result = x * y
division_result = x / y
if division_result < 1:
    st.write("Undefined number, cannot divide by zero")
else:
    st.write(f"The answer of {x} / {y} is {x / y}")

