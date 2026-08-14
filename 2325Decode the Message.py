# key = "the quick brown fox jumps over the lazy dog"
# dici={}
# temp=97
# for i in key:
#     if i!=" " and i not in dici:
#         dici[i]=chr(temp)
#         temp+=1
# #print(dici)
# message = "vkbs bs t suepuv"
# ans=""
# for i in message:
#     if i==" ":
#         ans+=" "
#     else:
#         ans+=dici[i]
# print(ans)









key= "zyxwvutsrqponmlkjihgfedcba"
dici={}
temp=97
for i in key:
    if i!=" " and i not in dici:
        dici[i]=chr(temp)
        temp+=1
    print(dici)
message="today i learn decode the message"

ans=""
for i in message:
    if i==" ":
        ans+=" "
    else:
        ans+=dici[i]
print(ans)