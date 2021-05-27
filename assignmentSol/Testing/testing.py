import unittest as un
import sys
sys.path.append('..')
from sudoku import ToBoard,SolveSudoku

class test(un.TestCase):
    def testCase1(self):
        testSudoku='310004069000000200008005040000000005006000017807030000590700006600003050000100002'
        sudokuBoard = ToBoard(testSudoku)
        result = SolveSudoku(sudokuBoard)
        sudokuTest = verifySudoku(testSudoku, result)
        self.assertEqual(True,sudokuTest,msg=f"Error on sequence:{testSudoku}")
    
    def testSudokuFile(self):
        with open('testdata.txt','r') as S:
            for sudoku in S:
                sudoku=sudoku.strip()
                sudokuBoard=ToBoard(sudoku)
                result=SolveSudoku(sudokuBoard)
                solverresult=verifySudoku(sudoku,result)
                self.assertTrue(solverresult==True,msg='Error on Subsequence:{sudoku}') 

def verifySudoku(testSudoku, result):
    resultInt = []
    for i in range(0, len(testSudoku)):
        if int(testSudoku[i])!=0:
            if testSudoku[i]!=result[i]:
                return False

    for r in result:
        resultInt.append(int(r))

    for r in resultInt:
        if r < 1 or r > 9:
            return False
    counter=9
    previouscounter=0
    while counter<=len(resultInt):
        rowSet = set(resultInt[previouscounter:counter])
        if len(rowSet)!=9:
            return False
        previouscounter=counter
        counter+=9
    
    for j in range(0,9):
        resultsudoku=set()
        for i in range(0,9):
            resultsudoku.add(resultInt[i*9+j])
        if(len(resultsudoku)!=9):
            print(resultsudoku)
            return False

    resultset=list()
    resultset.append(set())
    resultset.append(set())
    resultset.append(set())
    counter=0
    for i in range(0,9):
        index=0
        for j in range(0,9,3):
          resultset[index].add(resultInt[i*9+j])
          resultset[index].add(resultInt[i*9+j+1])
          resultset[index].add(resultInt[i*9+j+2])
          index+=1
        if counter%3==0 and counter!=0:
            if len([1 for x in resultset if len(x)==9])!=3:
                return False
            for k in resultset:
                k.clear()
    return True

if __name__=='__main__':
    un.main()