# students = []
# grades = []

# # Add student
# def add_student():
#     name = input("Enter student name: ")
#     grade = int(input("Enter grade: "))
#     students.append(name)
#     grades.append(grade)
#     print("Student added successfully!")

# # Update grade
# def update_grade():
#     name = input("Enter student name to update: ")

#     if name in students:
#         index = students.index(name)
#         new_grade = int(input("Enter new grade: "))
#         grades[index] = new_grade
#         print("Grade updated successfully!")
#     else:
#         print("Student not found.")

# # Remove student
# def remove_student():
#     name = input("Enter student name to remove: ")

#     if name in students:
#         index = students.index(name)
#         students.pop(index)
#         grades.pop(index)
#         print("Student removed successfully!")
#     else:
#         print("Student not found.")

# # Display average
# def average_grade():
#     if len(grades) > 0:
#         avg = sum(grades) / len(grades)
#         print("Average Grade =", avg)
#     else:
#         print("No records.")

# # Highest and Lowest
# def highest_lowest():
#     if len(grades) > 0:
#         print("Highest Grade =", max(grades))
#         print("Lowest Grade =", min(grades))
#     else:
#         print("No records.")

# # Display students
# def display():
#     if len(students) == 0:
#         print("No student records.")
#     else:
#         print("\nStudent Records")
#         for i in range(len(students)):
#             print(students[i], ":", grades[i])

# # Menu
# while True:
#     print("\n1.Add Student")
#     print("2.Update Grade")
#     print("3.Remove Student")
#     print("4.Average Grade")
#     print("5.Highest & Lowest")
#     print("6.Display")
#     print("7.Exit")

#     choice = int(input("Enter choice: "))

#     if choice == 1:
#         add_student()
#     elif choice == 2:
#         update_grade()
#     elif choice == 3:
#         remove_student()
#     elif choice == 4:
#         average_grade()
#     elif choice == 5:
#         highest_lowest()
#     elif choice == 6:
#         display()
#     elif choice == 7:
#         print("Program Ended")
#         break
#     else:
#         print("Invalid Choice")



# mark = 84

# if mark >= 90:
#     grade = "a"
# elif mark >= 80:
#     grade = "b"
# elif mark >= 70:
#     grade = "c"
# elif mark >= 60:
#     grade = "d"
# else:
#     grade = "f"

# print(grade)

# num = int(input("Enter a number:"))

# if num % 2== 0:
#     print("Even number")
# else:
#     print("odd number")

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))
# c = int(input("Enter third number:"))

# if(a>b and a>c):
#     print("first number is greater")
# elif(b>a and b>c):
#     print("second number is greater")
# else:
#     print("third number is greater")

# x = int(input("Enter first number:"))

# if(x % 7 ==0):
#     print("multiple of 7")
# else:
#     print("not multiple of 7")


#tuple 

# tup=(1,2,3,4)
# print(tup[0])

# list=("saiyara","tiger","dhrisham")
# print(list)

# movies = [] 
# mov1 = input("enter 1st movie")
# mov2 = input("enter 2nd movie")
# mov3 = input("enter 3rd movie")
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)


# list1 = [a, b, c, b, a]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if copy_list1 == list1:
#     print("palindrome")
# else:
#     print("not palindrome")


# grade = ("c", "c", "r", "s", "b", "a")
# print(grade.count("c"))

#dictionary






