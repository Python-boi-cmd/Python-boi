import streamlit as st


my_list = ["Addition", "Subtraction", "Multiplication", "Division"]

st.set_page_config(page_title="Math Calculator", page_icon=":small_airplane:", layout="wide")
item = st.selectbox("Select your Math Operation", my_list)

x = st.number_input("Enter your number here: ")
y = st.number_input("Enter your second number here: ")
if my_list == 0:
    st.write(f"The sum of {x} + {y} is {x + y}.")
elif my_list == 1:
    st.write(f"The difference of {x} - {y} is {x - y}.")
elif my_list == 2:
    st.write(f"The product of {x} * {y} is {x * y}.")
elif my_list == 3:
    st.write(f"The quotient of {x} / {y} is {x / y}")
