import sudokuSolver
import sudokuCreator
import copy
import sys

def main():
	if len(sys.argv) != 2:
		print "Invalid number of arguments"
		print "Must be in format: python create.py easy"
		return
	level = sys.argv[1]
	level = level.lower()
	if level != "easy" and level != "medium" and level != "hard" and level != "extreme":
		print "Invalid level argument"
		print "Must be in format: python create.py easy"
		print "Levels are easy, medium, hard, extreme"
		return
	sudokuChecker().create(level)
		

class sudokuChecker(object):
	def create(self, level):
		valid = False
		while not valid:
			s = sudokuCreator.SudokuCreator()
			s.createSudoku(level)
			board = copy.deepcopy(s.getBoard())
			t = sudokuSolver.SudokuSolver(s.getBoard())
			if t.solve(s.getBoard()):
				print s.getBoard()
				print board
				valid = True


if __name__ == "__main__":
	main()

