#return length of the longest subarr with atmost k odd numbers.
# return number of subarrays with atmoost k odd numbers
#  
arr=[1,3,4,5,6]
k=2
l=0
n=len(arr)
ans=0
temp=0
for r in range(n):
    if arr[r]%2 ==1:
        temp+=1

    while temp >k:
        if arr [l]%2==1:
            temp-=1
        l+=1
    ans=max(ans,r-l+1)
    print(arr[l:r+1])
print(ans)



#atmost k 

def atMostK(arr,k):
    l=0
    n=len(arr)
    temp=0
    ans=0
    for r in range(n):
        if arr[r]%2==1:
            temp+=1

        while temp>k:
          if arr[l]%2==1:
            temp-=1
          l+=1
        ans+=r-l+1
print(ans)

arr =[1,3,4,5,7]
k=2
print(atMostK(arr,k))


