white = ["RK1","KN1","BS1","QN1","KG1","BS1","KN1","RK1","PN1","PN1","PN1","PN1","PN1","PN1","PN1","PN1"]
black = ["RK2","KN2","BS2","QN2","KG2","BS2","KN2","RK2","PN2","PN2","PN2","PN2","PN2","PN2","PN2","PN2"]
boardmain = []
def WhiteKnight(pos):
    outcomes = []

    for i in range(1, -2, -2):
        b1 = ((pos - 8 * i) // 8) * 8
        b2 = ((pos - 16 * i) // 8) * 8

        # Up Right
        try:
            if boardmain[pos - 15 * i] not in white:
                if pos - 15 * i >= b2 and pos - 15 * i < b2 + 8:
                    outcomes.append(pos - 15 * i)
        except:
            pass

        # Up Left
        try:
            if boardmain[pos - 17 * i] not in white:
                if pos - 17 * i >= b2 and pos - 17 * i < b2 + 8:
                    outcomes.append(pos - 17 * i)
        except:
            pass

        # Low Right
        try:
            if boardmain[pos - 6 * i] not in white:
                if pos - 6 * i >= b1 and pos - 6 * i < b1 + 8:
                    outcomes.append(pos - 6 * i)
        except:
            pass

        # Low Left
        try:
            if boardmain[pos - 10 * i] not in white:
                if pos - 10 * i >= b1 and pos - 10 * i < b1 + 8:
                    outcomes.append(pos - 10 * i)
        except:
            pass
    return outcomes

def BlackKnight(pos):
    outcomes = []

    for i in [1, -1]:
        b1 = ((pos + 8 * i) // 8) * 8
        b2 = ((pos + 16 * i) // 8) * 8

        # Up Left
        try:
            if pos + 15 * i >= 0:
                if boardmain[pos + 15 * i] not in black:
                    if pos + 15 * i >= b2 and pos + 15 * i < b2 + 8:
                        outcomes.append(pos + 15 * i)
        except:
            pass

        # Up Right
        try:
            if pos + 17 * i >= 0:
                if boardmain[pos + 17 * i] not in black:
                    if pos + 17 * i >= b2 and pos + 17 * i < b2 + 8:
                        outcomes.append(pos + 17 * i)
        except:
            pass

        # Low Left
        try:
            if pos + 6 * i >= 0:
                if boardmain[pos + 6 * i] not in black:
                    if pos + 6 * i >= b1 and pos + 6 * i < b1 + 8:
                        outcomes.append(pos + 6 * i)
        except:
            pass

        # Low Left
        try:
            if pos + 10 * i >= 0:
                if boardmain[pos + 10 * i] not in black:
                    if pos + 10 * i >= b1 and pos + 10 * i < b1 + 8:
                        outcomes.append(pos + 10 * i)
        except:
            pass

    return outcomes

def WhiteKing(pos):
    outcomes = []
    # Upper and Lower
    for i in range(1, -2, -2):
        for y in range(7, 10):
            try:
                if boardmain[pos + y * i] not in white:
                    outcomes.append(pos + y * i)
            except:
                pass

    # Left and Right
    for i in range(-1, 2, 2):
        if boardmain[pos + i] not in white:
            outcomes.append(pos + i)
    return outcomes

def BlackKing(pos):
    outcomes = []

    # Upper and Lower
    for i in range(1, -2, -2):
        for y in range(7, 10):
            if pos + y * i >= 0:
                if boardmain[pos + y * i] not in black:
                    outcomes.append(pos + y * i)

    # Left and Right
    for i in range(-1, 2, 2):
        if boardmain[pos + i] not in black:
            outcomes.append(pos + i)

    return outcomes
def WhiteBishop(pos):
    outcomes = []

    # Upper Corners br-Right bl-Left
    br = bl = pos
    while (br + 1) % 8 != 0:
        br -= 7
    while bl % 8 != 0:
        bl -= 9

    # Upper Right Outcomes
    ye = 1
    while ye < 8:
        try:
            # If Piece is yours
            if boardmain[pos - 7 * ye] in white:
                break

            # If Black, add that only
            if boardmain[pos - 7 * ye] in black:
                outcomes.append(pos - 7 * ye)
                break

            # If outcome greater than corner, add
            if pos - 7 * ye >= br:
                outcomes.append(pos - 7 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Upper Left Outcomes
    ye = 1
    while ye < 8:
        try:
            # If Piece is yours
            if boardmain[pos - 9 * ye] in white:
                break

            # If Black, add that only
            if boardmain[pos - 9 * ye] in black:
                outcomes.append(pos - 9 * ye)
                break

            # If outcome greater than corner, add
            if pos - 9 * ye >= bl:
                outcomes.append(pos - 9 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Lower Corners br-Right bl-Left
    br = bl = pos
    while (br + 1) % 8 != 0:
        br += 9
    while bl % 8 != 0:
        bl += 7

    # Bottom Left
    ye = 1
    while ye < 8:
        try:
            if boardmain[pos + 7 * ye] in white:
                break

            if boardmain[pos + 7 * ye] in black:
                outcomes.append(pos + 7 * ye)
                break

            if pos + 7 * ye <= bl:
                outcomes.append(pos + 7 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Bottom Right
    ye = 1
    while ye < 8:
        try:
            if boardmain[pos + 9 * ye] in white:
                break

            if boardmain[pos + 9 * ye] in black:
                outcomes.append(pos + 9 * ye)
                break

            if pos + 9 * ye <= br:
                outcomes.append(pos + 9 * ye)
            else:
                break
        except:
            pass
        ye += 1
    return outcomes

def BlackBishop(pos):
    outcomes = []

    # Upper Corners br-Right bl-Left
    br = bl = pos
    while (br) % 8 != 0:
        br += 7
    while (bl + 1) % 8 != 0:
        bl += 9
    # Upper Right Outcomes
    ye = 1
    while ye < 8:
        try:
            # If Piece is yours
            if boardmain[pos + 7 * ye] in black:
                break

            # If Black, add that only
            if boardmain[pos + 7 * ye] in white:
                outcomes.append(pos + 7 * ye)
                break

            # If outcome  than corner, add
            if pos + 7 * ye <= br:
                outcomes.append(pos + 7 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Upper Left Outcomes
    ye = 1
    while ye < 8:
        try:
            # If Piece is yours
            if boardmain[pos + 9 * ye] in black:
                break

            # If Black, add that only
            if boardmain[pos + 9 * ye] in white:
                outcomes.append(pos + 9 * ye)
                break

            # If outcome less than corner, add
            if pos + 9 * ye <= bl:
                outcomes.append(pos + 9 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Lower Corners br-Right bl-Left
    br = bl = pos
    while br % 8 != 0:
        br -= 9
    while (bl + 1) % 8 != 0:
        bl -= 7

    # Bottom Left
    ye = 1
    while ye < 8:
        try:
            if pos - 7 * ye < 0:
                break
            if boardmain[pos - 7 * ye] in black:
                break

            if boardmain[pos - 7 * ye] in white:
                outcomes.append(pos - 7 * ye)
                break

            if pos - 7 * ye >= bl:
                outcomes.append(pos - 7 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # Bottom Right
    ye = 1
    while ye < 8:
        try:
            if pos - 9 * ye < 0:
                break
            if boardmain[pos - 9 * ye] in black:
                break

            if boardmain[pos - 9 * ye] in white:
                outcomes.append(pos - 9 * ye)
                break

            if pos - 9 * ye >= br:
                outcomes.append(pos - 9 * ye)
            else:
                break
        except:
            pass
        ye += 1

    return outcomes

def WhitePawn(pos):
    outcomes = []

    # Uppermost Position- bu
    bu = pos
    upperrow = [0, 1, 2, 3, 4, 5, 6, 7]
    while bu not in upperrow:
        bu -= 8

    if pos != bu:
        # Pawn Takes
        if boardmain[pos - 7] in black:
            outcomes.append(pos - 7)
        if boardmain[pos - 9] in black:
            outcomes.append(pos - 9)

        # Double Jump
        try:
            if boardmain[pos - 8] == "   " and boardmain[pos - 16] == "   ":
                if pos > 47 and pos < 56:
                    outcomes.append(pos - 16)
        except:
            pass

        # Normal Straight
        if boardmain[pos - 8] not in white:
            outcomes.append(pos - 8)
    return outcomes

def BlackPawn(pos):
    outcomes = []

    # Uppermost Position- bu
    bu = pos
    upperrow = [56, 57, 58, 59, 60, 61, 62, 63]
    while bu not in upperrow:
        bu += 8

    if pos != bu:
        # Pawn Takes
        if boardmain[pos + 7] in white:
            outcomes.append(pos + 7)
        if boardmain[pos + 9] in white:
            outcomes.append(pos + 9)

        # Double Jump
        try:
            if boardmain[pos + 8] == "   " and boardmain[pos + 16] == "   ":
                if pos > 7 and pos < 16:
                    outcomes.append(pos + 16)
        except:
            pass

        # Normal Straight
        if boardmain[pos + 8] not in black:
            outcomes.append(pos + 8)

    return outcomes

def WhiteRook(pos):
    outcomes = []

    bl = (pos // 8) * 8
    bu = pos
    while bu not in [0, 1, 2, 3, 4, 5, 6, 7]:
        bu -= 8
    # bottom- bu+56
    ye = 1

    # UP
    while pos - 8 * ye >= bu:
        try:
            if boardmain[pos - 8 * ye] in black:
                outcomes.append(pos - 8 * ye)
                break
            if boardmain[pos - 8 * ye] not in white:
                outcomes.append(pos - 8 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # DOWN
    ye = 1
    while pos + 8 * ye <= bu + 56:
        try:
            if boardmain[pos + 8 * ye] in black:
                outcomes.append(pos + 8 * ye)
                break
            if boardmain[pos + 8 * ye] not in white:
                outcomes.append(pos + 8 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # RIGHT
    ye = 1
    while pos + ye < bl + 8:
        try:
            if boardmain[pos + ye] in black:
                outcomes.append(pos + ye)
                break
            if boardmain[pos + ye] not in white:
                outcomes.append(pos + ye)
            else:
                break
        except:
            pass
        ye += 1

    # LEFT
    ye = 1
    while pos - ye >= bl:
        try:
            if boardmain[pos - ye] in black:
                outcomes.append(pos - ye)
                break
            if boardmain[pos - ye] not in white:
                outcomes.append(pos - ye)
            else:
                break
        except:
            pass
        ye += 1
    return outcomes

def BlackRook(pos):
    outcomes = []

    bl = (pos // 8) * 8
    bu = pos
    while bu not in [1, 0, 2, 3, 4, 5, 6, 7]:
        bu -= 8

    # UP
    ye = 1
    while pos + 8 * ye <= bu + 56:
        try:
            if boardmain[pos + 8 * ye] in white:
                outcomes.append(pos + 8 * ye)
                break
            if boardmain[pos + 8 * ye] not in black:
                outcomes.append(pos + 8 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # DOWN
    ye = 1
    while pos - 8 * ye >= bu:
        try:
            if boardmain[pos - 8 * ye] in white:
                outcomes.append(pos - 8 * ye)
                break
            if boardmain[pos - 8 * ye] not in black:
                outcomes.append(pos - 8 * ye)
            else:
                break
        except:
            pass
        ye += 1

    # RIGHT
    ye = 1
    while pos - ye >= bl:
        try:
            if boardmain[pos - ye] in white:
                outcomes.append(pos - ye)
                break
            if boardmain[pos - ye] not in black:
                outcomes.append(pos - ye)
            else:
                break
        except:
            pass
        ye += 1

    # LEFT
    ye = 1
    while pos + ye < bl + 8:
        try:
            if boardmain[pos + ye] in white:
                outcomes.append(pos + ye)
                break
            if boardmain[pos + ye] not in black:
                outcomes.append(pos + ye)
            else:
                break
        except:
            pass
        ye += 1

    return outcomes

def PossibleOutcomes(piece,pos,colour,temp):
    global white,black,boardmain
    boardmain = temp

    outcomes = []

    if colour == "white":
        if "QN" in piece:
            outcomes = WhiteKing(pos)
            outcomes.extend(WhiteBishop(pos))
            outcomes.extend(WhitePawn(pos))
            outcomes.extend(WhiteRook(pos))

        elif "KG" in piece:
            outcomes = WhiteKing(pos)

        elif "BS" in piece:
            outcomes = WhiteBishop(pos)

        elif "KN" in piece:
            outcomes = WhiteKnight(pos)

        elif "PN" in piece:
            outcomes = WhitePawn(pos)
            
        elif "RK" in piece:
            outcomes = WhiteRook(pos)
                    
    if colour == "black":

        if "QN" in piece:
            outcomes = BlackKnight(pos)
            outcomes.extend(BlackBishop(pos))
            outcomes.extend(BlackPawn(pos))
            outcomes.extend(BlackRook(pos))

        #King
        if "KG" in piece:
            outcomes = BlackKnight(pos)

        #Bishop
        if "BS" in piece:
            outcomes = BlackBishop(pos)

        if "KN" in piece:
            outcomes = BlackKnight(pos)

        if "PN" in piece:
            outcomes = BlackPawn(pos)
        
        if "RK" in piece:
            outcomes = BlackRook(pos)
    return outcomes
