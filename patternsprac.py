# r=4
# for i in range(r-1,-1,-1):
#     for j in range(r-i-1):
#         print(" ",end="")
#     for j in range(i*2+1):
#         if j==0 or j==i*2 or i==0 or i==1 or i==2 or i==r-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()




# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(j+1,end="")
#     print()


# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1,0,-1):
#         print(k,end="")
#     print()

#     n=5
#     for i in range(n):
#         for j in range(n-i-1):
#             print(" ",end="")
#         for k in range(i+1,0,-1):
#             print(k,end="")
#         for m in range(2,i+2):
#             print(m,end="")
#         print()



n=20
def table(n):
  for i in range(1,21):
    print(n, "*", i, "=", n*i)
table(21)
