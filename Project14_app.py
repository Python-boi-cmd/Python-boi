import streamlit as st
import random
st.set_page_config(page_title="Number Generator", page_icon=":small_airplane:", layout="wide")
x = random.randint(0,10)
y = random.randint(0,10)
st.write(f"What is {x} + {y}?")
z = st.number_input("Answer here: ")
if (z) == (x + y):
    st.write("Correct!")
else:
    st.write("Wrong.")
