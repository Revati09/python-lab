# #single 
# name='Revati'
# print(name)

# #double
# city="pune"
# print(city)

# #triple
# message='''hii good morning
# how are you?'''
# print(message)

#1
# string=input("Enter a string:")
# count=0
# for i in string:
#     count+=1
#     print("length of string is:",count)

#2
# string = input("Enter a string: ")

# vowels = consonants = digits = spaces = special = 0

# for ch in string:
#     if ch.lower() in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)


#3
# string = input("Enter a string: ")
# reverse = ""
# for ch in string:
#     reverse = ch + reverse
# print("Reverse =", reverse)

#4
# string= input("Enter a string:")

# if string == string[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

#5
# string= input("Enter a string:")
# upper=lower=0

# for ch in string:
#     if ch.isupper():
#         upper+=1
#     elif ch.islower():
#         lower+=1
# print("upper:",upper)
# print("lower:",lower)

#6
# string= input("Enter a string:")
# old= input("character to replace:")
# new= input("new character:")

# print(string.replace(old,new))

#7
# s = input("Enter a string: ")

# print("Result =", s.replace(" ", ""))

#8
# string = input("Enter a string:")
# ch = input("Enter a character:")
# print("Result =", string.count(ch))/

#9
# string = input("Enter a string:")
# print("first character=",string[0])
# print("last character=",string[-1])

#10
string = input("enter a string:")
for ch in string:
    print(ch, "=", ord(ch))