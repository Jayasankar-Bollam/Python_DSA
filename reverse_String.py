# def rev_str(s):
#     return s[::-1]
# print(rev_str("hello"))


s="abccba"
n=len(s)/2
mu=len(s)
valid=True
for i in range(int(n)):
    l=s[i]
    r=s[mu-1-i]
    if l!=r:
        valid=False
        break
if valid:
    print("yes")
else:
    print("No")  