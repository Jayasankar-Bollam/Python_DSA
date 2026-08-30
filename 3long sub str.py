s = "abcabcbb"
uniset = set()
l=0
ans = 0
for r in range (len(s)):
    ch=s[r]
    if ch not in uniset:
        uniset.add(ch)
    else:
        while ch in uniset:
            uniset.remove(s[l])
            l+=1
        uniset.add(ch)

    ans=max(ans,r-l+1)
print(ans)

