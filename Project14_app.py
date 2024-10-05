import streamlit as st
import random

st.set_page_config(page_title="Number Generator", page_icon=":small_airplane:", layout="wide")
st.write("The number you enter will be selected for the generator for example 1 - (input of user)")
number = st.number_input("Enter a Number: ")
st.write(f"The number you selected is {number}")
st.write(f"1 - {number}")
x = random.randint(0,{number})
st.write(f"The selected number from the generator is {number}")
