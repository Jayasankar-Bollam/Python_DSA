arr=[17,18,5,4,6,1]
n=len(arr)
ans=[]
for i in range(n-1):
     temp=float("-inf")
     for j in range(i+1,n):
          temp=max(temp,arr[j])
     ans.append(temp)
ans.append(-1)

print(ans)



#optimal solution
arr=[17,18,5,4,6,1]
n=len(arr)
rmax=-1
for i in range(n-1,-1,-1):
     temp=arr[i]
     arr[i]=rmax
     rmax=max(rmax,temp)
print(arr)











