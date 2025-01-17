# Write a Python program to find numbers between 100 and 400 (both included) 
# where each digit of a number is an even number. 
# The numbers obtained should be printed in a comma-separated sequence.

num = []

for number in range(99,401):
    if all(int(digit) % 2 == 0 for digit in str(number)):
        num.append(number)
print(",".join(map(str, num)))

#or

# # Create an empty list named 'items'
# items = []

# # Iterate through numbers from 100 to 400 (inclusive) using the range function
# for i in range(100, 401):
#     # Convert the current number 'i' to a string and store it in the variable 's'
#     s = str(i)
    
#     # Check if each digit in the current number 'i' is even (divisible by 2)
#     if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
#         # If all digits are even, append the string representation of 'i' to the 'items' list
#         items.append(s)

# # Join the elements in the 'items' list separated by ',' and print the result
# print(",".join(items)) 
