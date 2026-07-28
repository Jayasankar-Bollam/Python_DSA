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
    print()"""









"""r=5
c=5
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
           print("*",end="")
        else:
           print(" ",end="")
        if j!=c-1:
           print(" ",end="")
    print()"""




"""r=4
c=20
for i in range(r):
    for j in range(c):
        if i==0 or i==r-1 or j==0 or j==c-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()"""





r=6
c=10
for i in range(r):
    for j in range (c):
        if i==0 or  i==1 or  i==2 or  i==3 or  i==4 or  i==5 or j==5 or j==6 or j==7 or j==8 or j==9:
                print("*",end="")
        else:
             print(" ",end="")
    print()         