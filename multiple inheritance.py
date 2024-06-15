class A:
    welcome1="hi da"
class B:
    welcome2="hello da"
class C(A,B):
    welcome3="hello plus hi"
a1=C()
print(a1.welcome1)