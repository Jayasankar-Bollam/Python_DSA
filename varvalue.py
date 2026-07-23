lst=["--X","X++","X++","X++"]
x=0
for i in range(len(lst)):
    temp=lst[i]
    if temp=="--X" or temp=="X--":
        x=x-1
    else:
        x=x+1
print(x)