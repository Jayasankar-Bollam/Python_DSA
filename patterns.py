"""li=[["*","*","*"],["*","*","*"],["*","*","*"]]
r=len(li)         #r=3
c=len(li[0])         #c=4
for i in range(r):
    for j in range(c):
        print(li[i][j],end=" ")        #print("*",end=" ")
    print()



li=[["*","*","*"],["*","*","*"],["*","*","*"]]
r=3        #r=3
c=10     #c=4
for i in range(r):
    for j in range(c):
        print("*",end="")    
        if j!=c-1:
           print("-",end="")
    print()
"""








r=5
c=5
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
           print("*",end="")
        else:
           print(" ",end="")
        if j!=c-1:
           print(" ",end="")
    print()




"""r=4
c=20
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""





"""r=6
c=10
for i in range(r):
    for j in range (c):
        if i==0 or  i==1 or  i==2 or  i==3 or  i==4 or  i==5 or j==5 or j==6 or j==7 or j==8 or j==9:
                print("*",end="")
        else:
             print(" ",end="")
    print()  """       


"""
r=16
c=5
c1=r-1
for i in range(r):
    for j in range(c1-i):
        print(" ",end="")
    for k in range(c):
        print("*",end="")
    print()"""

"""n=15
for i in range(n):
    for j in range(n-i):
        print("-",end="")
    print()"""


"""r=10
for i in range(r):
    for j in range(r-i):
        print(" ",end="")
    temp=i*2+1
    for k in range(temp):
        print("*",end="")
    print()"""



r=9
n=r-1
for i in range(r):
    for j in range(i):
        print(" ",end="")
    temp=2*r-1-2*i
    for i in range(temp):
        print("*",end="")
    print() 