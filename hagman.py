import random

# List of secret words
secret_words = ["apple", "banana", "cherry", "grape", "kiwi"]

# Select a random word from the list
secret_word = random.choice(secret_words)

# Initialize a list to store correct guesses
correct_guesses = []

# Function to check if the guess is in the word
def check_guess(guess):
    # Convert the guess into lowercase
    guess = guess.lower()

    # Check if the guess is in the secret word
    if guess in secret_word:
        # If the guess is correct, add it to the list of correct guesses
        correct_guesses.append(guess)
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Function to ask for user input and check guesses
def ask_for_input():
    # Create a while loop to continuously ask the user for a letter
    while True:
        # Ask the user to guess a letter and assign it to the variable guess
        guess = input("Guess a letter: ")

        # Check if the input is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # Call the check_guess function to check if the guess is in the word
            check_guess(guess)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

        # Check if all letters in the secret word have been guessed
        if all(letter in correct_guesses for letter in secret_word):
            print(f"Congratulations! You guessed the word '{secret_word}' correctly.")
            break  # Exit the loop if all letters have been guessed

# Call the ask_for_input function to start the game
ask_for_input()
