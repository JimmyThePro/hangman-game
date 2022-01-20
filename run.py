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
        # show underscore instead of the word for the user
        self.display = ['_' for letter in self.word]

    # print display to terminal
    def view(self):
        display = ' '.join(self.display)
        print(f'\nSecret word (an animal): {display}')

    # index/char value in secret words
    def get_letter_in_word(self, guess_letter):
        positions = []
        # learned code here: https://realpython.com/python-enumerate/
        for index, char in enumerate(list(self.word)):
            if char == guess_letter:
                positions.append(index)
        return positions

    # check if our guessed letter is in the secret word
    def guess_check(self, guess_letter):
        if guess_letter in self.word:
            index_value = self.get_letter_in_word(guess_letter)
            self.display_update(index_value, guess_letter)

    # update display method
    def display_update(self, index_value, letter):
        for number in index_value:
            self.display[number] = letter

    # check if user win
    def win_check(self):
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print('Yay! You win!!')
            return True


def game():
    play = Hangman()
    print("\nLet's play Hangman! Good luck! :)")
    while True:
        play.view()
        guess = input('Guess a letter (a-z): ')
        play.guess_check(guess)
        if play.win_check():
            print('U won!')
            break


game()


def game_loop():
    while True:
        response = input('Wanna play again? (Y/N): ')
        if response == 'n':
            break
        elif response == 'y':
            game()
        else:
            print('Invalid key - Please enter "Y" or "N" to continue')


game_loop()
