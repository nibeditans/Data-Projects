class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def calc_avg(self):
        avg = sum(self.marks)/3
        return avg

s1 = Student("Nibedita", [97, 98, 95])
print(f"{s1.name}'marks = {s1.marks}")
avg = s1.calc_avg()
print(f"So, her average score = {avg}")
