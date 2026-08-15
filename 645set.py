nums=[1,2,2,4]
s=set()
duplicate=-1
missing=-1
for i in range(len(nums)):
    val=nums[i]
    if i not in s:
        s.add(val)
    else:
        duplicate=val
print(s)
for i in range(1,len(nums)+1):
    if i not in s:
        missing=i
print(duplicate,missing)