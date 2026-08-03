
"""r=9
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()"""



"""r=9
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    temp=2*r-1-2*i
    for i in range(temp):
        print("*",end="")
    print()"""

"""r=9
n=r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")
    print()
for i in range(r-2,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")
    print()"""



r=9
n=r-1

for i in range(r-1,-1,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")
    print()
for i in range(1,r):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2+1):
        print("*",end="")
    print()