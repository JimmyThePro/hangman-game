import random
from secret_words import secret_words


class Hangman:
    """
    Main class.
    Has methods for displaying secret words,
    hangman pictures (selfdrawn, terminal friendly) and guesses.
    """

    def __init__(self):
        self.word = random.choice(secret_words)
        # Show underscore instead of the word for the user
        self.display = ['_' for letter in self.word]

    # Print display to terminal
    def view(self):
        display = ' '.join(self.display).upper()
        print(f'\nSecret word (an animal): {display}')

    # Index/char value in secret words
    def get_letter_in_word(self, guess_letter):
        positions = []
        # Learned code here: https://realpython.com/python-enumerate/
        for index, char in enumerate(list(self.word)):
            if char == guess_letter:
                positions.append(index)
        return positions

    # Check if our guessed letter is in the secret word
    def guess_check(self, guess_letter):
        if guess_letter in self.word:
            index_value = self.get_letter_in_word(guess_letter)
            self.display_update(index_value, guess_letter)

    # Update display method
    def display_update(self, index_value, letter):
        for number in index_value:
            self.display[number] = letter

    # Check if user win
    def win_check(self):
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print('\nYay, you did it!')
            return True


def game():
    play = Hangman()
    print("\nLet's play Hangman! Good luck! :)")
    while True:
        play.view()
        guess = input('Guess a letter [a-z]: ').lower()
        play.guess_check(guess)
        if play.win_check():
            print('Great work! :)\n')
            break


game()


def game_loop():
    while True:
        response = input('Wanna play again? [y/n]: ').lower()
        if response == 'n':
            break
        elif response == 'y':
            game()
        else:
            print('Invalid key - Please enter "y" or "n" to continue')


game_loop()
