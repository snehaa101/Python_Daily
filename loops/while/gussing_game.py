# --------------------------------------------------------------
# Topic: PYTHON LOOPS (while loop)
# Problem: Create a guessing game where the user has to guess a number between 1 and 50.
# The program should give hints whether the guess is too low, too high, or correct.
# -------------------------------------------------------------

# importing the random module to generate a random number
import random

secret = random.randint(1, 50)

# initializing the variable to store the guessed of the number
guess = 0
print(
    """WELCOME~~
        The number guessing game here you have gusses a number between 1-50"""
)

while guess != secret:
    guess = int(input("Enter your another guess : "))
    if guess > secret:
        print(
            """oo sorry you guesses wrong
        (Hint : The number you guesses is TOO HIGH to the correct secret number.)"""
        )
    elif guess < secret:
        print(
            """oo sorry you guesses wrong
        (Hint : The number you guesses is TOO LOW to the correct secret number.)"""
        )
print("HURRAY...CONGRATULATIONS YOU HAVE GUESSED THE NUMBER CORRECT.")
