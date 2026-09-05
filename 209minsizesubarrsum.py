nums=[2,3,1,2,4,1]
n=len(nums)
target=0
l=0
temp=0
ans=float("inf")
for r in range(n):
    temp+=nums[r]


    while temp>=target:
        ans=min(ans,r-l+1)
        temp-=nums[l]
        l+=1
if ans==float("inf"):
    print(0)
print(ans)