import random
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


def print_result(winner):
    print(winner + "You have won!")


def ask_difficulty_level():
    difficulty_level = input("Choose difficulty level: \nEnter\n\t'e' for Easy\n\
    t'm' for Medium\n\t'h' for Hard\n: ").upper()
    while difficulty_level not in ['E', 'M', 'H']:
        print("Please choose from the options! ")
        difficulty_level = input("Choose difficulty level: \n\tEnter\n'e' for Easy\n\t'm' for Medium\n"
                                 "\t'h' for Hard\n: ").lower()
    return difficulty_level


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
    selected_level = ask_difficulty_level()
    word_to_find_out = ''
    if selected_level == 'E' or selected_level == 'M':
        word_to_find_out = get_word_for_easy_and_medium_level(selected_level)
    elif selected_level == 'H':
        word_to_find_out = get_word_to_hard_mode()
    word_letters = list(word_to_find_out)
    word_length = "_" * len(word_to_find_out)
    guessed_letters = []
    guessed = False
    print(hangman_display(players_lives))


if __name__ == '__main__':
    start_menu()
