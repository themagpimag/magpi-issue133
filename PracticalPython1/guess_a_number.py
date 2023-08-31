# Import the 'random' module to generate random numbers
import random

# Generate a random number between 1 and 100 and store it in 'target_number'
target_number = random.randint(1, 100)

# Initialize 'guess' to None and 'attempts' to 0
guess = None
attempts = 0

# Start a loop that continues until the player's guess matches the target number
while guess != target_number:
    # Get the player's guess as an integer input
    guess = int(input("Guess a number between 1 and 100: "))
    
    # Increment the 'attempts' counter by 1
    attempts += 1
    
    # Check if the guess is too low
    if guess < target_number:
        print("Too low!")
    # Check if the guess is too high
    elif guess > target_number:
        print("Too high!")

# When the loop ends (player guessed correctly), print a congratulations message
# and show the target number and the number of attempts it took
print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
