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


