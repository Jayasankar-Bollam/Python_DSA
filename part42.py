#How return works in functions
# # def func(val):
#    print("start fun")
#    if val==1:
#        return "middle func"
#    print("after func")            #after return statement nothing is printed until we call particularly********************
# ans=func(1)
# print(ans)

    
# def fun(val):
#     print("start fun")
#     if val==1:
#         return "middile fun"
#     print("after fun")
#     return ("last fun")
# ans= fun(2)
# print(ans)



# def fun(val):
#     li=[1,2,3,4,5,6]
#     for i in li:
#         if i in li:
#             return True
#         return False
# ans=fun(3)
# print(ans)

#How to send dici as a parameter into function

# def fun(s1,s2):
#     for i in range(len(s1)):
#         if s1[i]!=s2[i]:
#             return False
#     return  True
# ans=fun("abc","abd")
# print(ans)

# def func(dici):
#     print(dici)
# dici={1:4}
# func(dici)


#using func two hashmaps are equal or not checking(compare)
# def func(dicia,dicib):
#     if (dicia==dicib):
#         return True
#     return False
# dicia={1:4,2:7}
# dicib={2:7,1:4}
# ans=func(dicia,dicib)
# print(ans)


# def fun(dicia,dicib):
#     if len(dicia)!=len(dicib):
#         return False
#     for i in dicia:
#         if i not in dicib:                               #if i not in dicib or dicia[i]!=dicib[i]:    #order is very imp ******************
#             return False
#         if dicia[i]!=dicib[i]:
#             return False
#     return True
# dicia={1:4,2:7}
# dicib={2:7,1:4}
# ans=fun(dicia,dicib)
# print(ans)



#How to check if two strings are anagrams are not
def fun(dicia,dicib):
    if len(dicia)!=len(dicib):
        return False
    for i in dicia:
        if i not in dicib:                               #if i not in dicib or dicia[i]!=dicib[i]:    #order is very imp ******************
            return False
        if dicia[i]!=dicib[i]:
            return False
    return True
dicia={}
dicib={}
s1="abceab"
s2="bbaac"
for i in s1:
    if i in dicia:
        dicia[i]+=1
    else:
        dicia[i]=1
for i in s2:
    if i in dicib:
        dicib[i]+=1
    else:
        dicib[i]=1
ans=fun(dicia,dicib)
print(ans)