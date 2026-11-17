from outcome_finder import PossibleOutcomes

white = ["RK1","KN1","BS1","QN1","KG1","BS1","KN1","RK1","PN1","PN1","PN1","PN1","PN1","PN1","PN1","PN1"]
black = ["RK2","KN2","BS2","QN2","KG2","BS2","KN2","RK2","PN2","PN2","PN2","PN2","PN2","PN2","PN2","PN2"]

whitelost = []
blacklost = []

board8 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board7 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board6 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board5 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board4 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board3 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board2 = ["   ","   ","   ","   ","   ","   ","   ","   "]
board1 = ["   ","   ","   ","   ","   ","   ","   ","   "]


board8 = black[:8:]
board7 = black[8::]
board2 = white[8::]
board1 = white[:8:]

boardmain = []
boardmain.extend(board8)
boardmain.extend(board7)
boardmain.extend(board6)
boardmain.extend(board5)
boardmain.extend(board4)
boardmain.extend(board3)
boardmain.extend(board2)
boardmain.extend(board1)

boardmain[33] = "BS2"
boardmain[5] = "   "
boardmain[35] = "PN1"
boardmain[51] = "   "

def PrintMatLost(y):
    global whitelost,blacklost
    if y == "w":
        print("     White Materials Lost: ",end="")
        if not whitelost:
            print("None",end="")
        else:
            for x in whitelost:
                print(x,",",end="")
    elif y == "b":
        print("     Black Materials Lost: ",end="")
        if not blacklost:
            print("None",end="")
        else:
            for x in blacklost:
                print(x,",",end="")

def PrintWhite():
    def EmptyFill():
        print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
        print("  ┃----- ︳---- ︳---- ︳---- ︳---- ︳---- ︳---- ︳---- ︳")
        print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
    global boardmain
    print("      A     B      C      D     E      F      G     H")
    x = 8
    print("  ","━"*32)
    print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
    for i in range(0,64,8):
        print(x," ┃ ",end="",sep="")
        for y in range(i,i+8):
            print(boardmain[y]," ︳",end="",sep=" ")
        print(x,end='')
        if x == 5:
            PrintMatLost("w")
        elif x == 4:
            PrintMatLost("b")
        if i == 56:
            print()
            print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
            print("   ","━"*32,sep="")
        else:
            print()
            EmptyFill()
        x -= 1
    print("      A     B      C      D     E      F      G     H\n")

def PrintBlack():
    def EmptyFill():
        print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
        print("  ┃----- ︳---- ︳---- ︳---- ︳---- ︳---- ︳---- ︳---- ︳")
        print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
    global boardmain
    print("      A     B      C      D     E      F      G     H")
    boardmain = boardmain[::-1]
    x = 1
    print("  ","━"*32)
    print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
    for i in range(0,64,8):
        print(x," ┃ ",end="",sep="")
        for y in range(i,i+8):
            print(boardmain[y]," ︳",end="",sep=" ")
        print(x, end='')
        if x == 5:
            PrintMatLost("w")
        elif x == 4:
            PrintMatLost("b")
        if i == 56:
            print()
            print("  ┃      ︳     ︳     ︳     ︳     ︳     ︳     ︳     ︳")
            print("   ","━"*32,sep="")
        else:
            print()
            EmptyFill()
        x += 1
    print("      H     G      F      E     D      C      B     A\n")
    boardmain = boardmain[::-1]


