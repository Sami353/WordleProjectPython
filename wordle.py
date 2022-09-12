import random
import rich
from fivewords import words
from rich.prompt import Prompt
from rich.console import Console


def get_words(word):
    word = random.choice(word)
    while len(word) != 5:
        word = random.choice(word)
    return word.upper()


def correct_position(letter):
    return f'[white on green]{letter}[/]'


def correct_letter(letter):
    return f'[white on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[white on black]{letter}[/]'


def score(guess, answer):
    score = []
    for index, letter in enumerate(guess):
        if answer[index] == guess[index]:
            score += correct_position(letter)
        elif letter in answer:
            score += correct_letter(letter)
        else:
            score += incorrect_letter(letter)
    return ''.join(score)


def check_word(word):
    if len(word) != 5:
        return True
    else:
        return False


def verify_word(word, list):
    if word.lower() not in list:
        return True
    else:
        return False


def main():
    rich.print(correct_position('WELCOME') + " " + correct_letter('TO') + " " + incorrect_letter('WORDLE') + "")

    guesses = 6

    console = Console()
    actual_answer = get_words(words)

    while guesses != 0:
        guesses -= 1
        player_input = Prompt.ask('Enter a Word').upper()

        while check_word(player_input):
            console.print('This word is not valid. Please enter a valid word.')
            player_input = Prompt.ask('Enter a valid word').upper()

        while verify_word(player_input, words):
            console.print('This word is not valid. Please enter a valid word.')
            player_input = Prompt.ask('Enter a valid word').upper()

        console.print(score(player_input, actual_answer) + "")
        if player_input == actual_answer:
            console.print('CONGRATS! You guessed the word.')
            break

    if guesses == 0 and player_input != actual_answer:
        console.print('WRONG GUESS! The correct word is ' + correct_position(actual_answer))

if __name__ == '__main__':
    main()