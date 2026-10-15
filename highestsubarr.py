#Highest subarr                                        O(n^3)
li=[5,9,1,8,7]
n=len(li)
ans=0
for i in range(n):
    for j in range(i,n):
        tli=[]
        tsum=0
        for k in range(i,j+1):                                                     
            tli.append(li[k])
            tsum+=li[k]
        if len(tli)==3:
            ans=max(ans,tsum)
print(ans)






#optimal approach

#sliding window ,Two pointers

li=[5,9,1,8,7]
n=len(li)
l=0
temp=0
k=3
ans=0
for r in range(n):
    temp+=li[r]

 
    if (r-l==3):              #(r-l+1==4)
      temp-=li[l]
      l+=1


    if (r-l+1==k):
        ans=max(ans,temp)
print(ans)



       
          
 