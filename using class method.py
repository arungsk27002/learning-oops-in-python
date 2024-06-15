class Person:
    name="anonymous"
    def __init__(self):
        self.__class__.name="arun"
    @classmethod
    def changename(cls,name):
        cls.name =name
a1=Person()
print(a1.name)
a1.changename("dasan")
print(a1.name, Person.name)