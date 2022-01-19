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

    # check if the letter is in the secret word
    def get_letter_in_word(self, guess_letter):
        positions = []
        # learned code here: https://realpython.com/python-enumerate/
        for index, char in enumerate(self.word):
            if char == guess_letter:
                positions.append(index)
        return positions



game()
