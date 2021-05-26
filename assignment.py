# Πρότυπο εργασίας
import os
from readdatatemplate import ToBoard,Formatter,Sequences
from PencilMark import Marking
from solver import SolveSudoku

if __name__=="__main__":
    sudokus = Sequences(os.path.join('','RESOURCES','sudokusequence.input'))
    for sudoku in sudokus:
       sudokuboard=ToBoard(sudoku)
       Formatter(sudokuboard)
       print() 
       Marking(sudokuboard)
       print()
       solved=SolveSudoku(sudokuboard)
       boardresult=ToBoard(solved)
       Formatter(boardresult)
       print('\n')
       print('--'*25)


