import random

guessnum = random.randint(1, 20)
print("""Welcome to the Guessing Game!
The number is between 1 and 20.
How many tries will it take you to guess it?""")
counter = 1
    
while True:
    guess = int(input("""Guess?
"""))
    if guess == guessnum:
        print("You got it! It took you " + str(counter) + " tries to guess the number. Yay you!")
        endq = input("""Wanna play again?
""")
        if "y" in endq:
            guessnum = random.randint(1,20)
            counter = 1
            continue
        else:
            break
    elif guess > guessnum:
        print("Your guess was bigger than the number.")
        counter += 1
        continue
    elif guess < guessnum:
        print("Your guess was smaller than the number.")
        counter += 1
        continue
        
    
