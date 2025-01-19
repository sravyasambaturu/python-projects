#  Write a Python program to print the alphabet pattern 'P'.
# Expected Output:

#  ****                                                                   
#  *   *                                                                  
#  *   *                                                                  
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  * 


result_str = ""
for row in range(0,7):
    for column in range(1,6):
        if (column == 1 or 
            ( row == 0 and column != 5) or
            (row == 3 and column !=5) 
            or (column == 5  and row == 1) or (column == 5  and row == 2)
            ):
            result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"
print(result_str)