# # #difference between biggest and smallest
# # arr=[10,20,40,50,30]
# # biggest=max(arr)
# # smallest=min(arr)
# # print(biggest-smallest)

# # #avg of an array
# # arr=[10,20,40,30,60]
# # total=0
# # for num in arr:
# #     total=total+num
# # avg=total+len(arr)
# # print(avg)

# # #sum of even numbers
# # arr=[1,2,3,4,5,6]
# # total=0
# # for num in arr:
# #     if num%2==0:
# #         total+=num
# # print(total)

# # #count duplicate elements in an array


# # arr=[1,2,3,4,5,6]
# # count=0
# # for i in range(len(arr)):
# #     if arr [i] in arr[:i]:
# #         count+=1
# #     print(count)


# # #create an array of even numbers

# # arr=[1,2,3,4,5,6,7,8]
# # even=[]
# # for num in arr:
# #     if num%2==0:
# #         even.append(num)
# # print(even)

# # #palindrome number
# # num=121
# # temp=num
# # rev=0
# # while temp>0:
# #     digit = temp % 10
# #     rev=rev*10+digit
# #     temp//=10
# #     print("palindrome"if num ==rev else "Not palindrome")

# #Palindrome string

# str="Sankar"
# rev=str
# for i in range(len(str)-1,-1,-1):
#     rev=rev+str[i]
# if rev==str:
#     print("pal")
# else:
#     print("Not pal")


# # Duplicates

# arr=[1,2,3,4,5,4,5,6,6,7]
# result=[]
# for i in arr:
#     if i not in result:
#         result.append(i)
# print(result)



# #table

# def table(n):
#     for i in range(1,21):
#         print(n, "*",i,"=", n*i)
# table(2)


# arr=[1,2,4,5,6,7,8,9]
# total=0
# for i in range(len(arr)):
#     total=total+i
# avg=total+len(arr)
# print(avg)


# #sum of even numbers in an array

# arr=[1,2,4,5,6,7,8,91,24,45]
# total=0
# for i in range(len(arr)):
#     if i%2==0:
#         total=total+i
# print(total)


#palindrome num

# num=131
# temp=num
# rev=0
# while temp>0:
#     digit=temp%10
#     rev=rev*10+digit
#     temp=temp//10
# print("palindrome" if num==rev else "not plaindrome")


# #table
# def table(n):
#     for i in range(1,31):
#         print(n,"*",i,"=",n*i)
# table(2)

# #duplicates
# arr=[1,3,4,5,6,7,8,9,10]
# result=[]
# for i in range(len(arr)):
#     if i not in result:
#         result.append(num)
# print(result)


#armstrong number

num=371
temp=num
total=0
digits=len(str(num))
while temp >0:
    digit=temp % 10
    total += digit**digits
    temp//=10
print("armstrong" if total==num else "not armstrong")



# Initialize variables
num = 371
temp_num = num
total = 0
digits = len(str(num))

# Loop through each digit
while temp_num > 0:
    digit = temp_num % 10
    total += digit ** digits
    temp_num //= 10

# Print the result
print("armstrong" if total == num else "not armstrong")



#create new array of leap year

years=[2000,2001,2004,2010,2020,2024]
leap_years=[]
for year in years:
    if year%400==0 or (year%4==0 and year%100!=0):
        leap_years.append(year)
print(leap_years)



#prime number
for num in range(2,100):
    prime=True
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
            print(num,end=" ")