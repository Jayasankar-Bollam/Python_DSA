n=6
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print()


n=6
for i in range(n):
    for j in range(i+1):
       print(j+1,end=" ")
    print()



n=6
for i in range(n):
    for j in range(1,i+2):
        print(j,end=" ")
    print()


n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1,0,-1):
        print(k,end="")
    print()



# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1,0,-1):
#         print(k,end="")
#     for m in range(2,i+2):
#         print(m,end="")
#     print()