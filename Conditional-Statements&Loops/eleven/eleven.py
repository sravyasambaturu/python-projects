# Write a Python program that takes two digits m (row) and n (column) 
# as input and generates a two-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note :
# i = 0,1.., m-1
# j = 0,1, n-1.

# Test Data : Rows = 3, Columns = 4
# Expected Result : [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]]

row_value = input("Number of rows: ")
column_value = input("Number of columns: ")
result = []
m = int(row_value)
n = int(column_value)
for i in range(0,m):
    rows = []
    for j in range(0,n):
      rows.append(i*j)
    result.append(rows)
print(result)

#or

# # Prompt the user to input the number of rows
# row_num = int(input("Input number of rows: "))

# # Prompt the user to input the number of columns
# col_num = int(input("Input number of columns: "))

# # Create a 2D list (a list of lists) filled with zeros using list comprehension
# # The outer list will have 'row_num' elements and the inner lists will have 'col_num' elements
# multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# # Nested loop to populate the 2D list with multiplication results
# for row in range(row_num):
#     for col in range(col_num):
#         # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
#         multi_list[row][col] = row * col

# # Print the resulting 2D list containing the multiplication table
# print(multi_list) 
