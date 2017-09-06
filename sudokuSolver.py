from collections import deque        

class SudokuSolver(object):
    initboard = []

    def __init__(self, board):
        self.initboard = board

    def getInit(self):
        return self.initboard

    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        if self.solvedBoard(board):
            return True
        spot = self.nextSpot(board)
        if spot == [-1,-1]:
            return False
        for i in range(1,10):
            if self.valid(board, spot[0], spot[1], str(i)):
                board[spot[0]][spot[1]] = str(i)
                if self.solve(board):
                    return True
                board[spot[0]][spot[1]] = '.'


    def nextSpot(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return [i,j]
        return [-1,-1]

    def solvedBoard(self, board):
        for i in range(9):
            if not self.validRow(board, i) or not self.validCol(board, i) or not self.validSquare(board, i, i):
                return False
        return True

    def valid(self, board, row, col, num):
        if int(num) > 9 or int(num) < 0:
            return False
        if self.notInRow(board,row,num) and self.notInCol(board,col,num) and self.notInSquare(board,((int(row)/3)*3),((int(col)/3)*3),num):
            return True
        return False

    def validRow(self, board, row):
        for i in range(1,10):
            if self.notInRow(board, row, str(i)):
                return False
        return True

    def validCol(self, board, col):
        for i in range(1,10):
            if self.notInCol(board, col, str(i)):
                return False
        return True

    def validSquare(self, board, row, col):
        for i in range(1,10):
            if self.notInSquare(board,((int(row)/3)*3),((int(col)/3)*3),str(i)):
                return False
        return True
    
    def notInRow(self, board, row, num):
        for i in range(9):
            if board[row][i] == num:
                return False
        return True
    
    def notInCol(self, board, col, num):
        for i in range(9):
            if board[i][col] == num:
                return False
        return True
    
    #use start row and col of square. Ex - 0,0 3,0 3,6
    def notInSquare(self, board, row, col, num):
        for i in range(row, (row+3)):
            for j in range(col, (col+3)):
                if board[i][j] == num:
                    return False
        return True







