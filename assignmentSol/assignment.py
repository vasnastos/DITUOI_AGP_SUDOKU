# Πρότυπο εργασίας
from sudoku import *

def main():
    inputdata=Input('') 
    stringtolist=list()
    for sudoku in inputdata:
       print(f'Sequence used:{sudoku}\n')
       print('Preview')
       Formatter(sudoku)
       print('\nMarking')
       pencilMark(sudoku)
       print('\nSolution')
       solutionproblem=SolveSudoku(sudoku)
       Formatter(solutionproblem)
       print('-------------------------------------------------------------------\n')

if __name__=="__main__":
    main()



