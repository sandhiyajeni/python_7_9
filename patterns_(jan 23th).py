#code for right angle triangle using *, number, alphabet
for i in range(1,6,1):
    for j in range(i):
        print("* ",end=" ")
    print()
print()

for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end=" ")
    print()
print()
for i in range(65,71,1):
    for j in range(65,i+1,1):
        print(chr(i),end=" ")
    print()
print()
#code for downward half - pyramid pattern  using *, number, alphabet
for i in range(6, 0, -1):      
    for j in range(0, i - 1):      
        print("*", end=' ')    
    print()
print()  
for i in range(5, 0, -1):      
    for j in range(0, i ,1):      
        print(i, end=' ')    
    print()  
print()
n=5
for i in range(n, 0, -1):
        num = 65
        for j in range(0, i):
            ch = chr(num)
            print(ch, end=" ")
            num = num +1
        print()
print()
print("welcome back")