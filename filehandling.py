#write
file  = open("student.txt","w")
file.write("My name is revati\n")
file.write("I am 22 years old.")

file.close()
print("data written successfully")

#read
file = open("student.txt","r")
data = file.read()
print(data)
file.close()

#append
file = open("student.txt","a")
file.write("\nI am from Dy.Patil college.")
file.close()
print("data appended successfully")

#read after append
file = open("student.txt","r")

for line in file:
    print(line.strip())
file.close()

#count number of characters in file

file = open("student.txt","r")
data =file.read()
print("Number of character:",len(data))
file.close()

#count number of lines in file
file = open("student.txt","r")
lines = file.readlines()
print("Number of lines:",len(lines))
file.close() 

#count number of words in file
file = open("student.txt","r")
data = file.read()
words = data.split()
print("number of words:",len(words))
file.close()

#check whether file exits
import os
if os.path.exists("student.txt"):
    print("file exits")
else:
    print("file does not exits") 

#create a file using with open()
with open("student.txt","w") as file:
    file.write("My name is revati\n")
    file.write("I like to watch cricket.")
print("file created successfully")

#read file using with open()
with open("student.txt","r") as file:
    data = file.read()
    print(data)








    