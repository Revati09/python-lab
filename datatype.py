# # #integer

# # age=22
# # print(age)
# # print(type(age)) 

# # # Float
# # price = 99.99

# # print(price)
# # print(type(price))

# # # String
# # name = "Revati"

# # print(name)
# # print(type(name))

# # # Boolean
# # is_student = True

# # print(is_student)
# # print(type(is_student))

# # # List
# # fruits = ["Apple", "Banana", "Mango"]

# # print(fruits)
# # print(type(fruits))

# # # Tuple
# # numbers = (10, 20, 30)

# # print(numbers)
# # print(type(numbers))

# # # Set
# # colors = {"Red", "Green", "Blue"}

# # print(colors)
# # print(type(colors))# Set
# # colors = {"Red", "Green", "Blue"}

# # print(colors)

#1
# n=int (input("enter a number:"))

# for i in range(1, n+1):
#     print(i)

# #2

# n=int (input("Enter a number:"))

# for i in range(2, n+1, 2):
# print(i)

# #3
# n=int (input("Enter a number:"))

# for i in range(n):
# if i % 2!=0:
# print(i)

# #4
# n=int (input("Ente

# #8
# for i in range(3):
#     for j in range(3):
#         print(chr(65 + j), end=" ")
#     print()

# #9
# for i in range(1, n+1):
#  for j in range(3):
#   print(chr(65 + j)end="")
#   print(n)

# #10
# n=int (input("Enter a number:")
#        i=1
#        while i <= n:
#        print(i)
#        i += 1

# #11
# n=int (input("Enter a number:")
#        i = 2
#        while i <= n:
#        print(i)
#        i += 2
       
# #12
# n=int (input("Enter a number:"))
#       i = 1
#       while i<=n:
#       print(i)
#       i += 2

# #13
# n=int (input()


#1
# n = int(input("Enter number: "))
# i = 1

# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1

#2
# n = int(input("Enter number: "))
# temp = n
# rev = 0

# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10

# if rev == n:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#3
# n = int(input("Enter number: "))

# i = 2
# flag = True

# while i < n:
#     if n % i == 0:
#         flag = False
#         break
#     i += 1

# if n > 1 and flag:
#     print("Prime Number")
# else:
#     print("Not Prime Number")

#4
# n = int(input("Enter number: "))
# sum = 0

# while n > 0:
#     digit = n % 10
#     sum += digit
#     n //= 10

# print("Sum of digits =", sum)

#5
n=int (input("Enter a number:"))
fact=1



