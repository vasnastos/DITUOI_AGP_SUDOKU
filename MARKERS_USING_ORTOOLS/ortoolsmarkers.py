#Marking in a sudoku problem using ortools

from ortools.sat.python import cp_model
import math
import logging as log

logger=log.getLogger('SudokuLogger')
logger.setLevel(log.DEBUG)
fh=log.FileHandler('SudokuLogger.log','w')
sh=log.StreamHandler()
formatter=log.Formatter('%(asctime)s\n%(levelname)s\n%(message)s')
fh.setFormatter(formatter)
sh.setFormatter(formatter)
logger.addHandler(sh)
logger.addHandler(fh)

gap=13
sudokuproblem='070000043040009610800634900094052000358460020000800530080070091902100005007040802'

class Mark(cp_model.CpSolverSolutionCallback):
    def __init__(self,vars,srow,scol):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables=vars
        self.__vals=''
        self.r=srow
        self.c=scol
    
    def on_solution_callback(self):
        self.__vals+=str(self.Value(self.__variables[self.r,self.c]))
    
    def getValue(self):
        return self.__vals

def ToBoard():
    data=list()
    index=0
    count=9
    while index<81:
        data.append(sudokuproblem[index:count])
        index=count
        count+=9
    return data

def Marking(row,col):
    model=cp_model.CpModel()
    cells=dict()
    for i in range(9):
        for j in range(9):
            cells[i,j]=int(sudokuproblem[i*9+j])
    cells[row,col]=model.NewIntVar(1,9,f'cell{row}{col}')

    model.AddAllDifferent([cells[row,j] for j in range(9) if cells[row,j]!=0])
    model.AddAllDifferent([cells[i,col] for i in range(9) if cells[i,col]!=0])
    valrow=row//3
    valcol=col//3
    valrow*=3
    valcol*=3
    counter=3
    model.AddAllDifferent([cells[i,j] for j in range(valcol,(valcol+counter)) for i in range(valrow,(valrow+counter)) if cells[i,j]!=0])
    solcallback=Mark(cells,row,col)
    solver=cp_model.CpSolver()
    status=solver.SearchForAllSolutions(model,solcallback)
    logger.info(f'Row:{row}\nColumn:{col}\nValues:{solcallback.getValue()}\n\n')
    return solcallback.getValue()

def CmdMarking(data, searchmark):
    # Start with printing results
    print(str("." + "-" * (2 * gap) + "") * 3 + ".")
    i=0
    for x in data:
        if i % 3 == 0 and i != 0:
            print(":", end="")
            print(("-" * (2 * gap) + ":") * 2, end="")
            print("-" * (2 * gap) + ":")
        print("|", end="")
        for j in range(0, len(x), 3):
            output1 = (
                str(x[j] + " " * 7)
                if x[j] != "0"
                else searchmark[i,j]
                + str(" " * (8 - len(searchmark[i,j])))
            )
            output2 = (
                str(x[j + 1] + " " * 7)
                if x[j + 1] != "0"
                else searchmark[i,j+1]
                + str(" " * (8 - len(searchmark[i,j+1])))
            )
            output3 = (
                str(x[j + 2] + " " * 7 + "|")
                if x[j + 2] != "0"
                else searchmark[i,j+2]
                + " " * (8 - len(searchmark[i,j+2]))
                + "|"
            )
            print(output1, output2, output3, end="")
        print()
        i+=1
    print(str("." + "-" * (2 * gap) + "") * 3 + ".")

def Marks():
    markers=dict()
    for i in range(9):
        for j in range(9):
            if sudokuproblem[i*9+j]=='0':
                markers.update({(i,j):Marking(i,j)})
            else:
                markers.update({(i,j):str(sudokuproblem[i*9+j])})
    CmdMarking(ToBoard(),markers)

if __name__=='__main__':
    Marks()
