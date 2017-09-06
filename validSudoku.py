class validSudoku(object):
    def isValidSudoku(self, board):
        for i in range(9):
            if not self.validRow(board, i) or not self.validCol(board, i):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.validSquare(board, i, j):
                    return False
        return True
        
    def validRow(self, board, row):
        for i in range(9):
            if board[row][i] != '.':
                for j in range(9):
                    if i != j and board[row][i] == board[row][j]:
                        return False
        return True
    def validCol(self, board, col):
        for i in range(9):
            if board[i][col] != '.':
                for j in range(9):
                    if i != j and board[i][col] == board[j][col]:
                        return False
        return True
    def validSquare(self, board, row, col):
        for i in range(3):
            for j in range(3):
                if board[row+i][col+j] != '.':
                    for k in range(3):
                        for l in range(3):
                            if i != k and j != l and board[row+i][col+j] == board[row+k][col+l]:
                                return False
        return True
