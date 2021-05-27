# Πρότυπο εργασίας
from sudoku import *

def main():
    inputdata=Input('')
    inputdata.append('068420709001070450037085010002109080809300005010040096084006003000000800050034001')
    stringtolist=list()
    for x in inputdata:
       print(f'Sequence used:{x}\n')
       stringtolist=ToBoard(x)
       Formatter(stringtolist)
       print()
       pencilMark(stringtolist)
       print()
       solutiontoproblem=SolveSudoku(stringtolist)
       solutiontolist=ToBoard(solutiontoproblem)
       Formatter(solutiontolist)
       print('-------------------------------------------------------------------\n')

if __name__=="__main__":
    main()



