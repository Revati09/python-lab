
import re

# Take password input from user
password = input("Enter Password: ")

# Password conditions:
# At least 8 characters
# At least one uppercase letter
# At least one lowercase letter
# At least one digit
# At least one special character

pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}$"

# Check password
if re.match(pattern, password):
    print("Valid Password!")
else:
    print("Invalid Password!")


