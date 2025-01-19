# Write a Python program to print the alphabet pattern 'M'.
# Expected Output:

#   *       *                                                             
#   *       *                                                             
#   * *   * *                                                             
#   *   *   *                                                             
#   *       *                                                             
#   *       *                                                             
#   *       *

result_str = ""
for row in range(0,7):
    for column in range(0,9):
        if (column == 0 or ( column == 8 and (column != 2 or column != 3 or column != 4 or column != 5 or column != 6 or column != 7))
           or  (row == 2 and column != 1 and column != 3 and column != 4 and column !=5 and column !=7 )
           or ( row == 3 and column !=1 and column !=2 and column !=3 and column !=5 and column !=6 and column !=7 and column !=8)):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)

# # Initialize an empty string named 'result_str'
# result_str = ""

# # Iterate through rows from 0 to 6 using the range function
# for row in range(0, 7):
#     # Iterate through columns from 0 to 6 using the range function
#     for column in range(0, 7):
#         # Check conditions to determine whether to place '*' or ' ' in the result string
        
#         # If conditions are met, place '*' in specific positions based on row and column values
#         if (column == 1 or column == 5 or (row == 2 and (column == 2 or column == 4)) or (row == 3 and column == 3)):
#             result_str = result_str + "* "  # Append '*' followed by a space (' ') to the 'result_str'
#         else:
#             result_str = result_str + "  "  # Append two spaces ('  ') to the 'result_str'

#     result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'

# # Print the final 'result_str' containing the pattern
# print(result_str)
