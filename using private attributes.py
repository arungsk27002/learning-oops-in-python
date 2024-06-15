# class Account:
#     def __init__(self,accno,accpass):
#         self.accno=accno
#         self.__accpass=accpass
#     def privatemethoddefect(self):
#         print(self.__accpass)
# a1=Account(1010,3010)
# print(a1.privatemethoddefect())
class Person:
    __name="arun das h a"
    def __init__(self):
        pass
    def __hello(self):
        print("hi daa")
    def welcome(self):
        self.__hello()
p1=Person()
print(p1.welcome())