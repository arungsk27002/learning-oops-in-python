class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
    @property
    def calculatepercentage(self):
        return str((self.phy+self.chem+self.maths)/3)+"%"
Student1=Student(98,99,100)
print(Student1.calculatepercentage)