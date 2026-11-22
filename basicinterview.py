# #difference between biggest and smallest
# arr=[10,20,40,50,30]
# biggest=max(arr)
# smallest=min(arr)
# print(biggest-smallest)

# #avg of an array
# arr=[10,20,40,30,60]
# total=0
# for num in arr:
#     total=total+num
# avg=total+len(arr)
# print(avg)

# #sum of even numbers
# arr=[1,2,3,4,5,6]
# total=0
# for num in arr:
#     if num%2==0:
#         total+=num
# print(total)

# #count duplicate elements in an array


# arr=[1,2,3,4,5,6]
# count=0
# for i in range(len(arr)):
#     if arr [i] in arr[:i]:
#         count+=1
#     print(count)


# #create an array of even numbers

# arr=[1,2,3,4,5,6,7,8]
# even=[]
# for num in arr:
#     if num%2==0:
#         even.append(num)
# print(even)

# #palindrome number
# num=121
# temp=num
# rev=0
# while temp>0:
#     digit = temp % 10
#     rev=rev*10+digit
#     temp//=10
#     print("palindrome"if num ==rev else "Not palindrome")

#Palindrome string

str="Sankar"
rev=str
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
if rev==str:
    print("pal")
else:
    print("Not pal")


# Duplicates

arr=[1,2,3,4,5,4,5,6,6,7]
result=[]
for i in arr:
    if i not in result:
        result.append(i)
print(result)