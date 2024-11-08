#create class circle include methods to calculate area and perimeter
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print("area=",3.14*self.radius**2)

    def perimeter(self):
        print("perimeter=",2*3.14*self.radius)

obj=Circle(4)
obj.area()
obj.perimeter()








































