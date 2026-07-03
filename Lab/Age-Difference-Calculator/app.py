import streamlit as st
from datetime import date

from age_difference import compare_ages
from utils import format_result

st.title("Age Difference Calculator")

st.subheader("What's your name?")

name1 = st.text_input("Enter your name:")

dob1 = st.date_input(
    "Enter your date of birth:",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key="dob1"
)

st.divider()

st.subheader("Who do you want to compare your age with?")

name2 = st.text_input("Enter their name:")

dob2 = st.date_input(
    "Enter their date of birth:",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    key="dob2"
)

if st.button("Compare Ages"):

    if not name1.strip() or not name2.strip():
        st.warning("Please enter both of your names.")
    else:
        result = compare_ages(name1.strip(), dob1, name2.strip(), dob2)
        st.success(format_result(result))


st.markdown("---")
st.caption("Built by Nate!")
