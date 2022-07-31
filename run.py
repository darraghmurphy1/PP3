import colorama 
from colorama import Fore, Back
colorama.init()

OPPONENT_GRID = [[' '] * 5 for i in range(5)]
USER_GRID = [[' '] * 5 for i in range(5)]
int_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def startup_message():
    """ This is the welcome message """
    print(Fore.BLUE + """
(____  \   /\  (_______(_______| |     (_______)  | |  | |   | (_____(_____ \ 
 ____)  ) /  \  _       _      | |      _____      \ \ | |__ | |  _   _____) )
|  __  ( / /\ \| |     | |     | |     |  ___)      \ \|  __)| | | | |  ____/ 
| |__)  | |__| | |_____| |_____| |_____| |_____ _____) | |   | |_| |_| |      
|______/|______|\______)\______|_______|_______(______/|_|   |_(_____|_|      
                                                                              
                                                                                                                 
    """)
    print(Fore.BLUE + "Welcome to Battleships")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print(Fore.BLUE + "The aim of the game is to locate and bomb 5 ships")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print(Fore.BLUE + "You have 15 bombs to do this")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print(Fore.BLUE + "To win, destroy all 5 enemy ships")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
    print(Fore.BLUE + "O=Miss X=Hit")
    print(Fore.WHITE + "_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")


startup_message()


def print_grid(grid):
    """the function called to print the playing board to the terminal"""
    print(Fore.YELLOW + '  A B C D E')
    print(Fore.WHITE + ' ___________')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print(Fore.RED + " ===========")


