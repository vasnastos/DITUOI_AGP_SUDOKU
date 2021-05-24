import os
from datetime import datetime 
from core import *
from webbrowser import open_new_tab

def Sequences():
    filepath=os.path.join('','RESOURCES','sudokusequence.input')
    sequences=list()
    with open(filepath,'r') as F:
        sequences=F.readlines()
    code="""
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <style>
    body
    {
        font-family:calibri;
        font-size:18px;
        background-image:url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtxQGTa8IfQuFlvZg_iyFVOYgfzx39uoz3sg&usqp=CAU');
        background-repeat:no-repeat;
        background-size:cover;
        background-attachment:fixed;
    }
    img
    {
        width:75%;
        height:auto;
        border:2px solid;
    }
    .divsource
    {
        margin-left:15%;
        display:inline-block;
        width:40%;
        margin-right:20px;
    }
    table
    {
        width:40%;
        height:auto;
        border:2px solid blue;
        font-weight:bold;
        text-align:center;
        display:inline-block;
        margin-bottom:90px;
    }
    #fill
    {
      width:30px;
      color:black;
      border:1px solid red;
    }
    #empty
    {
       width:30px;
       background-color:grey;
       border:1px solid red;
    }
    .resultsource
    {
        display:inline-block;
        width:40%;
        text-align:left;
    }
    h1
    {
        color:black;
        font-weight:bold;
    }

    .fa-github
    {
        background-color:current;
        color:black;
    }

    .fa-github:hover
    {
        color:red;
        font-size:40px;
    }

    </style>
    </head>
    <body>
    <center>
    <h1>Sudoku Solver-Dit Agp Assignment<a href=\"https://chgogos.github.io/dituoi_agp/resources/agp_assignment20210515.pdf\"><i class=\"fa fa-github\"></i></a></h1>
    <img src=\"https://raw.githubusercontent.com/vasnastos/DITUOI_AGP_SUDOKU/main/RESOURCES/sudokucen.png?token=APD2HAMRFEXEN46E5XQNMP3AWSGN4\"/>
    <hr>
    <div style=\"text-align:left;\"><h2>Sudoku Sequences</h2>
    <ul>
    """
    for x in sequences:
        code+=f'<li>{x}</li>'
    code+='</ul><br><br><div style=\"text-align:left;\"><h2>Sudoku Results</h2></div><ul>'
    for k in sequences:
        print('\tSequence')
        print('**'*12)
        boardsequence=ToBoard(k)
        code+=f'<div style=\"text-align:left; margin-bottom:30px; font-size:19px; font-weight:bold;\"><li>Sequence:{k}</li></div><div class=\"divsource\"><table>'
        code+=Formatter(boardsequence)
        code+="</table></div>"
        code+="<div class=\"resultsource\"><br><table>"
        code+=Formatter(ToBoard(solver(boardsequence)))
        code+="</table></div>"
    code+="</center></body></html>"
    savepath=os.path.join('','RESOURCES','output.html')
    with open(savepath,'w') as F:
        F.write(code)
    open_new_tab(savepath)

if __name__=='__main__':
    start=datetime.now()
    Sequences()
    time=datetime.now()-start
    print('\nLapsed time:{}'.format(time))