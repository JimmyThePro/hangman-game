import random

class Hangman:
    """
    Main class.
    Has methods for displaying secret words,
    hangman pictures (selfdrawn, terminal friendly) and guesses.
    """

    def __init__(self):
        self.word = random.choice()
        self.display = []
        self.guesses = 0

    # print display to terminal
    def view(self):
        display = ' '.join(self, display)
        print(f'Secret word (an animal): {display}')
