import re
# Take input from user
email = input("Enter Email ID: ")
password = input("Enter Password: ")

# Regular expression for Gmail validation
pattern = r"^[A-Za-z0-9._%+-]+@gmail\.com$"

# Check email and password
if re.match(pattern, email):
    if password != "":
        print("Login Successful!")
    else:
        print("Password cannot be empty!")
else:
    print("Invalid Gmail ID!")