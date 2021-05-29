# Assignment 3-Or TOOLS

**:point_right:pip install ortools**

**:point_right:[string iteration](1/strgnread.py)**

![sudokuimage](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/1200px-Sudoku-by-L2G-20050714.svg.png)

**Το Σουντόκου είναι παζλ που βασίζεται στη λογική. Στόχος είναι να συμπληρωθούν όλα τα κουτάκια στον πίνακα (9x9), ώστε κάθε στήλη, κάθε σειρά και κάθε κουτάκι 3x3 να περιέχουν όλα τα ψηφία από το 1 μέχρι το 9. Μερικά κουτάκια είναι ήδη συμπληρωμένα, ώστε να υπάρχει μόνο μία δυνατή λύση.
Το σουντόκου επινοήθηκε από τον Αμερικανό Χάουαρντ Γκαρνς το 1979 και δημοσιεύτηκε για πρώτη φορά από την εταιρεία Dell Magazines με το όνομα "Number Place".Έγινε δημοφιλές στην Ιαπωνία το 1986, όταν εκδόθηκε από τον οίκο Nikoli και δόθηκε το όνομα Sudoku. Έγινε μόδα ανά την υφήλιο το 2005.**

---
## RESOURCES

* [ΕΚΦΩΝΗΣΗ](https://chgogos.github.io/dituoi_agp/resources/agp_assignment20210515.pdf)
* [Sudoku Explanation](https://www.sudoku.name/rules/el)


## ΕΡΩΤΗΜΑΤΑ ΕΡΓΑΣΙΑΣ
* Εμφάνιση preview για sudoku:[data input](1/readdata.py)

    ```
        def Formatter(sudokustart):
            data=list()
            #15 χαρακτήρες η κάθε γραμμή
            #13 γραμμές συνολικά
            counter=9
            previouscounter=0
            while counter<=81:
                data.append(sudokustart[previouscounter:counter])
                previouscounter=counter
                counter+=9
            totallinelength=len(data[0])+4
            print(str('.'+'-'*6+'')*3,end='')
            print('.')
            counter=0
            for x in data:
                if counter%3==0 and counter!=0:
                    print(':',end='')
                    print('------ '*2,end='')
                    print('------:')
                print('|',end='')
                for j in range(0,len(x),3):
                    print(str(x[j]) if x[j]!='0' else '.',str(x[j+1]) if x[j+1]!='0' else '.',str(x[j+2]) if x[j+2]!='0' else '.','|',end='')
                print()
                counter+=1
            print(str('.'+'-'*6+'')*3+'.')

    def main():
        sudokustart=''
        if len(sys.argv)!=2:
            with open(default,'r') as F:
                sudokustart=F.readline().strip()
        else:
            sudokustart=sys.argv[1]
        if len(sudokustart)!=81:
            with open(default,'r') as F:
                sudokustart=F.readline().strip()
        Formatter(sudokustart=sudokustart) 
    ```

    * Αποτέλεσμα
        
        ![ResourceOut](RESOURCES/sudoku.png)

    <br><br>

* Pencil Mark:[pencil mark](Solution/PencilMark.py)
    ```
        from readdatatemplate import StringRead
        from functools import reduce

        class square:
            def __init__(self):
                self.container=list()
                self.marks=dict()

            def AppendRow(self,row):
                self.container.append(row)

            def __str__(self):
                strng=''
                for x in self.container:
                    strng+=x+'\n'
                return strng

            def Marking(self,linestr,columnstr):
                pass

        class RCTuple:
            def __init__(self):
                self.textrow=''
                self.textcol=''

            def __str__(self):
                return f'RowText:{self.textrow}\nColumnText:{self.textcol}\n'

        class MarkingTuple:
            def __init__(self,r,c):
                self.row=r
                self.column=c
                self.numbers=list()

            def addMarker(self,num):
                self.numbers.append(num)

            def __str__(self):
                strng=f"Row:{self.row}\nColumn:{self.column}\n"
                for n in self.numbers:
                    strng+=f"Number:{n}\n"
                return strng



        # Functions for Data Spliting
        def MakeSquares(data):
            index=0
            counter=3
            squares=list()
            while index<7:
                asquare=None
                for l in range(len(data)):
                    if l%3==0:
                        if asquare!=None:
                            squares.append(asquare)
                        asquare=square()
                    asquare.AppendRow(''.join([data[l][x] for x in range(index,index+3)]))
                    if l==len(data)-1:
                        squares.append(asquare)

                index+=3
            return squares

        def MakeRowColumnMap(data):
            records=dict()
            for i in range(len(data)):
                for j in range(len(data[i])):
                    rec=RCTuple()
                    key=f'{i}-{j}'
                    rec.textrow=data[i]
                    rec.textcol=reduce(lambda y,x:y+x[j],data,'')
                    records.update({key:rec})
            return records

        def Marking(data):
            rclist=MakeRowColumnMap(data)
            squares=MakeSquares(data)
            squareid=dict()
            for i in range(len(squares)):
                squareid.update({i:squares[i]})
            squareindex=0
            columncount=3

            #Find Markings
            markings=list()
            availablenumbers=[chr(x) for x in range(48,58)]
            for i in range(len(data)):
                if i%3==0 and i!=0:
                    squareindex+=1
                tempid=squareindex
                for j in range(len(data[i])):
                    if j%3==0 and j!=0:
                        tempid+=3
                    key=f'{i}-{j}'
                    if data[i][j]=='0':
                        marker=MarkingTuple(i,j)
                        for l in availablenumbers:
                            if l not in str(squareid[tempid]) and l not in rclist[key].textrow and l not in rclist[key].textcol:    
                                marker.addMarker(l)
                        markings.append(marker)

            for marker in markings:
                print(str(marker))


        def main():
            data=StringRead()
            raw_data=''.join(data)
            print(raw_data)
            Marking(data)


        if __name__=='__main__':
            main()
    ```
* Pencil Mark-Εμφάνιση στην γραμμή εντολών:[Pencil Marking](Solution/PencilMark.py)

    ```
        import math

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


        def mark(sudokuString):
            # Δημιουργία κενού Dictionary
            markers = dict()
            # Εύρος 9 (Αριθμοί από 0 εώς 8)
            range9 = range(0, 9)
            # Αριθμοί από 1 εώς 9
            range1_10 = range(1, 10)

            # Αρχικά θέτω ότι όλα τα κελιά μπορούν να πάρουν όλους τους αριθμούς
            for row in range9:
                for column in range9:
                    for number in range1_10:
                        markers[row, column, number] = True

            # Στην συνέχεια περνάω από κάθε κελί και περιορίζω τους αριθμούς που μπορούν να πάρουν τα κελιά
            for row in range9:
                for column in range9:
                    # Εάν το κελί είναι συμπληρωμένο
                    if sudokuString[row * 9 + column] != "0":
                        # Μετατρέπω το αλφαριθμητικό σε integer
                        completedNumber = int(sudokuString[row * 9 + column])
                        # Το συγκεκριμένο κελί επειδή είναι ήδη συμπληρωμένο δέχεται μόνο την τιμή που έχει (Απαγορέυω όλους τους άλλους αριθμούς)
                        for number in range1_10:
                            if number != completedNumber:
                                markers[row, column, number] = False
                        # Απαγορεύω τον ίδιο αριθμό στα κελιά της ίδιας γραμμής
                        for bColumn in range9:
                            if bColumn != column:
                                markers[row, bColumn, completedNumber] = False
                        # Απαγορεύω τον ίδιο αριθμό στα κελιά της ίδιας στήλης
                        for bRow in range9:
                            if bRow != row:
                                markers[bRow, column, completedNumber] = False
                        # Απαγορεύω τον ίδιο αριθμό στα κελιά του ίδιου τετραγώνου:
                        for bRow in range9:
                            for bColumn in range9:
                                # Ελέγχω ότι δεν είμαι στο ήδη συμπληρωμένο κελί
                                if bRow != row or bColumn != column:
                                    # Χρησιμοποιόντας την ακέραια διαίρεση μπορώ να ελέγξω αν είμαι στο ίδιο τετράγωνο
                                    if bRow // 3 == row // 3 and bColumn // 3 == column // 3:
                                        markers[bRow, bColumn, completedNumber] = False
            return markers

        def FormatMarking(markers):
            newmarkers=dict()
            for i in range(0,9):
                for j in range(0,9):
                    newmarkers[i,j]="".join([str(number) for row,col,number in markers if row==i and col==j and markers[row,col,number]==True])
            return newmarkers        



        gap=13
        def CmdMarking(sudokustr):
            # markers-->dictionary
            # Start with printing results
            data=ToBoard(sudokustr)
            searchmark=FormatMarking(mark(sudokustr))
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



    ```

    * ΑΠΟΤΕΛΕΣΜΑΤΑ
        1. ΜΗ ΜΟΡΦΟΠΟΙΗΜΕΝΑ ΑΠΟΤΕΛΕΣΜΑΤΑ:[unformatted results](2/results.out)
        2. ΜΟΡΦΟΠΟΙΗΜΕΝΑ ΑΠΟΤΕΛΕΣΜΑΤΑ:[formatted results](2/resultsmarking.out)
    

* CpSolver Solution:[CpSat](Solution/solver.py)


    ```
        def SolveSudoku(data):
            #Η επίλυση θα γίνει με βάση τον πίνακα που κατασκευάστηκε στην συνάρτηση readData

            #Μήκος Πλέγματος περιοχής 3Χ3
            regsize=3
            maxval=len(data)
            #ΔΗΜΙΟΥΡΓΙΑ ΜΟΝΤΕΛΟΥ
            model=cp_model.CpModel()
            x=dict()
            for i in range(0,maxval):
                for j in range(0,len(data[i])):
                    if int(data[i][j])!=0:
                        # Κελιά τα οποία έχουν ήδη συμπληρωθεί
                        x[i,j]=int(data[i][j])
                    else:
                        x[i,j]=model.NewIntVar(1,maxval,f'x[{i},{j}]')
            
            #Περιορισμοί

            #-Διαφορετικά ψηφία ανά γραμμή
            for i in range(maxval):
                model.AddAllDifferent([x[i,j] for j in range(maxval)])

            #-Διαφορετικά ψηφία ανα στήλη
            for j in range(maxval):
                model.AddAllDifferent([x[i,j] for i in range(maxval)])

            #-Διαφορετικά ψηφία ανα πλέγμα
            for rowid in range(0,maxval,regsize):
                for colid in range(0,maxval,regsize):
                    model.AddAllDifferent([x[i,j] for j in range(colid,(colid+regsize)) for i in range(rowid,(rowid+regsize))]) 
            
            #Επίλυση Προβλήματος
            solver=cp_model.CpSolver()
            status=solver.Solve(model)
            result=''
            if status==cp_model.OPTIMAL:
                for rowid in range(maxval):
                    for colid in range(maxval):
                        result+=str(solver.Value(x[rowid,colid]))
            return result
    ```
    * ΑΠΟΤΕΛΕΣΜΑΤΑ
        1. ΑΠΟΤΕΛΕΣΜΑΤΑ ΣΕ TXT ΑΡΧΕΙΟ:[results txt](3/solveroutput.out)
        2. FORMATTED ΑΠΟΤΕΛΕΣΜΑΤΑ:[solver results](3/solverresults.out)

        ![cpsat results](3/solverresults.png)
    
<br><br>   

* Search For All Solutions
```
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
```


## ORTOOLS Examples
* [OR_TOOLS](https://github.com/vasnastos/AGP/tree/master/OR_TOOLS)
* [LATIN SQUARE](orToolsExamples/latinSquaresCpSat.ipynb)
* [NQUEENS](https://github.com/vasnastos/AGP/blob/master/OR_TOOLS/nqueens.py)
* [SUDOKU(4X4)](orToolsExamples/sudoku4x4.ipynb)

