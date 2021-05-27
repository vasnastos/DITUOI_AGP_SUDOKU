from PencilMark import Marking
import math
from ortools.sat.python import cp_model

def Input(filename):
    # Here you will insert the sequences you want to use
    # File you can use https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokusequence.input?token=APD2HAL7LD3PY3ZC7HHFPV3AXBTJM
    return list()

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
    print('Solution for')
    print(data)
    return ''



