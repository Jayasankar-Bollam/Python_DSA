# n=input()
# print(n)


# #int input
# n=int(input())
# print(n)


# #list input
# li=[]
# n=3
# for i in range(n):
#     temp=int(input())
#     li.append(temp)
# print(li)



# li=[]
# s="1 4 6"
# print(s.split())



#brute force way
li=[]
s="1 4 6"
temp=s.split()
for i in range(len(temp)):
    val=int(temp[i])
    li.append(val)
print(li)



#optimal way d

li=list(map(int,input().split()))
print(li)






li=[]

