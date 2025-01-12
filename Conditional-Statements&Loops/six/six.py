# Write a Python program to count the number of even and odd numbers in a series of numbers
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4


input_numbers = input("enter the sample numbers: ")
seperated_numbers = input_numbers.split(",")
updated_numbers = [int(num.strip()) for num in seperated_numbers]
even_numbers = []
odd_numbers = []
for i in updated_numbers:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Number of even numbers: " + str(len(even_numbers)))
print("Number of odd numbers: " + str(len(odd_numbers)))
 
    
#or

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# count_odd = 0
# count_even = 0
# for x in numbers:
#     if not x % 2: 
#         count_even += 1
#     else:
#         count_odd += 1
# print("Number of even numbers:", count_even)
# print("Number of odd numbers:", count_odd) 


