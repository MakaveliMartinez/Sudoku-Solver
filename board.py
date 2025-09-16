import matplotlib.pyplot as plt
import numpy as np

class Board():
    def __init__(self):

        self.calls = [[0] * 9 for _ in range(9)] #Board of the same shape to keep track of recusrive calls by cell
        self.board = [
                        [5, 3, 0, 0, 7, 0, 0, 0, 0],
                        [6, 0, 0, 1, 9, 5, 0, 0, 0],
                        [0, 9, 8, 0, 0, 0, 0, 6, 0],
                        [8, 0, 0, 0, 6, 0, 0, 0, 3],
                        [4, 0, 0, 8, 0, 3, 0, 0, 1],
                        [7, 0, 0, 0, 2, 0, 0, 0, 6],
                        [0, 6, 0, 0, 0, 0, 2, 8, 0],
                        [0, 0, 0, 4, 1, 9, 0, 0, 5],
                        [0, 0, 0, 0, 8, 0, 0, 7, 9]
                    ]

    """
    Using a heatmap to display where the most recursion calls happen on the board
    """
    def show_calls_heatmap(self):
        data = np.array(self.calls)

        plt.imshow(data,cmap ="hot", interpolation = "nearest")
        plt.colorbar(label = "Recursive Calls")
        plt.title("Sudoku Solver Recursion Heat Map")

        for i in range(9):
            for j in range(9):
                val = data[i,j]
                if val > 0:
                    plt.text(j, i, str(val),
                             ha="center", va="center",
                             color="white", fontsize=8)
        plt.show()
    """
    Function to return the value at a specific position 
    """
    def get(self,row,col):
        return self.board[row][col]


    """
    Function to set the value of a position on the board
    """
    def set(self,row,col,val):
        if not  (0<= row < 9 and 0 <= col < 9): #This make sure we saty within the bounds of the board
            raise IndexError("Row and column must be between 0 and 8")
        if not (0<= val <= 9 ): #makes sure the values we input are from 0 -> 9 we have to include zeor setting to zero
            raise ValueError("Value must be between 0 and 9")
        self.board[row][col] = val

    """
    A check to see if a specific cell on a board is empty denoted by a "0"
    """
    def is_empty(self,row,col):
        if self.board[row][col] == 0:
            return True
        else:
            return False

    """
    Finding the next empty cell
    """
    def findEmpty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r,c)
        return None #The board if full

    def isComplete(self):
        return self.findEmpty() is None #if we get none evaluated to true meaning no empty cells and the board is complete

    def clear(self,row,col):
        self.board[row][col] = 0

    #Checking of valid moves, first checking the value itself, then row, column , and finally the subgrid
    def isValidMove(self,row,col,val):
        if not(1<= val <=9 ) or self.board[row][col] != 0:
            return False
        #This checks the row
        if any(self.board[row][j] == val for j in range(9)):
            return False
        #This checks the column
        if any(self.board[i][col] == val for i in range(9)):
            return False

        #This checks the sub grids
        br, bc = (row//3) * 3 , (col // 3) * 3
        for i in range(br, br+3):
            for j in range(bc, bc+3):
                if self.board[i][j] == val:
                    return False
        return True

    """
    Printing how many times each cell is called recusrivel by using a similar board where the cell represents
    how many recursive calls where used to find that solution
    """
    def print_calls(self):
        lines = ["+---------------------------+---------------------------+---------------------------+"]
        for r in range(9):
            row_str = ""
            for c in range(9):
                if c % 3 == 0:
                    row_str += "| "
                val = self.calls[r][c]
                # right-align each number in width 4
                row_str += (str(val).rjust(4) if val > 0 else "   .") + " "
            row_str += "|"
            lines.append(row_str)
            if (r + 1) % 3 == 0:
                lines.append("+---------------------------+---------------------------+---------------------------+")
        print("\n".join(lines))

    def __str__(self):
        lines = ["+-------+-------+-------+"]
        #Border at the top of the board
        for r in range(9):
            row_str = "" #start string for the board
            for c in range(9):
                if c %3 == 0: #divide into subgrids
                    row_str += "| "
                val = self.board[r][c]
                row_str +=(str(val) if val != 0 else ".") + " " #adding either a . or the value with a space
            row_str+="|" #manually adding in the last border
            lines.append(row_str) #adding this row as an element to lines
            if(r+1)%3 == 0: # Adding a boarder after every 3 rows / helping divide into subgroups
                lines.append("+-------+-------+-------+")
        return "\n".join(lines)