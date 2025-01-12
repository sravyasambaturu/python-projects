#Guess a number between 1 to 9
import random

target_number, guess_number = random.randint(1, 9), 0

while target_number != guess_number :
    guess_number = int(input("Enter a number between 1 to 10 until your guess is right!: "))

print("Well Guessed!")

