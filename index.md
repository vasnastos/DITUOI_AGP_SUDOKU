# Assignment 3-Or TOOLS

## **ΣΗΜΑΝΤΙΚΑ**
   - !!!ΠΡΟΤΥΠΟ ΕΡΓΑΣΙΑΣ:<a href="http://algolab.dit.uoi.gr/DITUOI_AGP_SUDOKU/assignmentDitSudoku.zip"><img src="https://image.flaticon.com/icons/png/512/28/28814.png" width="25px" height="25px"/></a>-->ΚΩΔΙΚΟΣ:dituoiagp

   - ΟΔΗΓΙΕΣ ΕΓΚΑΤΑΣΤΑΣΗΣ ORTOOLS:[ortools_installation](installation.md)
[http://algolab.dit.uoi.gr/DITUOI_AGP_SUDOKU/assignmentDitSudoku.zip](http://algolab.dit.uoi.gr/DITUOI_AGP_SUDOKU/assignmentDitSudoku.zip)
![sudokuimage](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/1200px-Sudoku-by-L2G-20050714.svg.png)

**Το Σουντόκου είναι παζλ που βασίζεται στη λογική. Στόχος είναι να συμπληρωθούν όλα τα κουτάκια στον πίνακα (9x9), ώστε κάθε στήλη, κάθε σειρά και κάθε κουτάκι 3x3 να περιέχουν όλα τα ψηφία από το 1 μέχρι το 9. Μερικά κουτάκια είναι ήδη συμπληρωμένα, ώστε να υπάρχει μόνο μία δυνατή λύση.
Το σουντόκου επινοήθηκε από τον Αμερικανό Χάουαρντ Γκαρνς το 1979 και δημοσιεύτηκε για πρώτη φορά από την εταιρεία Dell Magazines με το όνομα "Number Place".Έγινε δημοφιλές στην Ιαπωνία το 1986, όταν εκδόθηκε από τον οίκο Nikoli και δόθηκε το όνομα Sudoku. Έγινε μόδα ανά την υφήλιο το 2005.**

---
## RESOURCES

* [ΕΚΦΩΝΗΣΗ](https://chgogos.github.io/dituoi_agp/resources/agp_assignment20210515.pdf)
* [Sudoku Explanation](https://www.sudoku.name/rules/el)
* [sudoku.sod](https://github.com/vasnastos/DITUOI_AGP_SUDOKU/blob/main/RESOURCES/sudoku.sod)


## ΕΡΩΤΗΜΑΤΑ ΕΡΓΑΣΙΑΣ
* Read Data input

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

        ![ResourceOut](https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudoku.png?token=APD2HAI6AXFWAGCI7ZUBHPTAXWVFA)

* Pencil Mark
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
       1. ΑΠΟΤΕΛΕΣΜΑΤΑ ΣΕ TXT:[txt results](https://github.com/vasnastos/DITUOI_AGP_SUDOKU/blob/main/2/results.out)
       2. ΑΠΟΤΕΛΕΣΜΑΤΑ (FORMATTED) ΣΕ TXT:[formatted results txt](https://github.com/vasnastos/DITUOI_AGP_SUDOKU/blob/main/2/resultsmarking.out)
       3. ΤΕΛΙΚΟ ΑΠΟΤΕΛΕΣΜΑ

           ![RESIMAGEGITHUBERROR](https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/maqrkingnums.png?token=APD2HAOG774EASTTIUWAIO3AWR3LA)
   
## ΕΠΙΛΥΣΗ SUDOKU
  * ΑΠΟΤΕΛΕΣΜΑΤΑ ΜΙΑΣ ΑΚΟΛΟΥΘΙΑΣ SUDOKU ΣΕ ΤΧΤ ΜΟΡΦΗ:[results txt](https://github.com/vasnastos/DITUOI_AGP_SUDOKU/blob/main/3/solverresults.out)
  * ΑΡΧΕΙΟ ΕΙΣΟΔΟΥ ΠΟΛΛΑΠΛΩΝ ΠΡΟΒΛΗΜΑΤΩΝ SUDOKU:[multiple inputs](https://github.com/vasnastos/DITUOI_AGP_SUDOKU/blob/main/RESOURCES/sudokusequence.input)
  * ΑΠΟΤΕΛΕΣΜΑ:[results.html](http://algolab.dit.uoi.gr/DITUOI_AGP_SUDOKU/)
  * ΤΕΛΙΚΑ ΑΠΟΤΕΛΕΣΜΑΤΑ:[Final results](https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/sequences.out?token=APD2HAN7BJ24LYMMQOA5B5TAXNQLA) 

## ΑΛΛΕΣ ΠΑΡΟΥΣΙΑΣΕΙΣ
  * [ORTOOLS EXAMPLES](ortools.md)



