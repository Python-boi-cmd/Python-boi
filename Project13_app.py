import streamlit as st


st.set_page_config(page_title="Addition Math Inputs", page_icon=":small_airplane:", layout="wide")


st.subheader("Enter your numbers to create the sum of them using addition.")
number = st.number_input("Insert a Number: ")
number2 = st.number_input("Enter your Second Number: ")
st.write(f"The sum of {number} and {number2} is {number + number2}.")
