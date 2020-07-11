from django.shortcuts import render
count=0
A={}

def home(request):
    return render(request,"home.html")


def game(request):
    global count
    count=0
    A.clear()
    return render (request,"game.html")


def validate(request,str):
    global count
    count+=1
    if A.get(str)=="P1" or A.get(str)=="P2":
        count+=1    
    elif(count%2)==0:
        A[str]="P2"
    else:
        A[str]="P1"
    if count==9:
        A["a"]="Game draw"
    if (A.get("A1")==A.get("A2")==A.get("A3")=="P1") or (A.get("A4")==A.get("A5")==A.get("A6")=="P1") or (A.get("A7")==A.get("A8")==A.get("A9")=="P1") or (A.get("A1")==A.get("A4")==A.get("A7")=="P1") or (A.get("A2")==A.get("A5")==A.get("A8")=="P1") or (A.get("A3")==A.get("A6")==A.get("A9")=="P1") or (A.get("A1")==A.get("A5")==A.get("A9")=="P1") or (A.get("A3")==A.get("A5")==A.get("A7")=="P1") :
        A["a"]="Player-1 win the match"
    elif (A.get("A1")==A.get("A2")==A.get("A3")=="P2") or (A.get("A4")==A.get("A5")==A.get("A6")=="P2") or (A.get("A7")==A.get("A8")==A.get("A9")=="P2") or (A.get("A1")==A.get("A4")==A.get("A7")=="P2") or (A.get("A2")==A.get("A5")==A.get("A8")=="P2") or (A.get("A3")==A.get("A6")==A.get("A9")=="P2") or (A.get("A1")==A.get("A5")==A.get("A9")=="P2") or (A.get("A3")==A.get("A5")==A.get("A7")=="P2") :
        A["a"]="Player-2 win the match"
    return render (request,"game.html",{'A':A})
    
