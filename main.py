# naughts and crosses
import sys
import os

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

row = [" "," "," "," "," "," "," "," "," "]
go = 0
game = 1

display = """1,2,3
4,5,6
7,8,9

this is how the board is set up (1 = top left)
"""

def grid():
    print(row[:3])
    print(row[3:6])
    print(row[6:])

def end_x():
    clear_console()
    print("x wins")
    grid()
    var = input("Would you like to play again? [Y/N]\n").upper()

    if var == 'N':
        print("Thanks for playing")
        sys.exit()

def end_o():
    clear_console()
    print("o wins")
    grid()
    var = input("Would you like to play again? [Y/N]\n").upper()

    if var == 'N':
        print("Thanks for playing!")
        sys.exit()

print(display)
count = 0
while game == 1:
    while go != 1:
        p1 = int(input("player 1, where do you want to place x? "))
        clear_console()
        if row[p1-1] == " ":
            row[p1-1] = 'x'
            count += 1
            go = 1
            print(display)
            grid()
        else:
            print(display)
            print("invalid move")
            grid()

        if row[0] == 'x' and row[1] == 'x' and row[2] == 'x':
            end_x()
        elif row[3] == 'x' and row[4] == 'x' and row[5] == 'x':
            end_x()
        elif row[6] == 'x' and row[7] == 'x' and row[8] == 'x':
            end_x()
        elif row[0] == 'x' and row[3] == 'x' and row[6] == 'x':
            end_x()
        elif row[2] == 'x' and row[4] == 'x' and row[7] == 'x':
            end_x()
        elif row[3] == 'x' and row[5] == 'x' and row[8] == 'x':
            end_x()
        elif row[0] == 'x' and row[4] == 'x' and row[8] == 'x':
            end_x()
        elif row[2] == 'x' and row[4] == 'x' and row[6] == 'x':
            end_x()
        
    go = 0

    if count == 9:
        print("Game over, its a draw")
        sys.exit()

    while go != 1:
        p2 = int(input("player 2, where do you want to place o? "))
        clear_console()
        if row[p2-1] == " ":
            row[p2-1] = 'o'
            count += 1
            go = 1
            print(display)
            grid()
        else:
            print(display)
            print("invalid move")
            grid()

        if row[0] == 'o' and row[1] == 'o' and row[2] == 'o':
            end_o()
        elif row[3] == 'o' and row[4] == 'o' and row[5] == 'o':
            end_o()
        elif row[6] == 'o' and row[7] == 'o' and row[8] == 'o':
            end_o()
        elif row[0] == 'o' and row[3] == 'o' and row[6] == 'o':
            end_o()
        elif row[2] == 'o' and row[4] == 'o' and row[7] == 'o':
            end_o()
        elif row[3] == 'o' and row[5] == 'o' and row[8] == 'o':
            end_o()
        elif row[0] == 'o' and row[4] == 'o' and row[8] == 'o':
            end_o()
        elif row[2] == 'o' and row[4] == 'o' and row[6] == 'o':
            end_o()
    
    go = 0
    


