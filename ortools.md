# ΠΑΡΑΔΕΙΓΜΑΤΑ ORTOOLS

* ΕΠΙΛΥΣΗ ΕΞΙΣΩΣΗΣ 

![intro prob](https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/introductionproblem.png?token=APD2HAJRFIP7CHUM3OCQE23AXMBOA)
        
```
          # ORtool CpSat επιλυτής
          from ortools.sat.python import cp_model
          # Μοντέλο
          model = cp_model.CpModel()
          # ΜΕΤΑΒΛΗΤΕΣ ΑΠΟΦΑΣΗΣ
          # x = ? y = ? z = ? -> x, y, z Μεταβλητές απόφασης (Decision Variables)
          # 9 >= x >= 1 -> Πεδίο ορισμού (Domain) της x [1, 9]
          # 8 > y >= 0 -> Πεδίο ορισμού (Domain) της y [0, 7]
          # 10 >= z >= 3 -> Πεδίο ορισμού (Domain) της z [3, 10]
          # x, y, z ∈ Z -> Οι μεταβλητές απόφασης είναι ακέραιες
          x = model.NewIntVar(1, 9, "x")
          y = model.NewIntVar(0, 7, "y")
          z = model.NewIntVar(3, 10, "z")
          # ΠΕΡΙΟΡΙΣΜΟΙ
          # x + y + z = 19
          # x + y = 15
          # x != y
          # z < y
          model.Add(x + y + z == 19)
          model.Add(x + y == 15)
          model.Add(x != y)
          model.Add(z < y)
          # Κλήση του επιλυτή
          solver = cp_model.CpSolver()
          status = solver.Solve(model)
          # Εκτύπωση του αποτελέσματος
          if status == cp_model.OPTIMAL:
              print("X = ", solver.Value(x))
              print("Y = ", solver.Value(y))
              print("Z = ", solver.Value(z))

          """
          RESULTS-->
            X =  9
            Y =  6
            Z =  4
          """

```

* Latin Squares Example

```
          from ortools.sat.python import cp_model
          # Μοντέλο
          model = cp_model.CpModel()

            # Μεταβλητές απόφασης
          cell00 = model.NewIntVar(1, 3, "cell00")
          cell01 = model.NewIntVar(1, 3, "cell01")
          cell02 = model.NewIntVar(1, 3, "cell02")
          cell10 = model.NewIntVar(1, 3, "cell10")
          cell11 = model.NewIntVar(1, 3, "cell11")
          cell12 = model.NewIntVar(1, 3, "cell12")
          cell20 = model.NewIntVar(1, 3, "cell20")
          cell21 = model.NewIntVar(1, 3, "cell21")
          cell22 = model.NewIntVar(1, 3, "cell22")

          # Περιορισμοί
          # Ήδη συμπληρωμένα κελιά
          model.Add(cell00 == 3)
          model.Add(cell10 == 1)
          model.Add(cell12 == 2)
          model.Add(cell22 == 3)

          ## Γραμμή 1
          model.Add(cell00 != cell01)
          model.Add(cell00 != cell02)
          model.Add(cell01 != cell02)

          ## Γραμμή 2
          model.Add(cell10 != cell11)
          model.Add(cell10 != cell12)
          model.Add(cell11 != cell12)

          ## Γραμμή 3
          model.Add(cell20 != cell21)
          model.Add(cell20 != cell22)
          model.Add(cell21 != cell22)

          ## Στήλη 1
          model.Add(cell00 != cell10)
          model.Add(cell00 != cell20)
          model.Add(cell10 != cell20)

          ## Στήλη 2
          model.Add(cell01 != cell11)
          model.Add(cell01 != cell21)
          model.Add(cell11 != cell21)

          ## Στήλη 3
          model.Add(cell02 != cell12)
          model.Add(cell02 != cell22)
          model.Add(cell12 != cell22)

          # Κλήση του επιλυτή
          solver = cp_model.CpSolver()
          status = solver.Solve(model)

```

**CODE WITH STYLE**

