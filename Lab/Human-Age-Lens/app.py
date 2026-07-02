import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

class Person:
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date

    @property
    def age(self):
        today = date.today()
        return relativedelta(today, self.birth_date)

def plural(value, singular, plural):
    return singular if value == 1 else plural

st.title("How Old Are You, Really?")

name = st.text_input("Enter your name")
birth_date = st.date_input(
    "Enter your birth date",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):
    person = Person(name, birth_date)
    a = person.age

    st.write(
        f"Hello, {person.name}.\n\n"
        f"You're {a.years} year{'' if a.years == 1 else 's'}, "
        f"{a.months} {plural(a.months, 'month', 'months')}, and "
        f"{a.days} {plural(a.days, 'day', 'days')} old."
    )

st.markdown("---")
st.caption("Built by Nate • Streamlit + Python")
