class Circle:
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return (22/7*self.r**2)
    def perimeter(self):
        return (2*22/7*self.r)
Circle1 = Circle(4)
print(Circle1.area(),Circle1.perimeter())
