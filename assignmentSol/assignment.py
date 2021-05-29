# Πρότυπο εργασίας
from sudoku import *

def main():
    inputdata=Input('') 
    stringtolist=list()
    for sudoku in inputdata:
       print(f'Sequence used:{sudoku}\n')
       stringtolist=ToBoard(sudoku)
       print('Preview')
       Formatter(stringtolist)
       print('\nMarking')
       pencilMark(sudoku)
       print('\nSolution')
       solutiontoproblem=SolveSudoku(stringtolist)
       solutiontolist=ToBoard(solutiontoproblem)
       Formatter(solutiontolist)
       print('-------------------------------------------------------------------\n')

if __name__=="__main__":
    main()



