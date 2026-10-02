"""s="ABCD"
print(s[3]+s[2]+s[1]+s[0])

#
print(list(range(3,-1,-1)))

#

str="abcde"
ans=""
ans=ans+str[4]
ans=ans+str[3]
ans=ans+str[2]
ans=ans+str[1]
ans=ans+str[0]
print(ans)

#
st='abc'
ans=""
for i in range(2,-1,-1):
    ans=ans+st[i]
    print(ans)
print(ans)


#BEST
lst=[5,7,6,8,5,3,2,1,9]
n=len(lst)
for i in range(n-1,-1,-1):
    print(lst[i])
"""



"""    #palindrome
str="abcd"
rev=""
for i in range(len(str)-1,-1,-1):
        rev=rev+str[i]
if rev==str:
        print('palindrome')
else:
       print("not palindrome")  
print(rev)
"""



s="abhhba"
n=len(s)//2
mu=len(s)
valid=True
for i in range(n):
        l=s[i]
        r=s[mu-1-i]
        if l!=r:
                valid=False
if valid:
        print('yes')
else:
        print("No")


#Optimized
"""s="abccba"
n=len(s)/2
mu=len(s)
valid=True
for i in range(int(n)):
    l=s[i]
    r=s[mu-1-i]
    if l!=r:
        valid=False
        break
if valid:
    print("yes")
else:
    print("No")"""


s="abccba"
print(len(s))