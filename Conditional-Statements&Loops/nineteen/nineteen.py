# Write a Python program to print the alphabet pattern 'E'.
# Expected Output:

#  *****                                                                  
#  *                                                                      
#  *                                                                      
#  ****                                                                   
#  *                                                                      
#  *                                                                      
#  *****


result_str = ""

for row in range(0,7):
    for column in range(1,6):
        if (column == 1) or ((row == 0 or row ==3 or row ==6)):
        #if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):
           result_str = result_str + "*"
        else:
            result_str = result_str + " "
    result_str = result_str + "\n"  
print(result_str) 

            