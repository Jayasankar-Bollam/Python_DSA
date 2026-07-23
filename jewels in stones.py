stones="aAbbbb"
jewels="aA"
ans=0
for i in stones:
    for j in jewels:
        if j==i:
            ans=ans+1
            break
print(ans)
