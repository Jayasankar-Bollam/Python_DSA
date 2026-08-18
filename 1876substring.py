s="abacacabd"
n=len(s)
ans=0
for i in range(n):
    for j in range(i,n):
        temp=""
        for k in range(i,j+1):
            temp+=s[k]
        if len(temp)==3 and len(set(temp))==3:
                ans+=1
print(ans)



#optimal

s="xyzzaz"
n=len(s)
l=0
dici={}
ans=0
k=3
for r in range(n):
     if s[r] in dici:
          dici[s[r]]+=1
     else:
          dici[s[r]]=1


     if r-1==k:
          dici[s[l]]-=1
          if dici[s[l]]==0:
               dici.pop(s[l])
               l+=1


     if len(dici)==k:
          ans=+1 

print(ans)
     