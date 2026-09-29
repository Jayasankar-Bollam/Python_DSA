nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
l=0
temp=0
n=len(nums)
ans=0
for r in range(len(nums)):
        if nums[r] == 0 :
            temp+=1
        while temp>k:
            if nums[l]==0:
                temp-=1
            l+=1
        ans=max(ans,r-l+1)
print(ans) 
 
