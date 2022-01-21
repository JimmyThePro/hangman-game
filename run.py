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
            print(f'\nYay, you did it! [{word.upper()}] is correct.\n')
            return True


def game():
    guessed_letters = []
    fails = 0
    play = Hangman()

    # Learned ascii art here: https://www.messletters.com/
    print(' __| |_________________________________________________| |__')
    print('(__   _________________________________________________   __)')
    print('   | |                                                 | |')
    print('   | |               Lets play HANGMAN!                | |')
    print('   | |                 (Animal words)                  | |')
    print('   | |                                                 | |')
    print('   | |  Rules:   You have 6 fails until GAME OVER.     | |')
    print('   | |           Only guess with ONE letter.           | |')
    print('   | |           If you get the secret word            | |')
    print('   | |           correct, you win!                     | |')
    print('   | |                                                 | |')
    print('   | |                   GOOD LUCK!                    | |') 
    print(' __| |_________________________________________________| |__')
    print('(__   _________________________________________________   __)')
    print('   | |                                                 | |\n')

    user = input('Enter your Name please: ')
    print(f'Welcome {user}! Remember: The Secret Word is an ANIMAL - Go!')

    while True:
        play.view()
        guess = input('Guess a letter [a-z]: ').lower()
        if guess not in string.ascii_letters:
            print('Error! - You can only guess with one letter.')
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
                print('You lost... GAME OVER!\n')
                break
            continue
        if play.win_check():
            print('｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡')
            print('                 CONGRATZ!')
            print('｡☆✼★━━━━━━━━━━━━━━━━━━━━━━━━━━━━━★✼☆｡')
            print('\nGreat work! You won! :)\n')
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
            print('Error - Please enter "y" or "n" to continue\n')


game_loop()
