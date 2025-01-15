# Write a Python program that accepts a sequence of comma separated
# 4 digit binary numbers as its input.
# The program will print the numbers that are divisible by 5 
# in a comma separated sequence.
# Sample Data : 0100,0011,1010,1001,1100,1001
# Expected Output : 1010 

# input_values = input("Enter a sequence of 4-digit binary numbers, separated by commas: ")
# binary_numbers = input_values.split(",")  
# divisible_by_5 = []

# for binary in binary_numbers:
#     binary = binary.strip()  
#     if len(binary) == 4 and all(ch in "01" for ch in binary):  
#         decimal_value = int(binary, 2)  
#         if decimal_value % 5 == 0:  
#             divisible_by_5.append(binary)
#     else:
#         print(f"Invalid binary number skipped: {binary}")

# if divisible_by_5:
#     print("Binary numbers divisible by 5:", ",".join(divisible_by_5))
# else:
#     print("No binary numbers divisible by 5 were found.")

#or

# items = []
# num = [x for x in input().split(',')]

# for p in num:
#     x = int(p, 2)

#     if not x % 5:
#         items.append(p)

# print(','.join(items))
