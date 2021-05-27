from pip._vendor import requests
from PencilMark import Marking
import math
import requests as reqs
from ortools.sat.python import cp_model

def Input(filename):
    # Here you will insert the sequences you want to use
    # File you can use https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokusequence.input?token=APD2HAL7LD3PY3ZC7HHFPV3AXBTJM
    data=reqs.get('https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokusequence.input?token=APD2HAL7LD3PY3ZC7HHFPV3AXBTJM').text
    return data.split('\n')

#Converts a sudoku sequence into a list
def ToBoard(rawdata:str)->list:
    if rawdata=='':
        return list()
    gridsize=int(math.sqrt(len(rawdata)))
    substrs=list()
    start=0
    next=gridsize
    while next<=len(rawdata):
      substrs.append(rawdata[start:next])
      start=next
      next+=gridsize
    return substrs

# Formats and display a preview into the cmd
def Formatter(data):
    if len(data)==0:
        return 0
    totallinelength = len(data[0]) + 4
    print(str("." + "-" * 6 + "") * 3, end="")
    print(".")
    counter = 0
    for x in data:
        if counter % 3 == 0 and counter != 0:
            print(":", end="")
            print("------ " * 2, end="")
            print("------:")
        print("|", end="")
        for j in range(0, len(x), 3):
            print(
                str(x[j]) if x[j] != "0" else ".",
                str(x[j + 1]) if x[j + 1] != "0" else ".",
                str(x[j + 2]) if x[j + 2] != "0" else ".",
                "|",
                end="",
            )
        print()
        counter += 1
    print(str("." + "-" * 6 + "") * 3 + ".")

#Displays the Pencil Mark
def pencilMark(data):
    Marking(data)


#Solve the sudoku Puzzle and return a string
def SolveSudoku(data):
    model=cp_model.CpModel()
    pos=dict()
    for x in range(len(data)):
        for j in range(len(data)):
            if int(data[x][j])!=0:
                pos[x,j]=int(data[x][j])
            else:
                pos[x,j]=model.NewIntVar(1,9,f'pos[{x}][{j}]')
    
    for i in range(len(data)):
        model.AddAllDifferent([pos[i,j] for j in range(len(data[i]))])

    for j in range(len(data)):
        model.AddAllDifferent([pos[i,j] for i in range(9)])
    
    for rowid in range(0,len(data),3):
        for colid in range(0,len(data),3):
            model.AddAllDifferent([pos[i,j] for j in range(colid,(colid+3)) for i in range(rowid,(rowid+3))])
    solver=cp_model.CpSolver()
    status=solver.Solve(model)
    result=''
    if status==cp_model.OPTIMAL:
       for i in range(len(data)):
           for j in range(len(data)):
               result+=str(solver.Value(pos[i,j]))
    return result