```
  # ORtool CpSat επιλυτής
  from ortools.sat.python import cp_model

  # Μοντέλο
  model = cp_model.CpModel()

  # Μεταβλητές απόφασης
  cells = dict()
  range3 = range(0, 3)

  for row in range3:
      for column in range3:
          cells[row, column] = model.NewIntVar(1, 3, f"cell{row}{column}")

  # Περιορισμοί
  # Ήδη συμπληρωμένα κελιά
  model.Add(cells[0, 0] == 3)
  model.Add(cells[1, 0] == 1)
  model.Add(cells[1, 2] == 2)
  model.Add(cells[2, 2] == 3)

  ## Όλα τα κελιά σε κάθε γραμμή έχουν διαφορετική τιμή
  for row in range3:
      model.AddAllDifferent(cells[row, column] for column in range3)

  ## Όλα τα κελιά σε κάθε στήλη έχουν διαφορετική τιμή
  for column in range3:
      model.AddAllDifferent(cells[row, column] for row in range3)

  # Κλήση του επιλυτή
  solver = cp_model.CpSolver()
  status = solver.Solve(model)

  # Εκτύπωση του αποτελέσματος
  if status == cp_model.OPTIMAL:
      for row in range3:
          print(
              solver.Value(cells[row, 0]),
              solver.Value(cells[row, 1]),
              solver.Value(cells[row, 2]),
          )
```

* Sudoku 4X4

```
        # ORtool CpSat επιλυτής
        from ortools.sat.python import cp_model

        # Μοντέλο
        model = cp_model.CpModel()

        # Μεταβλητές απόφασης
        cells = dict()
        range4 = range(0, 4)

        for row in range4:
            for column in range4:
                cells[row, column] = model.NewIntVar(1, 4, f"cell{row}{column}")

        # Περιορισμοί
        # Ήδη συμπληρωμένα κελιά
        model.Add(cells[0, 1] == 2)
        model.Add(cells[0, 2] == 3)
        model.Add(cells[1, 0] == 3)
        model.Add(cells[2, 1] == 1)
        model.Add(cells[3, 2] == 2)

        ## Όλα τα κελιά σε κάθε γραμμή έχουν διαφορετική τιμή
        for row in range4:
            model.AddAllDifferent(cells[row, column] for column in range4)

        ## Όλα τα κελιά σε κάθε στήλη έχουν διαφορετική τιμή
        for column in range4:
            model.AddAllDifferent(cells[row, column] for row in range4)

        ## Όλα τα κελιά σε κάθε εσωτερικό τετράγωνο έχουν διαφορετική τιμή
        for rowid in range(0,4,2):
            for colid in range(0,4,2):
                model.AddAllDifferent([cells[i,j] for j in range(colid,(colid+2)) for i in range(rowid,(rowid+2))])

        # Κλήση του επιλυτή
        solver = cp_model.CpSolver()
        status = solver.Solve(model)

        # Εκτύπωση του αποτελέσματος
        if status == cp_model.OPTIMAL:
            for row in range4:
                print(
                    solver.Value(cells[row, 0]),
                    solver.Value(cells[row, 1]),
                    solver.Value(cells[row, 2]),
                    solver.Value(cells[row, 3]),
        
```

---

## ΧΡΗΣΙΜΟΙ ΣΥΝΔΕΣΜΟΙ
- [https://developers.google.com/optimization](https://developers.google.com/optimization)
- [https://google.github.io/or-tools/](https://google.github.io/or-tools/)
- [https://medium.com/google-or-tools/google-or-tools-a-guide-39f439a5cd0f](https://medium.com/google-or-tools/google-or-tools-a-guide-39f439a5cd0f)
- [https://www.ics.uci.edu/~dechter/courses/ics-275/fall-2020/slides/OR-Tools_CP-SAT_Solver_Tutorial.pdf](https://www.ics.uci.edu/~dechter/courses/ics-275/fall-2020/slides/OR-Tools_CP-SAT_Solver_Tutorial.pdf)


