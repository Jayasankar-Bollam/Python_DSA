num=131
temp=num
rev=0
while(temp>0):
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print("palindrome"if rev==num else "not palindrome")



#armstrong

num=153
temp=num
total=0
digits=len(str(num))
while temp>0:
    digit= temp%10
    total+=digit**digits
    temp=temp//10
print("armstrong" if total==num else "not armstrong")