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

    def introduce(self):
        a = self.age

        def plural(value, singular, plural):
            return singular if value == 1 else plural

        print(
            f"Hello, {self.name}.\n"
            f"You're {a.years} year{'' if a.years == 1 else 's'}, "
            f"{a.months} {plural(a.months, 'month', 'months')}, and "
            f"{a.days} {plural(a.days, 'day', 'days')} old."
        )

nate = Person("Nate", date(2003, 6, 1))
nate.introduce()
