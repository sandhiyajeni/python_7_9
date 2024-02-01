#list-it is a collection of homogenous and heteregenous datatype
#1,2,3----1,.12,"qdd"
#it is enclosed with in [] and each element is separated by using ,
#[1,2,3,4,5]
#it start with base index 0
'''
a=[1,2,3,4,5]
for i in a:
    print(i)

a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(a[:6])
print(a[5:13])
print(a[5:13:3])



Write a Python program to count the number of strings from a given list .
The string length is 2 or more and the first and last characters are the same.
Sample List : ['cbc', 'xyz', 'aba', '1221']
Expected Result : 3

a=['cb', 'z', 'aba', '1221']
b=0
for i in a:
    if len(i)>1:
        if i[0]==i[-1]:
            b=b+1
            print(i)
print(b)
'''
# Write a Python program to remove duplicates from a list.
a=[1,2,2,7,1,7]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    print(b)


            

