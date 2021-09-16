import random
import time


def ask_player_name():
    player_name = input("Enter your name: ")
    return player_name



def get_word_to_hard_mode():
    with open("words.txt", 'r') as words:
        words_red = words.read()
        words_list = words_red.split(" ")
        return words_list[random.randint(0, len(words_list) -1)]


def print_result(winner):
    print(winner + "You have won!")


def main_game_logic():
    pass


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


if __name__ == '__main__':
    print(get_word())
