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
# string = input("enter a string:")
# for ch in string:
#     print(ch, "=", ord(ch))

# #11
# string = input("enter a string:")
# words = string.split()

# print("Total Words =", len(words))

#12
# string = input("enter a string:")
# words = string.split()
# longest = words[0]

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print("Longest Word =", longest)

#13
# string = input("Enter a string:")
# words = string.split()
# shortest = words[0]

# for word in words:
#     if len(word) < len(shortest):
#         shortest = word

# print("shortest word =", shortest)

#14
# string = input("Enter a string:")
# print("Title case =", string.title())

#15
# s = input("Enter a string: ")
# print("Duplicate Characters:")
# for ch in set(s):
#     if s.count(ch) > 1:
#         print(ch) 

#16
# string = input("Enter a string:")
# for ch in set(string):
#     print(ch, "=", string.count(ch))

#17
# s1 = input("Enter a first string:")
# s2 = input("Enter a second string:")

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

#18
# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch not in result:
#         result += ch
# print("Result =", result)

#19
# s = input("Enter a string:")
# sub = input("Enter a substring:")
# if sub in s:
#     print("substring is present")
# else:
#     print("substring is not present")

#20
# s = input("Enter a sentence: ")
# word = input("Enter word to search: ")
# words = s.split()
# count = words.count(word)
# print("Occurrences =", count)

#21
# password = input("Enter Password: ")

# if (len(password) >= 8 and
#     any(ch.isupper() for ch in password) and
#     any(ch.islower() for ch in password) and
#     any(ch.isdigit() for ch in password) and
#     any(not ch.isalnum() for ch in password)):
#     print("Valid Password")
# else:
#     print("Invalid Password") 

#22

