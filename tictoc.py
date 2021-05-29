


import numpy as np

def show_titctoc_board(board):
    for r in board:
        for c in r:
            print(c,end = " ")
        print()
    print()


def checkRows(board,dec):
    for row in board:
        if len(set(row)) == 1:
            if row[0] == dec:
                return True
    return False

def checkDiagonals(board,dec):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] == dec:
            return True

    if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
        if board[0][len(board)-1] == dec:
            return True
    return False

def manin(name,T,turn):
    count = 0
    while True:

        try:
            show_titctoc_board(T)
            x=input()
            if x == "exit":
                print("exit")
                return False
            newplace =[int(i) for i in x.split(" ")]
            
            if T[newplace[0]-1][newplace[1]-1] != "-":
                print("Not valid")
            else:
                T[newplace[0]-1][newplace[1]-1] = turn
                count += 1
                show_titctoc_board(T)

                for newBoard in [T, np.transpose(T)]:
                    if checkRows(newBoard,turn) :
                        return print(name[turn]+" Won the game")

                if checkDiagonals(T,turn):
                    return print(name[turn]+" Won the game")

                if count == np.array(T).size:
                    break

                if turn == 'X':
                    turn = 'O'
                else :
                    turn = 'X'
                
        except Exception as e:
            print(e)
            print("not valid")
    print("Game Over")



T = [["-","-","-"], ["-", "-","-"], ["-", "-", "-"]]
first = input("player 1 :")
second = input("Player 2 :")
name = {"X":first,"O":second}
turn = "X"
manin(name,T,turn)


    
    