from random import randint


OPPONENT_GRID = [[' '] * 5 for i in range(5)]
USER_GRID = [[' '] * 5 for i in range(5)]
int_letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4}


def startup_message():
    """ This is the welcome message """
    print(""" \u001b[34m
(____  \   /\  (_______(_______| |     (_______)  | |  | |   | (_____(_____ \
 ____)  ) /  \  _       _      | |      _____      \ \ | |__ | |  _   _____) )
|  __  ( / /\ \| |     | |     | |     |  ___)      \ \|  __)| | | | |  ____/
| |__)  | |__| | |_____| |_____| |_____| |_____ _____) | |   | |_| |_| |
|______/|______|\______)\______|_______|_______(______/|_|   |_(_____|_|""")
    print("Welcome to Battleships")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[35m+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[37mThe aim of the game is to find and bomb 5 ships\u001b[0m")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[37mYou have 15 bombs to do this\u001b[0m")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[37mTo win, destroy all 5 enemy ships\u001b[0m")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[37mSelect a row and column when prompted\u001b[0m")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")
    print("\u001b[32mO=Miss \u001b[31mX=Hit\u001b[0m")
    print("\u001b[35m_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_\u001b[0m")


startup_message()


def print_grid(grid):
    """the function called to print the playing board to the terminal"""
    print('  A B C D E')
    print(' ___________')
    row_num = 1
    for row in grid:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num += 1
    print("\u001b[31m ===========\u001b[0m")


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
    row = input("Enter the row you want to bomb: ")
    print('____________________________________________')
    while row not in ["1", "2", "3", "4", "5"]:
        print('\u001b[37mPlease enter a valid co-ordinate\u001b[0m')
        print('____________________________________________')
        row = input("\u001b[37mEnter a row 1-5: ")
    column = input("\u001b[37mEnter column to bomb: \u001b[0m").upper()
    print('____________________________________________')
    while column not in ["A", "B", "C", "D", "E"]:
        print('\u001b[37mPlease enter a a valid co-ordinate\u001b[0m')
        print('____________________________________________')
        column = input("\u001b[37mEnter a value A-E: \u001b[0m").upper()
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
        print('\u001b[33m__________________________________________\u001b[0m')
        print('Enter the co-ordinates you want to bomb\u001b[0m')
        print('\u001b[33m__________________________________________\u001b[0m')
        print_grid(USER_GRID)
        row, column = target()
        if USER_GRID[row][column] == "O":
            print("Location already hit")
        elif OPPONENT_GRID[row][column] == "X":
            print("\u001b[32mYou sunk my battleship!\u001b[0m")
            print('\u001b[33m_______________________________________\u001b[0m')
            USER_GRID[row][column] = "X"
            bombs -= 1
        else:
            print("\u001b[31mMISS!\u001b[0m")
            USER_GRID[row][column] = "O"
            bombs -= 1
        if hit_counter(USER_GRID) == 5:
            print("\u001b[32mCongrats! You sunk my battleships.\u001b[0m")
            print('\u001b[33m_______________________________________\u001b[0m')
            break
        print("You have " + str(bombs) + " bombs left")
        print('\u001b[33m_______________________________________\u001b[0m')
        if bombs == 0:
            print("\u001b[31mGame Over! You have been defeated.")
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
            print('____________________________________________')


print("Thank you for playing.")
