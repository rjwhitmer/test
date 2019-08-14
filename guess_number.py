import random
number=random.randrange(1, 101)
num_guess=0
num_trys=0
while number!=num_guess:
    num_guess=input("Guess a number between 1 and 100: ")
    num_guess=int(num_guess)
    num_trys+=1
    if num_guess > number:
        print("The number you guessed is too high. Guess again: ")
    elif num_guess < number:
        print("The number you guessed is too low. Guess again: ")
    elif num_guess == number:
        print("That's right!")
        print("You got it in", num_trys, "guesses! Well done!")
        break
