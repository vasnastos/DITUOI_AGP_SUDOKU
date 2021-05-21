from readdatatemplate import StringRead, Formatter
from functools import reduce
from pandas import DataFrame

gap = 13


class square:
    def __init__(self):
        self.container = list()
        self.marks = dict()

    def AppendRow(self, row):
        self.container.append(row)

    def __str__(self):
        strng = ""
        for x in self.container:
            strng += x + "\n"
        return strng

    def Marking(self, linestr, columnstr):
        pass


class RCTuple:
    def __init__(self):
        self.textrow = ""
        self.textcol = ""

    def __str__(self):
        return f"RowText:{self.textrow}\nColumnText:{self.textcol}\n"


class MarkingTuple:
    def __init__(self, r, c):
        self.row = r
        self.column = c
        self.numbers = list()

    def addMarker(self, num):
        self.numbers.append(num)

    def text(self):
        return "".join(self.numbers)

    def __str__(self):
        strng = f"Row:{self.row}\nColumn:{self.column}\n"
        for n in self.numbers:
            strng += f"Number:{n}\n"
        return strng


# Functions for Data Spliting
def MakeSquares(data):
    index = 0
    counter = 3
    squares = list()
    while index < 7:
        asquare = None
        for l in range(len(data)):
            if l % 3 == 0:
                if asquare != None:
                    squares.append(asquare)
                asquare = square()
            asquare.AppendRow("".join([data[l][x] for x in range(index, index + 3)]))
            if l == len(data) - 1:
                squares.append(asquare)

        index += 3
    return squares


def MakeRowColumnMap(data):
    records = dict()
    for i in range(len(data)):
        for j in range(len(data[i])):
            rec = RCTuple()
            key = f"{i}-{j}"
            rec.textrow = data[i]
            rec.textcol = reduce(lambda y, x: y + x[j], data, "")
            records.update({key: rec})
    return records


def Marking(data):
    rclist = MakeRowColumnMap(data)
    squares = MakeSquares(data)
    squareid = dict()
    for i in range(len(squares)):
        squareid.update({i: squares[i]})
    squareindex = 0
    columncount = 3

    # Find Markings
    markings = list()
    availablenumbers = [chr(x) for x in range(48, 58)]
    for i in range(len(data)):
        if i % 3 == 0 and i != 0:
            squareindex += 1
        tempid = squareindex
        for j in range(len(data[i])):
            if j % 3 == 0 and j != 0:
                tempid += 3
            key = f"{i}-{j}"
            if data[i][j] == "0":
                marker = MarkingTuple(i, j)
                for l in availablenumbers:
                    if (
                        l not in str(squareid[tempid])
                        and l not in rclist[key].textrow
                        and l not in rclist[key].textcol
                    ):
                        marker.addMarker(l)
                markings.append(marker)
    searchmark = dict()
    for marker in markings:
        searchmark.update({f"{marker.row}-{marker.column}": marker})
    return searchmark


def CmdMarking(data, searchmark):
    counter = 0
    # Start with printing results
    print(str("." + "-" * (2 * gap) + "") * 3 + ".")
    for x in data:
        if counter % 3 == 0 and counter != 0:
            print(":", end="")
            print(("-" * (2 * gap) + ":") * 2, end="")
            print("-" * (2 * gap) + ":")
        print("|", end="")
        for j in range(0, len(x), 3):
            output1 = (
                str(x[j] + " " * 7)
                if x[j] != "0"
                else searchmark[f"{counter}-{j}"].text()
                + str(" " * (8 - len(searchmark[f"{counter}-{j}"].text())))
            )
            output2 = (
                str(x[j + 1] + " " * 7)
                if x[j + 1] != "0"
                else searchmark[f"{counter}-{j+1}"].text()
                + str(" " * (8 - len(searchmark[f"{counter}-{j+1}"].text())))
            )
            output3 = (
                str(x[j + 2] + " " * 7 + "|")
                if x[j + 2] != "0"
                else searchmark[f"{counter}-{j+2}"].text()
                + " " * (8 - len(searchmark[f"{counter}-{j+2}"].text()))
                + "|"
            )
            print(output1, output2, output3, end="")
        print()
        counter += 1
    print(str("." + "-" * (2 * gap) + "") * 3 + ".")


def main():
    print("\t\tSudoku Game solution using OR_TOOLS")
    print("##" * 30)
    data = StringRead()
    raw_data = "".join(data)
    print("Data input:{}".format(raw_data))
    print("\nInput Analyse as rows")
    print("*" * 45)
    tableFrame = DataFrame(data, columns=["ROWS"])
    print(tableFrame, end="\n\n")
    print("\nSudoku Preview")
    Formatter(data)
    print("\n")
    print("\nSudoku Marking Preview")
    marks = Marking(data)
    CmdMarking(data, marks)


if __name__ == "__main__":
    main()
