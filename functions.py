"""n=3
s="HIIII"
for i in range(n):
  print(s)


  #
n2=5
s2="Hello"
for i in range(n2):
  print(s2)"""



#
"""def fun(n):
  print("Hello")
  for i in range(n):
    print("Sankar") 
  print("Bye")
fun( 5)
fun(3)
fun(2)"""
"""

def fun(n):
   print("Hello")
   return n*n
print(fun(5))
  """

"""
#table
def table(n):
    for i in range(1, 21):
        print(n, "*", i, "=", n * i)
table(19)"""





"""
def table(n):
    for i in range(1,21):
        print(n,"*",i,"=",n*i)
table(6)"""



#leetcode

str="zaz"
ans=0
for i in range(len(str)-1):
    temp=abs(ord(str[i])-ord(str[i+1]))
    ans=ans+temp
print(ans)






lst=["--X","X--","X++","X++"]
x=0
for i in range(len(lst)):
    temp=lst[i]
    if temp=="--X" or temp=="X--":
        x=x-1
    else:
        x=x+1
print(x)
        

        #or
        #leetcode



