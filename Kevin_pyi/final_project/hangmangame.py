import os
import random
import time


def welcome():
    os.system('cls')

    print('''======================================
    Welcome to the HANGMAN GAME!!!
            ------------
            |         |
            |          O 
            |         / |
            |          |
            |         / | 
            |
            |     
======================================                
Press ENTER to continue''')

    input()
    os.system('cls')
    print('Loading...')

    time.sleep(1)
    os.system('cls')


def selectWord():
    with open("./words.txt", "r", encoding='UTF-8') as f:
        # se crea una lista con las palabras y se elimina el caracter \n
        words = [i.replace("\n", "") for i in f]

        # se selecciona una palabra de la lista al azar
        w = random.choice(words)

        # crea un diccionario ASCII donde las llaves son los numeros que representan las letras con tilde, y los values son los numeros que representan a las letras sin tilde
        corrections = w.maketrans('áéíóú', 'aeiou')

        # se utiliza el diccionario para corregir las letras con tilde
        w = w.translate(corrections)
        return w.upper()


def level():

    print('''======================================
    Select difficulty level:
          
        (1) AMATEUR 
                
        (2) INTERMIDIATE
        
        (3) PRO\n
              ''')


def score_of_the_game(letters_complited, word_to_guess, random_word):
    if ''.join(letters_complited) == word_to_guess:
        os.system('cls')
        print(f'''======================================
CONGRATULATIONS
              
You are the winner!
======================================
The word was : {random_word}
''')

    else:
        print(f'''======================================
GAME OVER

You have lost the game!
======================================  
The word was : {random_word}            
              ''')


def attemps_allowed(attempts):
    done = False
    error_num = 0
    while not done:
        try:
            level()

            difficulty = int(input('Type the level number:\t\t'))
            time.sleep(1)
            os.system('cls')

            if difficulty == 1:
                difficulty = attempts*2
                done = True
                return difficulty

            elif difficulty == 2:
                difficulty = attempts + (attempts*1.5)
                done = True
                return difficulty

            elif difficulty == 3:
                difficulty = attempts
                done = True
                return difficulty

            else:
                os.system('cls')
                print('''======================================
There is not such level.\n\nPlease type level (1), (2) or (3)
======================================\n''')
                print('Press ENTER to continue')
                input()
                os.system('cls')
                error_num += 1

        except ValueError as ve:
            os.system('cls')
            print('''======================================
Strings are not allowed!\n\nPlease type level (1), (2) or (3)
======================================\n\n''')
            print('Press ENTER to continue')
            input()
            os.system('cls')
            error_num += 1


def play():
    # gets a random word
    random_word = selectWord()

    # establishing attemps according the difficulty choosed
    game_attempts_allowed = attemps_allowed(len(random_word))

    # lines to be printed and changed according to the letter guessed
    lines = '_' * len(random_word)
    listed_as_letters = list(lines)
    attempts_left = game_attempts_allowed

    while True:
        # counter of attempts left
        attempts_played = []

        os.system('cls')
        print(f'Attempts left:\t\t{attempts_left}')
        print('''
======================================              
           GUESS THE WORD!
======================================\n''')
        print(' '.join(listed_as_letters))

        # get the letter that player chose
        selected_letter = input("\nType a letter: ").upper()

        # compare the letter chose with the letters of the word and get the indices
        for index, string in enumerate(random_word):
            if selected_letter == string:
                listed_as_letters[index] = selected_letter
            else:
                # this is the first step to know if the answer is wrong
                attempts_played.append(string)

        # this is the second and final step to know if the answer is wrong
        if len(attempts_played) >= len(random_word):
            # if it's wrong then substract 1 attempt allowed
            attempts_left -= 1
        else:
            pass

        #
        if not '_' in listed_as_letters:
            score_of_the_game(listed_as_letters, random_word, random_word)
            break
        else:
            pass

        print('''
======================================              
Press ENTER to continue''')
        input()

        # when there is no more attemps left the loop will break
        if attempts_left == 0:
            print('There is no more attempts left!')
            print('\nPress ENTER to continue')
            input()
            os.system('cls')

            score_of_the_game(listed_as_letters, random_word, random_word)
            break


def run():
    welcome()
    play()


if __name__ == "__main__":
    run()
