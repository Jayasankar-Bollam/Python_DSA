li=[1,6,8,4,5,9]
ans=0
for i in range(len(li)):
    #val=li[i]
    #if val>ans:
      #ans=val
    ans=max(li[i],ans)
print(ans)




"""
s="one problem a day"
temp=1
for i in range(len(s)):
    ch=s[i]
    if ch==" ":
        temp=temp+1
print(temp)"""




li=["hello good a ","bad","great work"]
ans=0
for j in range(len(li)):
    s=li[j]
    temp=1
    for i in range(len(s)):
        ch=s[i]
        if ch==" ":
            temp=temp+1
    ans=max(ans,temp)
print(ans) 
        
