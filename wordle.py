import random
import sys 
from termcolor import colored
import nltk
from nltk.corpus import words


def print_menu():
    print("let's play wordle: ")
    print("type a 5 letter word and hit enter!\n")


def nltk_random_word():
    pass

def read_random_word():
    with open("words.txt") as f:
        words = f.read().splitlines()
        return random.choice(words).upper()

nltk.data.path.append('/work/words')
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu()


play_again = ''
while play_again != 'q':

    word = read_random_word()
    #print(word)


    for attempt in range(1,7):
        guess = input('\n').upper()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess),5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end='')
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end='')
            else:
                print(guess[i], end='')

        if guess == word:
            print(colored(f'\nCongrats!! you got the wordle in {attempt}','red'))
            break
    play_again = input('want to play again? type q to exit.')