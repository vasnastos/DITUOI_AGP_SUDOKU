# Πρότυπο εργασίας
from sudoku import *

def main():
    inputdata=Input('')
    stringtolist=list()
    for x in inputdata:
       print(f'Sequence used:{x}\n')
       stringtolist=ToBoard(x)
       print('Preview')
       Formatter(stringtolist)
       print('\n\Marking')
       pencilMark(stringtolist)
       print('\n\t\tSolution')
       solutiontoproblem=SolveSudoku(stringtolist)
       solutiontolist=ToBoard(solutiontoproblem)
       Formatter(solutiontolist)
       print('-------------------------------------------------------------------\n')

if __name__=="__main__":
    main()



