class Circle:
    def __init__(self, radius):
        self.radius = radius
        print("Radius of the circle: ", radius)

    def Area(self):
        area = 3.14 * (self.radius) ** 2
        print("Area of the circle: ", area)

    def Perimeter(self):
        perimeter = 2 * 3.14 * (self.radius)
        print("Perimeter of the circle: ", perimeter)

c1 = Circle(7.5)
c1.radius
c1.Area()
c1.Perimeter()
