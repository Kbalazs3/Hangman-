import random
import time


def ask_player_name():
    player_name = input("Enter your name: ")
    return player_name


def get_word():
    with open("words.txt", 'r') as words:
        words_red = words.read()
        words_list = words_red.split(" ")
        return words_list[random.randint(0, len(words_list) -1)]


def print_result(winner):
    print(winner + "You have won!")


def main_game_logic():
    pass


if __name__ == '__main__':
    print(get_word())
