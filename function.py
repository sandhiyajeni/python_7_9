''' #without argument & return value
def cube():
    a=int(input("enter a number"))
    print("cube of ",a**3)
cube()

# without argument & with return value
def cube1():
    a=int(input("enter a number"))
    return a**3
print("cube of 3 ",cube1())
print("cubic value",cube1())
# with argument & without return value
def add(a,b):
    print(a+b)
add(90,20)
# default argument
def country(a="india"):
    print(a)
country()
country("russia")'''
#keyword argument
def my(name,age):
    print(name," ",age)
my(21,"sakthi")
my(age=17,name="anu")
print()
