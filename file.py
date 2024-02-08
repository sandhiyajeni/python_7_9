#file handling
a=open("Admiral.txt","r")
b=a.read(5)
print(b)
a.close()
import os
print(os.getcwd())
print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))