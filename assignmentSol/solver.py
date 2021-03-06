from ortools.sat.python import cp_model

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

