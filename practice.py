import random



with open ("words.txt") as my_file:
    my_file = my_file.readlines()

    stripped_words = []
    for word in my_file:
        word = word.strip('\n')
    
        stripped_words.append(word)

    word_to_guess = random.choice(stripped_words)

# print(f'The word to guess is {word_to_guess}')
# print(word_to_guess[1])
# print(len(word_to_guess))


guesses_left = 8
letters_guessed = []

print("Letters in word: " + str(len(word_to_guess)))

    

while guesses_left > 0:
    print(f"You have {guesses_left} guesses left")
    guess_letter = input("Guess a letter: ")
    word_display = []
    print(letters_guessed)

    if len(guess_letter) != 1:
        print('Must be one letter')
    elif not guess_letter.isalpha():
        print('Must be a letter')
    elif guess_letter in letters_guessed:
        print('You already guessed that') 
    else:
        letters_guessed.append(guess_letter)
        for letter in word_to_guess:
            # print(letter)
                 
            if letter in letters_guessed:
                word_display.append(letter)
            else:
                word_display.append('_')
                 
            
        # print(f'word display is {word_display}')    
        print(' '.join(word_display))
        guesses_left -= 1
        


# if guesses_left = 0:      
    # print('Sorry, you ran out of guesses. You lose.')
print(f"The word was {word_to_guess}")


    







    # if random.choice(stripped_words) == guess_word:
    #     print('you guessed it!')
    # else:
    #     print("try again!")

  













