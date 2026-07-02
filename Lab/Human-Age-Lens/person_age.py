from datetime import date

class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
    
    def get_age(self):
        current_year = date.today().year
        return current_year - self.birth_year
    
    def introduce(self):
        print(f"Hi, this is {self.name} and I've just turned {self.get_age()} this year.")

nate = Person("Nate", 2003)
nate.introduce()
