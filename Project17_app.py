import streamlit as st

st.title("University Admission Based on GPA")

x = st.number_input("Enter your GPA here:", min_value=0.0, max_value=4.0, step=0.1)

if 0 <= x < 2.0:
    st.write(f'''
    You can get into these types of universities with a GPA of {x}:
    - Community colleges
    - Alternative admissions programs
    - State universities
    ''')
elif 1.9 <= x < 2.6:
    st.write(f'''
    You can get into these universities with a GPA of {x}:
    - State Universities w/ Flexible Admissions
    - Less Selective Private Colleges
    - Technical and Vocational Schools
    - Pathway Programs
    ''')
elif 2.4 <= x < 3.0:
    st.write(f'''
    With a GPA of {x} you can get into:
    - Better Public Uni/State Uni (Depends)
    - Moderately Selective Private Colleges
    - Alternative Admission Programs
    ''')
elif 2.9 <= x < 3.5:
    st.write(f'''
    With a GPA of {x} you can get into: 
    - State Flagship Universities
    - Competitive Liberal Arts Colleges
    - Public Honors Colleges
    ''')
elif 3.4 <= x <= 4.0:
    st.write(f'''
    With a GPA of {x} you can get into: 
    - Highly Selective State Universities
    - Highly Selective Liberal Arts Colleges
    - Top-Ranked Private Universities
    ''')
else:
    st.write("Please enter a valid GPA between 0.0 and 4.0.")