# Write a Python program to print the following patterns.
# Expected Output:

#   ****                                                                  
#  *                                                                      
#  *                                                                      
#   ***                                                                   
#      *                                                                  
#      *                                                                  
#  **** 

# result_str = ""
# for row in range(0,7):
#     for column in range(1,6):
#         if ( (column == 1 and row != 0 and row != 3 and row != 4 and row != 5) or
#             (row == 6 and column != 5) or
#             (row == 0 and column != 1) or 
#             (row == 3 and column != 1 and column != 5) or
#             (column == 5 and row == 4) or 
#             (column == 5 and row == 5)):
#             result_str = result_str + "*"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)


# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# oooo                                                                    
# oooo                                                                    
# oooo                                                                    
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
#              oooo                                                       
#              oooo                                                       
#              oooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo                                                       
# ooooooooooooooooo


# result_str = ""
# for row in range(0,16):
#     for column in range(1,18):
#         if ( row == 0 or row == 1 or row == 2 or row == 6 or row == 7 or row ==8 or row == 12 or row == 13 or row == 14 
#              or ((row >2 and row < 6 and (column < 5))) or
#              ((row > 8 and row < 12 and (column > 13))) ):
#             result_str = result_str + "o"
#         else:
#             result_str = result_str + " "
#     result_str = result_str + "\n"
# print(result_str)

result_str = ""
for row in range(0,16):
    for column in range(1,18):
        if ( ((row <= 2) or (row >= 6 and row <= 8) or (row >= 12 and row <= 14)) 
             or ((row >2 and row < 6 and (column < 5))) or
             ((row > 8 and row < 12 and (column > 13))) ):
            result_str = result_str + "o"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)




# # Define variables 'row' and 'col' with values 15 and 18 respectively
# row = 15    
# col = 18   
# result_str = ""  # Reinitialize the 'result_str' to an empty string

# # Loop through values from 1 to 'row' using the range function
# for i in range(1, row+1):
#     # Check conditions to determine the pattern for each row
    
#     # If conditions are met, append 'o' to the 'result_str' in specific positions
#     if ((i <= 3) or (i >= 7 and i <= 9) or (i >= 13 and i <= 15)):
#         for j in range(1, col):
#             result_str = result_str + "o"  # Append 'o' to the 'result_str'
#         result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'
#     elif (i >= 4 and i <= 6):
#         for j in range(1, 5):
#             result_str = result_str + "o"  # Append 'o' to the 'result_str'
#         result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'
#     else:
#         for j in range(1, 14):
#             result_str = result_str + " "  # Append space (' ') to the 'result_str'
#         for j in range(1, 5):
#             result_str = result_str + "o"  # Append 'o' to the 'result_str'
#         result_str = result_str + "\n"  # Add a newline character after each row in 'result_str'

# # Print the final 'result_str' containing the pattern for the second shape
# print(result_str)
