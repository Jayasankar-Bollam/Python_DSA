nums = [12,1,3,1,1,6,7,1,8,1]
k=2
n=len(nums)
l=0
temp=0
ans=0
for r in range(n):
    if(nums[r]%2==1):
        temp+=1

    while(temp>k):
        if(nums[l]%2 ==1):
            temp-=1
        l+=1
    ans= max(ans,r-l+1)
print(ans) 
