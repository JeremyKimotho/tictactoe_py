#Constants for piece types
EMPTY = 0
X = 1
O = 2
class Board:
    def __init__(self, rows=3, columns=3):
        self.board = []
        for i in range(0, rows):
            colum=[]
            for i in range (0, columns):
                colum.append(EMPTY)
            self.board.append(colum)
    
    def canPlay(self, row, column):
        if self.board[row][column]==EMPTY:
            return True
        else:
            return False
    
    def play(self, row, column, piece):
        self.board[row][column]=piece

    def cols(self):
        return len(self.board[0])

    def rows(self):
        return len(self.board)
                    
    def full(self):
        for x in range(0,len(self.board)):
            for i in self.board[x]:
                if i==EMPTY:
                    return False
        return True
            
   
    def winInRow(self, row, piece):
        for x in range(0, len(self.board[row])-2):
            if self.board[row][x]==piece and self.board[row][x+1]==piece:
                if self.board[row][x+2]==piece:
                    return True
        return False

    def winInCol(self, column, piece):
        for i in range(len(self.board)-2):
            if self.board[i][column]==piece and self.board[i+1][column]==piece:
                if self.board[i+2][column]==piece:
                    return True
        return False
        

    def won(self, piece):
        return False
            
    def hint(self, piece):             
        return -1, -1
    
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False
