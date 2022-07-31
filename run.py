import colorama 
from colorama import Fore, Back
colorama.init()


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



OPPONENT_GRID = [[' '] * 5 for i in range(5)]
USER_GRID = [[' '] * 5 for i in range(5)]