while True:
    #WHITE TURN
    PrintWhite()

    print("TURN: White")

    while True: 

        #Input Move
        while True:
            movem = input("\nEnter move (__ to __) : ").upper()
            
            for i in range(0,movem.count(" ")):
                movem = movem.replace(" ","")
            
            movem = movem.split("TO")
            
            tomove = movem[0]
            tomove1 = ord(tomove[0])-65
            tomove2 = int(tomove[1])
            tomove = [tomove1,tomove2]
            tomoveval = boardmain[8*(9-tomove[1]) - (8 - tomove[0])]
            tomovepos = 8*(9-tomove[1]) - (8 - tomove[0])
            valid_tomove = tomove[0] < 8 and tomove[0] >= 0 and tomove[1] < 9 and tomove[1]

            move = movem[1]
            move1 = ord(move[0])-65
            move2 = int(move[1])
            move = [move1,move2]
            moveval = boardmain[8*(9-move[1]) - (8 - move[0])]
            movepos = 8*(9-move[1]) - (8 - move[0])
            valid_move = move[0] < 8 and move[0] >= 0 and move[1] < 9 and move[1] > 0

            if valid_tomove and valid_move:
                break
            else:
                print("Invalid Position")

        #Hypothetical Board
        boardtemp = boardmain.copy()
        boardtemp[movepos] = tomoveval
        boardtemp[tomovepos] = "   "

        whiteking = boardtemp.index("KG1")
        print("White King:", whiteking)

        blackall = {}
        whiteall = {}

        for i in range(0,len(boardtemp)):
            if boardtemp[i] in black:
                new = {}
                new[boardtemp[i]] = PossibleOutcomes(boardtemp[i],i,"black",boardtemp)
                for x in new:
                    if not new[x]:
                        new[x] = []
                for x in new:
                    if x in blackall:
                        blackall[x].extend(new[x])
                    else:
                        blackall[x] = new[x]
            elif boardtemp[i] in white:
                new = {}
                new[boardtemp[i]] = PossibleOutcomes(boardtemp[i],i,"white",boardtemp)
                for x in new:
                    if not new[x]:
                        new[x] = []
                for x in new:
                    if x in whiteall:
                        whiteall[x].extend(new[x])
                    else:
                        whiteall[x] = new[x]


        blackoutcomes = []
        whiteoutcomes = []
        for x in blackall:
            blackoutcomes.extend(blackall[x])
        for x in whiteall:
            whiteoutcomes.extend(whiteall[x])

        print("White Outcomes: ")
        for x in whiteall:
            print(x,whiteall[x])
        print("Black Outcomes: ")
        for x in blackall:
            print(x,blackall[x])

        # Checks
        if tomoveval in white:
            if moveval in black or moveval == "   ":
                outcomes = PossibleOutcomes(tomoveval,tomovepos,"white",boardmain)
                print("Outcomes: ",outcomes)
                if outcomes:
                    if movepos in outcomes:
                        if whiteking not in blackoutcomes:
                            if moveval in black:
                                blacklost.append(moveval)
                            boardmain[movepos] = tomoveval
                            boardmain[tomovepos] = "   "
                            break
                        else:
                            print("You've Been Checked/Pinned! Cant play that!")
                            print("Getting checked by:", end="")
                            for x in blackall:
                                moves = blackall[x]
                                if whiteking in moves:
                                    print(x, end="")
                            print()
                        
                    else:
                        print("Outcome not found")
                else:
                        print("Outcome not found")
            else:
                print("\nERROR: Cannot Take Your Own Pieces!")
        else:
            print("\nERROR: Thats not your piece!")


    #BLACK TURN
    PrintBlack()
    
    print("TURN: Black")

    while True:

        while True:
            movem = input("\nEnter move (__ to __) : ").split(" to ")

            tomove = (movem[0]).title()
            tomove1 = ord(tomove[0])-65
            tomove2 = int(tomove[1])
            tomove = [tomove1,tomove2]
            tomoveval = boardmain[8*(9-tomove[1]) - (8 - tomove[0])]
            tomovepos = 8*(9-tomove[1]) - (8 - tomove[0])

            move = (movem[1]).title()
            move1 = ord(move[0])-65
            move2 = int(move[1])
            move = [move1,move2]
            moveval = boardmain[8*(9-move[1]) - (8 - move[0])]
            movepos =  8*(9-move[1]) - (8 - move[0])
            if tomove[0] < 8 and tomove[0] >= 0 and tomove[1] < 9 and tomove[1] > 0 and move[0] < 8 and move[0] >= 0 and move[1] < 9 and move[1] > 0:
                break
            else:
                print("Invalid Position")

        boardtemp = boardmain.copy()
        boardtemp[movepos] = tomoveval
        boardtemp[tomovepos] = "   "

        blackking = boardtemp.index("KG2")
        print("Black King:", blackking)

        blackall = {}
        whiteall = {}

        for i in range(0,len(boardtemp)):
            if boardtemp[i] in black:
                new = {}
                new[boardtemp[i]] = PossibleOutcomes(boardtemp[i],i,"black",boardtemp)
                for x in new:
                    if not new[x]:
                        new[x] = []
                for x in new:
                    if x in blackall:
                        blackall[x].extend(new[x])
                    else:
                        blackall[x] = new[x]
            elif boardtemp[i] in white:
                new = {}
                new[boardtemp[i]] = PossibleOutcomes(boardtemp[i],i,"white",boardtemp)
                for x in new:
                    if not new[x]:
                        new[x] = []
                for x in new:
                    if x in whiteall:
                        whiteall[x].extend(new[x])
                    else:
                        whiteall[x] = new[x]


        blackoutcomes = []
        whiteoutcomes = []
        for x in blackall:
            blackoutcomes.extend(blackall[x])
        for x in whiteall:
            whiteoutcomes.extend(whiteall[x])
            
        print("White Outcomes: ")
        for x in whiteall:
            print(x,whiteall[x])
        print("Black Outcomes: ")
        for x in blackall:
            print(x,blackall[x])

        #Checks
        if tomoveval in black:
            if moveval in white or moveval == "   ":
                outcomes = PossibleOutcomes(tomoveval,tomovepos,"black",boardmain)
                print("Outcomes: ",outcomes)
                if outcomes:
                    if movepos in outcomes:
                        if blackking not in whiteoutcomes:
                            if moveval in white:
                                whitelost.append(moveval)
                            boardmain[movepos] = tomoveval
                            boardmain[tomovepos] = "   "
                            break
                        else:
                            print("You've Been Checked! Cant play that!")
                            print("Getting checked by:",end="")
                            for x in whiteall:
                                moves = whiteall[x]
                                if blackking in moves:
                                    print(x,end="")
                            print()

                    else:
                        print("Outcome not found")
                else:
                        print("Outcome not found")
            else:
                print("Cannot Take Your Own Pieces!")
        else:
            print("Thats not your piece!")
