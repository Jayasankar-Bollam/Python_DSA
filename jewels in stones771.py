# stones="aAbbbb"
# jewels="aA"
# ans=0
# for i in stones:
#     for j in jewels:
#         if j==i:
#             ans=ans+1
#             break
# print(ans)


stones="aAbbbb"
jewels="aA"
dici={}
for i in stones:
    if i in dici:
        dici[i]+=1
    else:
        dici[i]=1
ans=0
for i in range(len(jewels)):
    ch=jewels[i]
    if ch in dici:
        ans+=dici[ch]
print(ans)


# stones="aAbbbb"
# jewels="aA"
# ans=0
# for i in stones:
#     for j in jewels:
#         if j==i:
#             ans=ans+1
#             break
# print(ans)