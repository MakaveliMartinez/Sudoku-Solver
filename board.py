class Board():
    def __init__(self):

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
    def get(self,row,col):
        return self.board[row][col]

    def set(self,row,col,val):
        self.board[row][col] = val

    def is_empty(self,row,col):
        if self.board[row][col] == 0:
            return True
        else:
            return False

    def findEmpty(self):
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r,c)
        return None #The board if full

    def isComplete(self):
        return self.findEmpty() is None #if we get none evaluated to true meaning no empty cells and the board is complete


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