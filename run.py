import random
import string

from secret_words import secret_words
from hangman_pictures import hangman_stages


class Hangman:
    """
    Main class.
    Has methods for displaying secret words,
    hangman pictures (selfdrawn, terminal friendly) and guesses.
    """

    def __init__(self):
        """
        Pick a random word in secret_words and
        show underscore instead of the word for the user.
        """
        self.word = random.choice(secret_words)
        # Show underscore instead of the word for the user
        self.display = ['_' for letter in self.word]

    def view(self):
        """
        Print display to terminal.
        """
        display = ' '.join(self.display).upper()
        print(f'\nSecret word (an animal): {display}')

    def get_letter_in_word(self, guess_letter):
        """
        Index/char value in secret words.
        """
        positions = []
        # Learned code here: https://realpython.com/python-enumerate/
        for index, char in enumerate(list(self.word)):
            if char == guess_letter:
                positions.append(index)
        return positions

    def guess_check(self, guess_letter):
        """
        Check if guessed letter is in the secret word.
        """
        if guess_letter in self.word:
            index_value = self.get_letter_in_word(guess_letter)
            self.display_update(index_value, guess_letter)

    def display_update(self, index_value, letter):
        """
        'Update display' method.
        """
        for number in index_value:
            self.display[number] = letter

    def win_check(self):
        """
        Check if user wins.
        """
        display = ''.join(self.display)
        word = self.word
        if display == word:
            print(f'\nYay, you did it! [{word.upper()}] is correct.\n')
            return True


def game():
    """
    Function that open up a new game, and user can enter a name,
    and start guessing letters, until he/she win or lose.
    """
    guessed_letters = []
    fails = 0
    play = Hangman()

    # Learned ascii art here: https://www.messletters.com/
    print('\n __| |_________________________________________________| |__')
    print('(__   _________________________________________________   __)')
    print('   | |                                                 | |')
    print("   | |               Let's play HANGMAN!               | |")
    print('   | |                 (Animal words)                  | |')
    print('   | |                                                 | |')
    print('   | |   Rules:  You have 6 fails until GAME OVER.     | |')
    print('   | |           Only guess with ONE letter.           | |')
    print('   | |           If you get the secret word            | |')
    print('   | |           correct, you win!                     | |')
    print('   | |                                                 | |')
    print('   | |                   GOOD LUCK!                    | |')
    print(' __| |_________________________________________________| |__')
    print('(__   _________________________________________________   __)')
    print('   | |                                                 | |\n')

    user = input('Enter your Name please: ')
    while len(user) == 0:
        user = input('Error! - You need to enter your Name: ')
        if len(user) >= 1:
            break

    print(f"Welcome {user}! Let's play!")
    while True:
        play.view()
        guess = input('Guess a letter [a-z]: ').lower()
        # Learned code here: https://tinyurl.com/5n88vmfa
        if guess not in string.ascii_letters:
            print('\nError! - You can only guess with one letter.')
            continue
        if len(guess) == 0:
            print('\nError! - You need to enter a letter')
            continue
        play.guess_check(guess)
        if guess in guessed_letters:
            print(f'You already guessed "{guess.upper()}", try again...')
            continue
        for i, char in enumerate(play.word):
            if guess == char:
                print(f'\n★ Great! "{char.upper()}" is in ★')
                guessed_letters.append(guess)
                break
        if guess != char:
            print(f'\nOoops! "{guess.upper()}" is not in...')
            guessed_letters.append(guess)
            print(hangman_stages[fails])
            fails += 1
            if fails == 6:
                print(f'[{play.word.upper()}] was the Secret word.\n')
                print(f'Sorry {user}, you lost... GAME OVER!\n')
                break
            continue
        if play.win_check():
            print('｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡')
            print('                WINNER!')
            print('｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡')
            print(f'\nGreat work {user}! You won! :)\n')
            break


game()


def game_loop():
    """
    Function loop after a user win or lose a game,
    Y or N to input if user want to start a new game or not.
    """
    while True:
        response = input('Start a new game? [y/n]: ').lower()
        if response == 'n':
            print('Closing game...\n')
            break
        elif response == 'y':
            game()
        else:
            print('Error! - Please enter "y" or "n" to continue\n')


game_loop()
