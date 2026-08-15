# #my thinking
# li=[1,8,9]
# for i in range(len(li)):
#     for j in range(i,i+1):
#         print(li[i],li[j])


li=[1,8,9]
n=len(li)

for i in range(n):
    for j in range(i,n):
        for k in range(i,j+1):

           print(li[k],end=" ")
        print()