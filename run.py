import random

class Hangman:
    """
    Main class.
    Has methods for displaying secret words,
    hangman pictures (selfdrawn, terminal friendly) and guesses.
    """

    def __init__(self):
        self.word = random.choice()
        # show underscore instead of the word for the user
        self.display = ['_' for letter in self.word]
        self.guesses = 0

    # print display to terminal
    def view(self):
        display = ' '.join(self, display)
        print(f'Secret word (an animal): {display}')

    # index/char value in secret words
    def get_letter_in_word(self, guess_letter):
        positions = []
        # learned code here: https://realpython.com/python-enumerate/
        for index, char in enumerate(self.word):
            if char == guess_letter:
                positions.append(index)
        return positions

    # check if our guessed letter is in the secret word
    def guess_check(self, guess_letter):
        if guess_letter in self.word:
            index_value = self.get_letter_in_word(guess_letter)

    # need update display
    def display_update():



game()
