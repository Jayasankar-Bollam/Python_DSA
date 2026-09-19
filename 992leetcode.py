
nums=[1,2,1,2,3]
k=2
def atMostK(nums,k):
    l=0
    n=len(nums)
    dici={}
    ans=0
    for r in range(n):
        val=nums[r]
        if val in dici:
            dici[val]+=1
        else:
            dici[val]=1
        while(len(dici)>k):
            lval=nums[l]
            dici[lval]-=1
            if dici[lval]==0:
                dici.pop(lval)
            l+=1
        ans=ans+r-l+1

    return ans
print(atMostK(nums,k)-atMostK(nums,k-1)) 
   
