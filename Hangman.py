import random
import time


def start_menu():
    print("START MENU\n\nStart Game\nQuit")
    start_menu_command = input("Enter 's' to start game and 'q' to quit game").upper()
    if start_menu_command == 'S':
        main_game_logic()
    elif start_menu_command == 'Q':
        quit(0)


def ask_player_name():
    player_name = input("Enter your name: ").capitalize()
    return player_name


def get_word_for_easy_and_medium_level(selected_level):
    with open("countries-and-capitals.txt", "r") as countries_and_capitals:
        word_list = []
        open_file_for_read = open("countries-and-capitals.txt", "r")
        for line in countries_and_capitals.readlines():
            if selected_level == "easy":
                word_list.append(line.split('|')[0].strip())
            elif selected_level == "hard":
                word_list.append(line.split('|')[1].strip())
            return word_list[random.randint(0, len(word_list) - 1)]


def get_word_to_hard_mode():
    with open("words.txt", 'r') as words:
        words_red = words.read()
        words_list = words_red.split(" ")
        return words_list[random.randint(0, len(words_list) -1)]


def print_result(winner):
    print(winner + "You have won!")


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
    while players_lives > 0:
        pass


if __name__ == '__main__':
    start_menu()
    main_game_logic()