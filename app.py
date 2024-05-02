import random

from game_art import stages, logo
from words import word_list

display = []


def insert_blanks():
    for index in range(len(chosen_word)):
        display.insert(index, '_')


def lose_life(index):
    print(stages[index])


def guess():
    lives = 7
    guesses = []
    while lives > 0 and '_' in display:
        guess_letter = input('Guess a letter in the mystery word:   ').lower()
        if guess_letter in guesses:
            print(f'You have already guessed: {guess_letter}')
        else:
            if guess_letter in chosen_word:
                for index in range(len(chosen_word)):
                    if chosen_word[index] == guess_letter and display[index] != guess_letter:
                        display[index] = guess_letter
                        guesses.append(guess_letter)
                        print(display)
            else:
                lose_life(lives-1)
                lives -= 1

        if '_' not in display:
            print('You win! =D')

        if lives == 0:
            print("You lose. :'(")
            print(f"Mystery Word: {chosen_word}")


print(logo)
chosen_word = random.choice(word_list)
#aprint(f'Psst, the solution is {chosen_word}')
insert_blanks()
guess()
