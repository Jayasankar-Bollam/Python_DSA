# dici={}
# dici[5]=3
# dici[6]=2
# dici[5]=dici[5]+1
# dici[5]=dici[5]+1
# dici[5]=dici[5]+1

# print(dici)

#




li=[1,5,8,0,8,1,5,1]
dici={}
for val in li:
    if val not in dici:
        dici[val]=1
    else:
        dici[val]=dici[val]+1
print(dici)


#
for i in dici:
    print(i,"->",dici[i])