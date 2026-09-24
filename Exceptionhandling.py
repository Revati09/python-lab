#1.try except
#handling division by  zero error
# try:
#     n = 0 
#     res = 100/n
# except ZeroDivisionError:
#     print("You can't divide by zero")
# print("program completed.")

#2.multiple exceptions
# try:
#     n = 0
#     res = 100 / n
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# except ValueError:
#     print("Enter a valid number!")

# else:
#     print("Result is", res)

# finally:
#     print("Execution complete.")

#3.try except else finally
# try:
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     result = a / b
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
#     print("Enter numbers only!")
# else:
#     print("Result =", result)
# finally:
#     print("Execution completed.")

# #4.user defined  exception
# class InvalidAgeException(Exception):
#     pass
# number = 18
# try:
#     input_num = int(input("Enter your age: "))

#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")

# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")

#5.user defined salary Exception
# class SalaryNotInRangeError(Exception):

#     def __init__(self, salary,
#                  message="Salary is not in (5000, 15000) range"):
#         self.salary = salary
#         self.message = message
#         super().__init__(self.message)


# salary = int(input("Enter salary amount: "))

# if not 5000 < salary < 15000:
#     raise SalaryNotInRangeError(salary)

# print("Salary is in valid range.")


#6.assert for consistency test
# x = 10
# assert x > 0, "x must be positive"
# print("Program continues...")

# # if the condition is false

# x = -10
# assert x > 0, "x must be positive"
# print("Program continues...")



