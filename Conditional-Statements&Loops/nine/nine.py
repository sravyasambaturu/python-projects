# Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 1 1 2 3 5 8 13 21 34

a = 1
b = 1
n = [1,1]

for i in range(0,7):
    i = a + b
    a = b 
    b = i
    n.append(i)
print(n)

#or

# n = [0,1]
# for i in range(0,10):
#     n.append(n[i]+n[i+1])
# print(n)


#or 

# x, y = 0, 1
# while y < 50:
#     print(y)
#     x, y = y, x + y
