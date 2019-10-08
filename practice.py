import random

# def open_and_read(file):

with open ("words.txt") as my_file:
    my_file = my_file.readlines()

    stripped_words = []
    for word in my_file:
        word = word.strip('\n')
      
        stripped_words.append(word)

  

    word_to_guess = random.choice(stripped_words)

    print("Letters in word: " + str(len(word_to_guess)))



    guess_letter = input("Guess a letter: ")
    if len(guess_letter) > 1 or len(guess_letter) < 1:
        print('Must be one letter')
    else:
        for letter in word_to_guess:
            if guess_letter != letter in word_to_guess:
                  print("guess again")
            if guess_letter == letter:
                print(guess_letter)
            



            # elif guess_letter != letter:
            #     print("guess again!")

    
    


    # print(guess_letter)


    # if random.choice(stripped_words) == guess_word:
    #     print('you guessed it!')
    # else:
    #     print("try again!")



    # for letter in word_to_guess:
    #     if guess_letter == letter:
    #         print(guess_letter)
    #     else:
    #         print("try again!")

  













