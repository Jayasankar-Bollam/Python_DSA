fruits=[1,2,2]
l=0
dici={}
ans=0
k=2
for r in range(len(fruits)):
    val=fruits[r]
    if val in dici:
        dici[val]+=1
    else:
        dici[val]=1
    while  len(dici)>k:
        lval=fruits[l]
        dici[lval]-=1
        if dici[lval]==0:
            dici.pop(lval)
        l+=1
    ans=max(ans,r-l+1)
print(ans) ###

