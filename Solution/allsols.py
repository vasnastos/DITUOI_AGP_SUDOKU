from pip._vendor import requests
from ortools.sat.python import cp_model
import math

websource='https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokusequence.input?token=APD2HAJ7RZXJMQ67Q46LNQLAXMFH2'

def Input():
    data=requests.get(websource).text
    return data.split('\n')

def ToBoard(rawdata:str)->list:
    gridsize=int(math.sqrt(len(rawdata)))
    substrs=list()
    start=0
    next=gridsize
    while next<=len(rawdata):
      substrs.append(rawdata[start:next])
      start=next
      next+=gridsize
    return substrs

def Formatter(data):
        totallinelength = len(data[0])+4
        print(str('.'+'-'*6+'')*3, end='')
        print('.')
        counter = 0
        for x in data:
            if counter % 3 == 0 and counter != 0:
                print(':', end='')
                print('------ '*2, end='')
                print('------:')
            print('|', end='')
            for j in range(0, len(x), 3):
                print(str(x[j]) if x[j] != '0' else '.', str(x[j+1]) if x[j+1] !=
                      '0' else '.', str(x[j+2]) if x[j+2] != '0' else '.', '|', end='')
            print()
            counter += 1
        print(str('.'+'-'*6+'')*3+'.')

class SolverOutput(cp_model.CpSolverSolutionCallback):
    def __init__(self,variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables=variables
        self.__solution_count=0
    
    def on_solution_callback(self):
        self.__solution_count+=1
        result=''
        region=int(math.sqrt(len(self.__variables)))
        for i in range(region):
            for j in range(region):
                result+=str(self.Value(self.__variables[i,j]))
        Formatter(ToBoard(result))
        print()
    
    def Solution_Counter(self):
        return self.__solution_count




def SolveSudoku(data):
   model=cp_model.CpModel()
   cells=dict()
   for k in range(len(data)):
       for m in range(len(data[k])):
           if int(data[k][m])!=0:
               cells[k,m]=int(data[k][m])
           else:
               cells[k,m]=model.NewIntVar(1,9,f'Cell{k}{m}')
   for i in range(len(data)):
       model.AddAllDifferent([cells[i,j] for j in range(len(data))])
   
   for j in range(len(data)):
       model.AddAllDifferent([cells[i,j] for i in range(len(data))])
   region=int(math.sqrt(len(data)))
   for rowid in range(0,len(data),3):
       for colid in range(0,len(data),3):
           model.AddAllDifferent([cells[i,j] for j in range(colid,(colid+region)) for i in range(rowid,(rowid+region))])
   solver=cp_model.CpSolver()
   solveroutput=SolverOutput(cells)
   status=solver.SearchForAllSolutions(model,solveroutput)
   print(f'Status:{solver.StatusName(status)}')
   print(f'Number of Solutions:{solveroutput.Solution_Counter()}')

def main():
    data=Input()
    counter=1
    print('\t\tSolve Sudoku Using Ortools SoftWare')
    print('##'*60)
    for x in data:
        print(f'{counter}.')
        print(f'Sudoku Sequence:{x}')
        tempview=ToBoard(x)
        print('Preview')
        Formatter(tempview)
        print('\nSolutions')
        SolveSudoku(tempview)
        print('--'*20,end='\n\n')
        counter+=1
    
    print(f'\nData obtained from:{websource}')

if __name__=='__main__':
    main()

