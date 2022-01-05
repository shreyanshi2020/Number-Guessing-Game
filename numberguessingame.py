import random
number = random.randint(1,9)
chance = 0
while chance>5:
    guess = int(input())
    if guess== number:
        print("Congrats")
    elif guess>number:
        print("Your Guess is less.")
    else:
        print("Your guess is More.") 
    chance = chance+1
