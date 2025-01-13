# <!-- Write a Python program that iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". 
# For numbers that are multiples of three and five, print "FizzBuzz". -->

n = []
for i in range(1,51):
    if (i%3==0 and i%5==0):
        n.append("FizzBuzz")
    elif i%5==0:
        n.append("Buzz")
    elif i%3==0:
        n.append("Fizz")
    else:
        n.append(i)
result = "\n".join(map(str, n))
print(result)

#or

# # Iterate through numbers from 0 to 50 using the range function
# for fizzbuzz in range(51):
#     # Check if the current number is divisible by both 3 and 5 (i.e., divisible by 15)
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         # If divisible by both 3 and 5, print "fizzbuzz" and continue to the next iteration
#         print("fizzbuzz")
#         continue
#     # Check if the current number is divisible only by 3
#     elif fizzbuzz % 3 == 0:
#         # If divisible only by 3, print "fizz" and continue to the next iteration
#         print("fizz")
#         continue
#     # Check if the current number is divisible only by 5
#     elif fizzbuzz % 5 == 0:
#         # If divisible only by 5, print "buzz" and continue to the next iteration
#         print("buzz")
#         continue
#     # If the number is neither divisible by 3 nor 5, print the number itself
#     print(fizzbuzz) 

#or

# def fizz_buzz(start, end):
#     """
#     Print 'Fizz', 'Buzz', or 'FizzBuzz' for numbers in the specified range based on divisibility rules.
    
#     Parameters:
#     start (int): The starting number of the range.
#     end (int): The ending number of the range.
#     """
#     if start > end:
#         print("Start should be less than or equal to end.")
#         return

#     for fizzbuzz in range(start, end + 1):
#         if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#             print("FizzBuzz")
#         elif fizzbuzz % 3 == 0:
#             print("Fizz")
#         elif fizzbuzz % 5 == 0:
#             print("Buzz")
#         else:
#             print(fizzbuzz)

# # Example usage
# print("From 1 to 10")
# fizz_buzz(1, 10)
# print("\nFrom 50 to 75")
# fizz_buzz(50, 75)
