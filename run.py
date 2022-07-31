from random import randint
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


def spawn_ships(grid):
    """ This function spawns 5 ships in random locations across the grid and
     marks them with an 'X' after importing randInt. 
    It will pick a row and column and place a ship in that coordinate"""
    for ship in range(5):
        ship_row, ship_column = randint(0, 4), randint(0, 4)
        while grid[ship_row][ship_column] == "X":
            ship_row, ship_column = target()
        grid[ship_row][ship_column] = "X"


def target():
    """ this function allows the user to target their desired coordinates
    validation is used to make sure the coordinates are valid."""
    row = input(Fore.BLUE + "Enter the row you want to bomb: ")
    print('____________________________________________')
    while row not in ["1", "2", "3", "4", "5"]:
        print('Please enter a valid co-ordinate')
        print('____________________________________________')
        row = input("Enter a row 1-5: ")
    column = input("Enter the column you want to bomb: ").upper()
    print('____________________________________________')
    while column not in ["A", "B", "C", "D", "E"]:
        print('Please enter a a valid co-ordinate')
        print('____________________________________________')
        column = input("Enter a value A-E: ").upper()
    return int(row) - 1, int_letters[column]


def hit_counter(grid):
    """ This function counts the amount of ships that have been hit
     succesfully so that the game can end when all 
     ships are hit. for loop simply looks for 'X'
    meaning hit and adds that to the count."""
    count = 0
    for row in grid:
        for column in row:
            if column == "X":
                count += 1
    return count


if __name__ == "__main__":
    """ if statement that displays the game. creates 'bombs' or lives 
    which are used to tell if the user won or lost the game.""" 
    spawn_ships(OPPONENT_GRID)
    bombs = 15
    while bombs > 0:
        print('____________________________________________')
        print('Enter the co-ordinates you want to bomb')
        print('____________________________________________')
        print_grid(USER_GRID)
        row, column = target()
        if USER_GRID[row][column] == "O":
            print("Location already hit")
        elif OPPONENT_GRID[row][column] == "X":
            print(Fore.GREEN + "You sunk my battleship!")
            print('____________________________________________')
            USER_GRID[row][column] = "X"
            bombs -= 1  
        else:
            print(Fore.RED + "MISS! RELOAD!")
            USER_GRID[row][column] = "O"
            bombs -= 1     
        if hit_counter(USER_GRID) == 5:
            print(Fore.GREEN + "Congratultions! You sunk my battleships.")
            print('____________________________________________')
            break
        print("You have " + str(bombs) + " bombs left")
        print(Fore.WHITE + '____________________________________________')
        if bombs == 0:
            print(Fore.RED + "Game Over! You have been defeated.")
            print("""
            
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄

            """)
            print(Fore.WHITE + '____________________________________________')


print(Back.GREEN + Fore.WHITE + "Thank you for playing.")
