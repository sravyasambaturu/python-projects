# Write a Python program that accepts a sequence of lines (blank line to terminate) as input 
# and prints the lines as output (all characters in lower case).

lines = []
while True:
    user_input = input()
    if not user_input:  
        break
    lines.append(user_input)
my_string = "\n".join(lines) 
print(my_string.lower())


