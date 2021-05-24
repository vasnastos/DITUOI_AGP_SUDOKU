import os
import sys
import math
from typing import List

default=os.path.join('','sudoku.sod')

def ToBoard(rawdata:str)->List:
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

def StringRead():
    sudokustart=''
    if len(sys.argv)!=2:
          with open(default,'r') as F:
              sudokustart=F.readline().strip()
    else:
          sudokustart=sys.argv[1]
    if len(sudokustart)!=81:
          with open(default,'r') as F:
              sudokustart=F.readline().strip()
    data = list()
        # 15 χαρακτήρες η κάθε γραμμή
        # 13 γραμμές συνολικά
    counter = 9
    previouscounter = 0
    while counter <= 81:
            data.append(sudokustart[previouscounter:counter])
            previouscounter = counter
            counter += 9
    return data

def main():
      sudokustart=StringRead()
      Formatter(sudokustart) 

#main()