#  Create a list containing the names of your 5 favorite fruits.
favorite_fruits = ["apple", "banana", "cherry", "grape", "kiwi"]

# Assign this list to a variable called word_list.
word_list = favorite_fruits

#  Print out the newly created list to the standard output (screen).
print("List of favorite fruits:", word_list)
import random  # To import a module, you have to use the import keyword at the top of the file.


# Create the random.choice method and pass the word_list variable into the choice method.
word = random.choice(word_list)
#  Assign the randomly generated word to a variable called word.

#  Print out word to the standard output.
print("Randomly selected word:", word)

# Ask the user to enter a single letter
guess = input("Please enter a single letter: ")

#  Assign the input to a variable called guess
print("You entered:", guess)

#  Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
guess = input("Please enter a single letter: ")

if len(guess) == 1 and guess.isalpha():
    #  In the body of the if statement, print a message that says "Good guess!"
    print("Good guess!")
else:
    #  Create an else block that prints "Oops! That is not a valid input."
    print("Oops! That is not a valid input.")
