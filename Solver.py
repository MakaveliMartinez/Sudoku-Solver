
from board import Board

'''
Function used to solve the sudoku board using backtracking
'''
def solve(board: Board):
    empty = board.findEmpty() #Scan the board for the first zero (Empty cell)

    if empty is None:
        return True #meaning it isn't empty and thus the board is solved

    row, col = empty #positon of first empty cell

    for val in range(1,10): # 1 --> 9 values, valid for the board
        board.calls[row][col] += 1
        if board.isValidMove(row,col,val):
            board.set(row,col,val)
            if solve(board):
                return True
            board.clear(row,col)
    return False



if __name__ == "__main__":
    board = Board()
    calls = Board()# board object
    solve(board)
    print(board)           # pretty print using overwritten __str__
    print("Number of recursive calls by a cell\n")
    print(board.print_calls())

    print(board.show_calls_heatmap())