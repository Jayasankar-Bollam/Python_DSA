li=[7,1,2,3,4]
n=len(li)
for i in range(0,n-1):
    didSwapped=False
    for j in range(0,n-i-1):
        if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1],li[j]
            didSwapped=True
    print(li)
    if(didSwapped==False):
        break
print(li)


#didSwapped is optimal,notice in output then you know




#sort()
li=[4,6,3,2,1,8]
li.sort()
print(li)

#sorted(li)

li=[4,5,2,7,3,1,0]
temp=sorted(li)
print(temp)
print(li)