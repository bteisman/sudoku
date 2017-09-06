from random import randint
import validSudoku

class SudokuCreator(object):

	positions = {}
	board = []
	count = None

	def __init__(self):
		self.board = [
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.'],
			['.','.','.','.','.','.','.','.','.']
		]
		self.count = 0

	def createSudoku(self, level):
		if level == "easy":
			while self.count != 35:
				self.randomPosition()
		elif level == "medium":
			while self.count != 30:
				self.randomPosition()
		elif level == "hard":
			while self.count != 28:
				self.randomPosition()
		elif level == "extreme":
			while self.count != 25:
				self.randomPosition()

	def randomPosition(self):
		row = randint(0, 8)
		col = randint(0, 8)
		num = randint(1, 9)
		if self.board[row][col] == '.':
			self.count += 1
			self.board[row][col] = str(num)
			if not validSudoku.validSudoku().isValidSudoku(self.board):
				self.board[row][col] = '.'
				self.count -= 1

	def getBoard(self):
		return self.board

