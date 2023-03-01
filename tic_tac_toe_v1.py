#simple Tic-tac-toe program for 2 players by O.H.

#determines if user wants to play again
def cont(): 
     while True:
        cont = input("continue? y/n: ")
        if cont == "y":
            return True
        if cont == "n":
            return False
        else:
            print("napište y nebo n")

def show_board(board):
    for y in board:
        print(y)

def getValidInput(board, symbol):
            while True:
                rada = input("napište číslo řady: ")
                
                rada_index = input("napište číslo indexu řady: ")
                
                
                try:
                    rada = int(rada)
                    rada_index = int(rada_index)

                    rada -= 1;
                    rada_index -= 1;
                except(ValueError):
                    print("vstup musí být číslo")
                    continue

                if rada_index not in list(range(0,3)) or rada not in list(range(0,3)):
                    print("mimo rozsah pole")
                    continue
                else:
                    pass

                if board[rada][rada_index] != "-":
                    print("zde už symbol je")
                    continue
                else:
                    pass
                break

            board[rada][rada_index] = symbol
            return board

#checks if there is a winner
def isWinner(board):
    if checkRow(board) or checkColumn(board) or checkDiagonal(board):
        return True
    else:
        return False

# the following three functions check if there are 3 X's or O's along a diagonal, row or a column
def checkRow(board):
    for i in board:
        if len(set(i)) == 1 and "-" not in i:
            return True
    return False

def checkColumn(board):
    column = []
    index = 0
    for i in range(3):
        for row in range(len(board)):
            column.append(board[row][index])
        if len(set(column)) ==  1 and "-" not in column:
            return True
        else:
            column = []
            index += 1
    return False

def checkDiagonal(board):
    diagonal = []

    for row in range(len(board)):
        diagonal.append(board[row][row])
    if len(set(diagonal)) == 1 and "-" not in diagonal:
        return True

    diagonal = []

    for row in range(len(board)):
        diagonal.append(board[row][len(board)-row-1])
    if len(set(diagonal)) == 1 and "-" not in diagonal:
        return True
    return False

def chooseSymbol():
    while True:
        symbol = input("první hráč hraje jako X/O: ")
        if symbol == "X":
            return ["X","O"]
        elif symbol == "O":
            return ["O","X"]
        else:
            print("X nebo O")
            continue
        
#main game loop
def main():

    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    run = True
    new_board = True

    while run:
        if new_board:
            chars = chooseSymbol()
            board = [['-','-','-'],['-','-','-'],['-','-','-']]
            new_board = False
            show_board(board)
        
        getValidInput(board,chars[0])

        show_board(board)

        if isWinner(board):
            print("%s vyhrál"% (chars[0]))
            if cont():
                new_board = True
                continue
            else:
                run = False
                break

        getValidInput(board,chars[1])

        show_board(board)

        if isWinner(board):
            print("%s vyhrál"% (chars[1]))
            if cont():
                new_board = True
                pass
            else:
                run = False
                break
            
    print("děkujeme za hraní")



main()


