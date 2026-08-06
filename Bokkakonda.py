# # r=4
# # for i in range(r):
# #     for j in range(r-i-1):
# #         print(" ",end="")
# #     for j in range(i*2+1):
# #         if j==0 or j==i*2 or i==r-1:
# #          print("*",end="")
# #         else:
# #            print(" ",end="")
# #     print("")



# #reverse bokka padina konda muggu
# r=4
# for i in range(r-1,-1,-1):
#     for j in range(r-i-1):
#       print(" ",end="")
#     for j in range(i*2+1):
#       if j==0 or j==i*2 or i==r-1:
#          print("*",end="")
#       else:
#          print(" ",end="")
#     print()



r=4
for i in range(r-1):
     for j in range(r-i-1):
         print(" ",end="")
     for j in range(i*2+1):
         if j==0 or j==i*2 or i==r-1:
          print("*",end="")
         else:
            print(" ",end="")
     print("")
#reverse bokka padina konda muggu
for i in range(r-1,-1,-1):
    for j in range(r-i-1):
      print(" ",end="")
    for j in range(i*2+1):
      if j==0 or j==i*2 :
         print("*",end="")
      else:
         print(" ",end="")
    print()