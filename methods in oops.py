import math
class Calculator:
    
    
    def __init__(self,number):
        self.number=number
    def square(self):
        return self.number*self.number
    def cube(self):
        return self.number*self.number*self.number
    def squareroot(self):
        return math.sqrt(self.number)
    @staticmethod
    def hello():
        print("hello my world")
    
c1=Calculator(10)
print(c1.squareroot(),c1.square(),c1.cube())
print(c1.hello())