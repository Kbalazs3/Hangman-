import random
import os
import time


def start_menu():
    print("START MENU\n\nStart Game\nQuit")
    start_menu_command = input("Enter 's' to start game and 'q' to quit game\n: ").upper()
    if start_menu_command == 'S':
        main_game_logic()
    elif start_menu_command == 'Q':
        print("\n\n\n\t\t\t\t\t\t\t\tBye-bye!\n\n\n")
        quit(0)
    else:
        print("\nEnter 's' or 'q'!\n")
        start_menu()


def ask_player_name():
    player_name = input("Enter your name: ").capitalize()
    return player_name


def tabs_to_push_to_middle():
    return "\t" * 6


def get_word_for_easy_and_medium_level(selected_level):
    word_list = []
    open_file_for_read = open("countries-and-capitals.txt", "r")
    for line in open_file_for_read.readlines():
        if selected_level == "E":
            word_list.append(line.split('|')[0].strip())
        elif selected_level == "M":
            word_list.append(line.split('|')[1].strip())
    open_file_for_read.close()
    return word_list[random.randint(0, len(word_list) - 1)]


def get_word_to_hard_mode():
    with open("words.txt", 'r') as words:
        words_red = words.read()
        words_list = words_red.split(" ")
        return words_list[random.randint(0, len(words_list) - 1)]


def ask_difficulty_level():
    difficulty_level = input("Choose difficulty level: \nEnter\n\t'e' for Easy\n\
    t'm' for Medium\n\t'h' for Hard\n: ").upper()
    while difficulty_level not in ['E', 'M', 'H']:
        print("Please choose from the options! ")
        difficulty_level = input("Choose difficulty level: \n\tEnter\n'e' for Easy\n\t'm' for Medium\n"
                                 "\t'h' for Hard\n: ").lower()
    return difficulty_level


def clear():
    time.sleep(3)
    os.system('cls')


def hangman_display(lives):
    hangman = [  # You loose element 0
        """
            _________________________
            |\ _____________________ /|
            | |_____________________| |
            |/_______________________\|
            /=========================\ 
            '==========================='
            |  ~~       _|_        ~~ |
            |        You Loose        |
            |_________________________|
                        """,

        # 1 health
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \
           -
        """,
        # Two health minus
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        """,
        # Three lives minus
        """
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        """,
        # Four lives minus
        """
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        """,
        # Five lives minus
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # Six lives minus
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # Seven lives minus -> Game Over
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]

    return hangman[lives]


def main_game_logic():
    player_name = ask_player_name()
    players_lives = 7
    print(f'\nWelcome {player_name} in the Hangman Game!\n')
    selected_level = ask_difficulty_level()
    word_to_find_out = ''
    if selected_level == 'E' or selected_level == 'M':
        word_to_find_out = get_word_for_easy_and_medium_level(selected_level).lower()
        if selected_level == 'E':
            print("You will have to find out a country name.")
        elif selected_level == 'M':
            print('You will have to find out a capital city.')
    elif selected_level == 'H':
        word_to_find_out = get_word_to_hard_mode().lower()
        print("You will have get any random word.")
    word_letters = list(word_to_find_out)
    word_length = "_" * len(word_to_find_out)
    word_length_list = list(word_length)
    tried_letters = []
    guessed = False
    print(word_length)
    print("\n")
    while not guessed and players_lives > 0:
        if players_lives == 0:
            print(f'\t\t\t\t{player_name} You loose!\n\n')
            break
        elif "".join(word_length_list) == word_to_find_out:
            print(f'\n\n\t\t\t\t\t\tCongratulations {player_name} You win!\n\n')
            break
        print(f'\nRemaining lives: {str(players_lives)}')
        print("Tried letters: " + ", ".join(tried_letters) + "\n")
        guess = input("Guess a letter: ").lower()
        while len(guess) != 1 and not guess.isalpha():
            print("Please enter only one letter!")
            guess = input("Guess a letter: ").lower()
        if guess in tried_letters:
            print("You have tried that before!")
        elif len(guess) == 1 and guess.isalpha() and guess not in word_letters and guess not in tried_letters:
            players_lives -= 1
            print("That's wrong! You lost one life point!\n")
            print(hangman_display(players_lives))
            if players_lives == 0:
                print(f'\n\t\t\t\t\t\t{player_name} You loose!\n\n')
                print(f'\t\t\t\t\t\tThe solution would have been: {word_to_find_out}\n')
                break
        elif guess in word_letters and guess not in tried_letters:
            for index, letter in enumerate(word_letters):
                if guess == letter:
                    word_length_list[index] = guess
        elif guess == 'quit':
            print("Bye-bye!")
            start_menu()
            break
        print("".join(word_length_list))
        if len(guess) == 1 and guess.isalpha():
            tried_letters.append(guess)
    clear()
    start_menu()

if __name__ == '__main__':
    start_menu()
