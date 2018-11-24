c = ["1","2","3","4","5","6","7","8","9"]
print "..!!.. Welcome To The Game ..!!.."
print "__________ TIC TAC TOE __________"
print "           -----------           "
p1=raw_input("Enter Player 1's Name :")
p2=raw_input("Enter Player 2's Name :")
print p1,"Choose Between X or O"
w=raw_input("Enter X or O : ")
if(w=='x' or w=='X'):
    print p2,"Got O"
    playerturn =1
elif(w=='o' or w=='O'):
    playerturn=0
    print p2,"Got X"
    (p1,p2)=(p2,p1)


end=1

def printg() :
    print "-------------"
    print '|', c[0], '|', c[1], '|', c[2], '|'
    print "----+---+----"
    print '|', c[3], '|', c[4], '|', c[5], '|'
    print "----+---+----"
    print '|', c[6], '|', c[7], '|', c[8], '|'
    print "-------------"

while end:
    printg()

    if playerturn==1 :
        print p1, "Choose Position Number"
    else :
        print p2, "Choose Position Number"

    try:
        c1=input("Enter the Position >> ")
    except:
        print "please enter a valid field"
        continue
    if(c1>9):
        print "Out of range"
        continue
    if c[c1-1]=='X' or c[c1-1]=='O':
        print "illegal move, plase try again"
        continue

    if playerturn==1 :
        c[c1-1]='X'

    else :
        c[c1-1]='O'


    playerturn = not playerturn
    count=0
    for a in range(9):
        if(c[a]=='X' or c[a]=='O'):
            count=count+1
    for x in range (0, 3) :
        y = x * 3
        if (c[y]==c[y+1] and c[y]==c[y+2]) :
            end =0
            printg()
        if (c[x]==c[x+3] and c[x]==c[x+6]) :
            end=0
            printg()

    if((c[0]==c[4] and c[0]==c[8]) or (c[2]==c[4] and c[4]==c[6])) :
        end=0
        printg()
    elif(count==9):
        count=count+1
        end=0
        printg()


if count==10:
    print "The Game ends in a tie"
elif playerturn==0:
    print p1,"Wins The Game!"
    print "Better Luck Next Time",p2
else:
    print p2,"Wins The Game!"
    print "Better Luck Next Time",p1

