class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def Shownumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,number):
        newreal=self.real+number.real
        newimg=self.img+number.img
        return Complex(newreal,newimg)
    def __sub__(self,number):
        newreal=self.real-number.real
        newimg=self.img-number.img
        return Complex(newreal,newimg)
num1=Complex(3,4)
num1.Shownumber()
num2=Complex(5,6)
num2.Shownumber()
result=num1-num2
result.Shownumber()
result1=num1+num2
result1.Shownumber()