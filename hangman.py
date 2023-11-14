import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word, self.word_guessed, self.num_letters = self.initialize_game()

    def initialize_game(self):
        word = random.choice(self.word_list)
        word_guessed = ['_' for _ in word]
        num_letters = len(set(word))
        return word, word_guessed, num_letters

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            self.update_word_guessed(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            self.reduce_lives()
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def update_word_guessed(self, guess):
        for i, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[i] = guess
        self.num_letters -= 1

    def reduce_lives(self):
        self.num_lives -= 1

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

                if self.num_letters == 0:
                    print(f"Congratulations! You guessed the word '{self.word}' correctly.")
                    break
                elif self.num_lives == 0:
                    print(f"Game over! The word was '{self.word}'. Better luck next time.")
                    break

if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "grape", "kiwi"]
    game = Hangman(words)
    game.ask_for_input()
