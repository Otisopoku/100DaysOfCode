# Hundred days of code Hangman
import random
lives = 6; 
guess_word = ['_' for i in range(lives)]
right_guess = False


list_of_words = ["amanda", "colder", "coming", "exempt"]
word_to_guess = random.choice(list_of_words)

while lives > 0:
    print(f'************************ {lives}/6 LIVES LEFT ***************************')
    print(f'Word to guess: {"".join(guess_word)}')
    input_letter = input("Guess a letter: ")
    for i in range(len(word_to_guess)):
        if word_to_guess[i] == input_letter:
            right_guess = True
            guess_word[i] = input_letter

    if ("".join(guess_word) == word_to_guess):
        break
    if not right_guess:
        print(f'You guessed {input_letter}, that\'s not in the word. You lose a life\n')
        lives -= 1
    else:
        print("".join(guess_word) + "\n")
        right_guess = False

if lives <= 0:
    print(f'**************** IT WAS {word_to_guess}! YOU LOSE **************************')
else:
    print(f'**************** IT WAS {word_to_guess}! YOU WON **************************')


'''
ChatGPT Implementation

# Hundred days of code Hangman
import random

# Game setup
lives = 6
words = ["amanda", "colder", "coming", "exempt"]
word_to_guess = random.choice(words)
guess_word = ["_"] * len(word_to_guess)

while lives > 0:
    print(f'\n************* {lives}/6 LIVES LEFT *************')
    print(f'Word to guess: {" ".join(guess_word)}')

    input_letter = input("Guess a letter: ").strip().lower()

    if input_letter in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == input_letter:
                guess_word[i] = input_letter
    else:
        print(f'You guessed "{input_letter}", that\'s not in the word. You lose a life.\n')
        lives -= 1

    # Check if player won
    if "".join(guess_word) == word_to_guess:
        print(f'\n🎉 YOU WON! The word was "{word_to_guess}".')
        break
else:
    print(f'\n💀 YOU LOST! The word was "{word_to_guess}".')


'''