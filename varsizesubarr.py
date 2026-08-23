li=[9,3,4,8,1]
ans=0
l=0
temp=0
k=10
for r in range(len(li)):
    temp+=li[r]
    while temp>k:
        temp-=li[r]
        l+=1
    ans=max(ans,r-l+1)
print(ans) 