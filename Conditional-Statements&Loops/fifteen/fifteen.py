# Write a Python program to check the validity of passwords input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.


user_input = str(input("Enter the password: "))

if 6 < len(user_input) < 12:
    if any(ch.isalpha() for ch in user_input):
        if any(ch.upper() for ch in user_input):
            if any(ch.isdigit() for ch in user_input):
                if any(ch in "$#@" for ch in user_input):
                    print("Your Password is validated!")
                else:
                    print("Password must contain at least one special character ($, #, @).")
            else:
                print("Password must contain at least one digit.")
        else:
            print("Password must contain at least one uppercase letter.")
    else:
        print("Password must contain at least one alphabetic character.")
else:
    print("Password length must be between 7 and 12 characters.")


#or

# # Import the 're' module for regular expressions
# import re

# # Prompt the user to input a password and store it in the variable 'p'
# p = input("Input your password")

# # Set 'x' to True to enter the while loop
# x = True

# # Start a while loop that continues until 'x' is True
# while x:  
#     # Check conditions for a valid password:
#     # Password length should be between 6 and 12 characters
#     if (len(p) < 6 or len(p) > 12):
#         break
#     # Password should contain at least one lowercase letter
#     elif not re.search("[a-z]", p):
#         break
#     # Password should contain at least one digit
#     elif not re.search("[0-9]", p):
#         break
#     # Password should contain at least one uppercase letter
#     elif not re.search("[A-Z]", p):
#         break
#     # Password should contain at least one special character among '$', '#', '@'
#     elif not re.search("[$#@]", p):
#         break
#     # Password should not contain any whitespace character
#     elif re.search("\s", p):
#         break
#     else:
#         # If all conditions are met, print "Valid Password" and set 'x' to False to exit the loop
#         print("Valid Password")
#         x = False
#         break

# # If 'x' remains True, print "Not a Valid Password"
# if x:
#     print("Not a Valid Password")

