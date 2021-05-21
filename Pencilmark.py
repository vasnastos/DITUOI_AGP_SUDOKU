from readdata import StringRead
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
    print(raw_data+'\n')
    Marking(data)
    
    
if __name__=='__main__':
    main()
