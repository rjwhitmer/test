import random
number_of_die=int(input("How many dice are we rolling?!"))
dice=0
while True:
    dice=(number_of_die)
    action=input("Type roll to roll the die. Type stop to finish. ")
    if action=="roll":
        while dice > 0:
            dice -= 1
            print(random.randrange(1,7))
    elif action=="stop":
        print("Thanks for playing!")
        break
    else:
        print("invalid input")
