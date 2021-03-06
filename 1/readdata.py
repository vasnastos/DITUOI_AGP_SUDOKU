import sys
import os
from webbrowser import open_new_tab

default=os.path.join('','sudokuinput.sod')

def HtmlPreview(sudokustart):
    data=list()
    #15 χαρακτήρες η κάθε γραμμή
    #13 γραμμές συνολικά
    counter=9
    previouscounter=0
    while counter<=81:
        data.append(sudokustart[previouscounter:counter])
        previouscounter=counter
        counter+=9
    htmlcode="""
    <html>
    <head>
    <title>
     Sudoku Start Preview
    </title>
    <style>
     table
     {
         width:auto;
         height:auto;
         font-size:17px;
         font-weight:bold;
         border:2px solid black;
     }
     
    #container
    {
        width:auto;
        height:auto;
    }

    #num
    {
       background-color:#93c989;
       width:30px;
    }
     #nah
     {
        background-color:grey;
        width:30px;
     }
     #hrtab
     {
         width:90px;
         height:2px;
         color:blue;
     }
     body
     {
         font-family:calibri;
     }
    </style>
    </head>
    <body>
    <center>
    <h1>Sudoku Preview</h1>
    """+f"""
    <b style="color:blue;">Input String:{''.join(data)}</b>
    <hr style=\"border-top:2px solid darkgreen;\">
    <table>
    """
    counter=0
    for x in data:
        if counter%3==0 and counter!=0:
           htmlcode+='<tr id=\"hrtab\"></tr>'
        htmlcode+="<tr id=\"container\">"
        for i in range(0,len(x),3):
            htmlcode+='<td id={}>{}</td><td id={}>{}</td><td id={}>{}</td>'.format("num" if x[i]!='0' else "nah",x[i] if x[i]!='0' else ' ',"num" if x[i+1]!='0' else "nah",x[i+1] if x[i+1]!='0' else ' ',"num" if x[i+2]!='0' else "nah",x[i+2] if x[i+2]!='0' else ' ')
        htmlcode+="</tr>"
        counter+=1
    htmlcode+="""
    </table>
    <br><br>
    </center>
    </body>
    </html>
    """
    with open('sudokupreview.html','w') as O:
        O.write(htmlcode)
    open_new_tab(os.path.join('','sudokupreview.html'))

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
    HtmlPreview(sudokustart=sudokustart)
    


if __name__=='__main__':
    main()
    
