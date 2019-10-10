import random


def get_word():
    with open ("words.txt") as my_file:
        my_file = my_file.readlines()

        stripped_words = []
        for word in my_file:
            word = word.strip('\n')
        
            stripped_words.append(word)

        word_to_guess = random.choice(stripped_words)

        return word_to_guess


def display_letters(word_to_guess, letters_guessed, word_display):
    for letter in word_to_guess:
            # print(letter)
            if letter in letters_guessed:
                word_display.append(letter)
            else:
                word_display.append('_')
    return word_display
                

def evaluate_guess(guess_letter, letters_guessed, word_to_guess, word_display):
    decrement_guesses = False
    if len(guess_letter) != 1:
        print('Must be one letter')
    elif not guess_letter.isalpha():
        print('Must be a letter')
    elif guess_letter in letters_guessed:
        print('You already guessed that') 
    else:
        letters_guessed.append(guess_letter)
        word_display = display_letters(word_to_guess, letters_guessed, word_display)
        if guess_letter not in word_display:
            decrement_guesses = True
        return decrement_guesses

    
def play_game():
    word_to_guess = get_word()
    print('Welcome to Mystery Word!\n')
    print("Letters in word: " + str(len(word_to_guess)))
    guesses_left = 8
    letters_guessed = []
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left")
        guess_letter = input("Guess a letter: ")
        # print(word_to_guess)
        word_display = []
        print(letters_guessed)
        
        decrement_guesses = evaluate_guess(guess_letter, letters_guessed, word_to_guess, word_display) 
        print(' '.join(word_display))
        # print(word_to_guess, word_display)
        if list(word_to_guess) == word_display:
            print('You Win!')
            break
        if decrement_guesses:
            guesses_left -= 1
        if guesses_left == 0:     
            print('Sorry, you ran out of guesses. You lose.')
        

        




    print(f"The word was {word_to_guess}")


play_game()