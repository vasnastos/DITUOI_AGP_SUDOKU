def printMarkers(markers):
    range9 = range(0, 9)
    range1_10 = range(1, 10)
    for row in range9:
        for column in range9:
            print(f"Allowed in {row},{column} :", end=" ")
            for number in range1_10:
                if markers[row, column, number] == True:
                    print(number, end=" ")
            print()


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
    printMarkers(markers)


if __name__ == "__main__":
    sudoku = "200905006003000100070060050800602003006000200300709004040030010002000400100407008"
    mark(sudoku)