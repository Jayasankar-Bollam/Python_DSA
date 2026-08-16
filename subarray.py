# #my thinking
# li=[1,8,9]
# for i in range(len(li)):
#     for j in range(i,i+1):
#         print(li[i],li[j])


li=[1,8,9,5,6]
n=len(li)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=[]
        for k in range(i,j+1):
           temp.append(li[k])
        ans.append(temp)
print(ans)



str="Sankar"
n=len(str)
ans=[]
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=(str[k])
        ans.append(temp)
print(ans)