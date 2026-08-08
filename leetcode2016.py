li=[5,8,1,6]
n=len(li)
ans=0
for i in range(n):
    for j in range(i+1,n):
        if li[i]<li[j]:
           temp=li[j]-li[i]
           ans=max(ans,temp)
print(ans)



#optimal sol
nums=[3,2,10]
n=len(nums)
ans=-1
low=nums[0]
for j in range(1,n):
    if low<nums[j]:
        temp=nums[j]-low
        ans=max(ans,temp)
    low=min(low,nums[j])
print(ans)
