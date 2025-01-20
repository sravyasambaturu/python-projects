#  Write a Python program to print the alphabet pattern 'R'.
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  * *                                                                    
#  *  *                                                                   
#  *   *


# result_str = ""
# for row in range(0,7):
#     for column in range(1,6):
#         if (column == 1 or 
#             ( row == 0 and column != 5) or
#             (row == 3 and column !=5) 
#             or (column == 5  and row == 1) or (column == 5  and row == 2)
#             or (column == 3 and row == 4)
#             or (column == 4 and row == 5)
#             or (column == 5 and row == 6)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)



result_str = ""
for row in range(0,7):
    for column in range(1,6):
        if (column == 1 or 
            ( row == 0 and column != 5) or
            (row == 3 and column !=5) 
            or (column == 5  and row == 1) or (column == 5  and row == 2)
            or (column >1 and row == column +1 and row > 3 and row < 7)
            ):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)


# # Initialize an empty string named 'result_str'
# result_str = ""

# # Loop through rows from 0 to 6 using the range function
# for row in range(0, 7):
#     # Loop through columns from 0 to 6 using the range function
#     for column in range(0, 7):
#         # Check conditions to determine whether to place '*' or ' ' in the result string
        
#         # If conditions are met, place '*' in specific positions based on row and column values
#         if (((row == 0 or row == 3 or row == 6) and column > 1 and column < 5) or 
#             (column == 1 and (row == 1 or row == 2 or row == 6)) or 
#             (column == 5 and (row == 0 or row == 4 or row == 5))):
#             result_str = result_str + "*"  # Append '*' to the 'result_str'
#         else:
#             result_str = result_str + " "  # Append space (' ') to the 'result_str'

#     result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'

# # Print the final 'result_str' containing the pattern for the first shape
# print(result_str)