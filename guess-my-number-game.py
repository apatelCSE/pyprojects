import random
    
guessnum = random.randint(1, 20)
print("""Welcome to the Guessing Game!
The number is between 1 and 20.
How many tries will it take you to guess it?""")

while True:
    guess = int(input("""Guess?
"""))
    if guess == guessnum:
        print("You got it! Yay you!")
        endq = input("Wanna play again?")
        if "y" in endq:
            continue
        else:
            break
    elif guess > guessnum:
        print("Your guess was bigger than the number.")
        continue
    elif guess < guessnum:
        print("Your guess was smaller than the number.")
        continue
        
    

