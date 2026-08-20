nums=[3,5,8,4,1]
n=len(nums)
nums.sort()
k=3
ans=float("inf")
for i in range(n):
    for j in range(i,n):
        temp=[]
        for m in range(i,j+1):
            temp.append(nums[m])
            if len(temp)==3:
                last=temp[-1]
                first=temp[0]
                ans=min(ans,last-first)
print(ans)
