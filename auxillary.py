digits = ['1','2','3','4','5','6','7','8']
file2py = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
    }
py2file = ["a", "b", "c", "d", "e", "f", "g", "h"]
whitePieces = ["K", "P", "N", "B", "R", "Q"]
centralsquares = [[3,3],[3,4],[4,3],[4,4]]
pieceName = {
    "k": "black King",
    "n": "black Knight",
    "q": "black Queen",
    "r": "black Rook",
    "b": "black Bishop",
    "p": "black Pawn",
    "K": "white King",
    "N": "white Knight",
    "Q": "white Queen",
    "R": "white Rook",
    "B": "white Bishop",
    "P": "white Pawn"
    }
nameValues = {
    "black King": 99,
    "black Knight":3,
    "black Queen":8,
    "black Rook":5,
    "black Bishop":3,
    "black Pawn":1,
    "white King":99,
    "white Knight":3,
    "white Queen":8,
    "white Rook":5,
    "white Bishop":3,
    "white Pawn":1,
    }

def paraform(sentences):
    paragraph = ""
    for i in sentences:
        paragraph += i+"\n"
    return paragraph

def paraformN(sentences):
    paragraph = ""
    for i in sentences:
        paragraph += i+"\n"
    return paragraph

def virtualBoard(FEN):
    centralisation, kFlag = 0, 0
    boardLayout = FEN.split()[0]
    boardLayout = boardLayout.split('/')
    visualBoard = []
    #process FEN
    for i in range(0, 8):
        temp = [['']*int(x) if x in digits else x for x in boardLayout[i]]
        flat_temp = [item for sublist in temp for item in sublist]
        visualBoard.append(flat_temp)
    return visualBoard

def py2board(location):
    return py2file[int(location[1])]+str(8-location[0])

def movement(FEN, square, piece):
    #Location
    L = [8-int(square[1]),file2py[square[0]]]
    board = virtualBoard(FEN)
    #Extract Piece
    #piece = board[L[0]][L[1]]
    moves = []
    
    #PAWNS
    if piece == "P":
        if board[L[0]-1][L[1]] == "":
            moves += [[L[0]-1, L[1]]]
        moves += [[L[0]-1, L[1]+1],[L[0]-1, L[1]-1]]
    if piece == "p":
        if board[L[0]+1][L[1]] == "":
            moves += [[L[0]+1, L[1]]]
        moves += [[L[0]+1, L[1]+1],[L[0]+1, L[1]-1]]

    #Bishop
    if piece == "B" or piece == "b":
        
        #TOP RIGHT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1  and (L[1]+counter) < 8:
            moves += [[L[0]-counter, L[1]+counter]]
            lastpiece = board[L[0]-counter][L[1]+counter]
            counter += 1
            
        #TOP LEFT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1  and (L[1]-counter) > -1:
            moves += [[L[0]-counter, L[1]-counter]]
            lastpiece = board[L[0]-counter][L[1]-counter]
            counter += 1
            
        #BOTTOM LEFT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8  and (L[1]-counter) > -1:
            moves += [[L[0]+counter, L[1]-counter]]
            lastpiece = board[L[0]+counter][L[1]-counter]
            counter += 1

        #BOTTOM RIGHT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8  and (L[1]+counter) < 8:
            moves += [[L[0]+counter, L[1]+counter]]
            lastpiece = board[L[0]+counter][L[1]+counter]
            counter += 1

    #Rook
    if piece == "R" or piece == "r":
        
        #UP
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1:
            moves += [[L[0]-counter, L[1]]]
            lastpiece = board[L[0]-counter][L[1]]
            counter += 1
        #DOWN
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8:
            moves += [[L[0]+counter, L[1]]]
            lastpiece = board[L[0]+counter][L[1]]
            counter += 1
        #Left
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[1]-counter) > -1:
            moves += [[L[0], L[1]-counter]]
            lastpiece = board[L[0]][L[1]-counter]
            counter += 1

        #Right
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[1]+counter) < 8:
            moves += [[L[0], L[1]+counter]]
            lastpiece = board[L[0]][L[1]+counter]
            counter += 1
    #Queen
    if piece == "Q" or piece == "q":
        #UP
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1:
            moves += [[L[0]-counter, L[1]]]
            lastpiece = board[L[0]-counter][L[1]]
            counter += 1
        #DOWN
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8:
            moves += [[L[0]+counter, L[1]]]
            lastpiece = board[L[0]+counter][L[1]]
            counter += 1
        #Left
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[1]-counter) > -1:
            moves += [[L[0], L[1]-counter]]
            lastpiece = board[L[0]][L[1]-counter]
            counter += 1

        #Right
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[1]+counter) < 8:
            moves += [[L[0], L[1]+counter]]
            lastpiece = board[L[0]][L[1]+counter]
            counter += 1
            
        #TOP RIGHT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1  and (L[1]+counter) < 8:
            moves += [[L[0]-counter, L[1]+counter]]
            lastpiece = board[L[0]-counter][L[1]+counter]
            counter += 1
            
        #TOP LEFT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]-counter) > -1  and (L[1]-counter) > -1:
            moves += [[L[0]-counter, L[1]-counter]]
            lastpiece = board[L[0]-counter][L[1]-counter]
            counter += 1
            
        #BOTTOM LEFT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8  and (L[1]-counter) > -1:
            moves += [[L[0]+counter, L[1]-counter]]
            lastpiece = board[L[0]+counter][L[1]-counter]
            counter += 1

        #BOTTOM RIGHT
        lastpiece = ""
        counter = 1
        while lastpiece == "" and (L[0]+counter) < 8  and (L[1]+counter) < 8:
            moves += [[L[0]+counter, L[1]+counter]]
            lastpiece = board[L[0]+counter][L[1]+counter]
            counter += 1
    #Knight
    if piece == "N" or piece == "n":
        #UP and DOWN
        moves += [[L[0]-2, L[1]+1], [L[0]-2, L[1]-1]]
        moves += [[L[0]+2, L[1]+1], [L[0]+2, L[1]-1]]
        #RIGHT and LEFT
        moves += [[L[0]-1, L[1]-2], [L[0]+1, L[1]-2]]
        moves += [[L[0]-1, L[1]+2], [L[0]+1, L[1]+2]]
        #Getting rid of out of range moves
        moves = [i for i in moves if (i[0] < 8 and i[0] > -1 and i[1] < 8 and i[1] > -1)]

    #King
    if piece == "K" or piece =="k":
        #Orthogonal
        moves += [[L[0]+1, L[1]],[L[0]-1,L[1]],[L[0],L[1]+1],[L[0],L[1]-1]]
        #Diagonal
        moves += [[L[0]-1,L[1]-1],[L[0]-1,L[1]+1],[L[0]+1,L[1]-1],[L[0]+1,L[1]+1]]
        moves = [i for i in moves if (i[0] < 8 and i[0] > -1 and i[1] < 8 and i[1] > -1)]
    moves = [i for i in moves if (i[0] < 8 and i[0] > -1 and i[1] < 8 and i[1] > -1)]
    return moves
    

def attacking(FEN, square):
    board = virtualBoard(FEN)
    location = [8-int(square[1]),file2py[square[0]]]
    piece = board[location[0]][location[1]]
    attacklist = []
    if piece in whitePieces:
        colour = "w"
    else:
        colour = "b"
    #get possible moves
    movelist = movement(FEN, square, piece)
    if colour == "w":
        for i in movelist:
            if board[i[0]][i[1]] not in whitePieces and board[i[0]][i[1]] != "":
                attacklist += [[pieceName[board[i[0]][i[1]]], py2board(i)]]
            if i in centralsquares:
                attacklist += [['CENTER']]
    if colour == "b":
        for i in movelist:
            if board[i[0]][i[1]] in whitePieces and board[i[0]][i[1]] != "":
                attacklist += [[pieceName[board[i[0]][i[1]]], py2board(i)]]
            if i in centralsquares:
                attacklist += [['CENTER']]
    return attacklist

def detectDoubleAttacks(FEN, square):
    board = virtualBoard(FEN)
    piece = board[8-int(square[1])][file2py[square[0]]]
    pieceValue = nameValues[pieceName[piece]]
    attackList = attacking(FEN, square)
    attackList = [x for x in attackList if x != ['CENTER']]
    attackList = [x for x in attackList if nameValues[x[0]] > pieceValue]
    if len(attackList) > 1:
        return "This move attacks {0} higher value pieces simultaneously.".format(len(attackList))
    return None

def defending(FEN, square, piece, exclude = None):
    board = virtualBoard(FEN)
    location = [8-int(square[1]),file2py[square[0]]]
    #piece = board[location[0]][location[1]]
    defendlist = []
    if piece in whitePieces:
        colour = "w"
    else:
        colour = "b"
    movelist = movement(FEN, square, piece)
    if exclude != None:
        excludesquare = [8-int(exclude[1]),file2py[exclude[0]]]
        try:
            movelist.remove(excludesquare)
        except:
            pass
        
    if colour == "w":
        for i in movelist:
            if board[i[0]][i[1]] in whitePieces and board[i[0]][i[1]] != "":
                defendlist += [[pieceName[board[i[0]][i[1]]], py2board(i)]]
    if colour == "b":
        for i in movelist:
            if board[i[0]][i[1]] not in whitePieces and board[i[0]][i[1]] != "":
                defendlist += [[pieceName[board[i[0]][i[1]]], py2board(i)]]
    return defendlist


def pinMovement(FEN, square, piece):
    #Location
    L = [8-int(square[1]),file2py[square[0]]]
    board = virtualBoard(FEN)
    #Extract Piece
    #piece = board[L[0]][L[1]]
    moves = []


    #Bishop
    if piece == "B" or piece == "b":
        
        #TOP RIGHT
        lastpiece = []
        counter = 1
        moves1 = []
        while len(lastpiece) < 2  and (L[0]-counter) > -1  and (L[1]+counter) < 8:
            moves1 += [[L[0]-counter, L[1]+counter]]
            if board[L[0]-counter][L[1]+counter] != "":
                lastpiece += [board[L[0]-counter][L[1]+counter]]
            counter += 1
            
        #TOP LEFT
        lastpiece = []
        counter = 1
        moves2 = []
        while len(lastpiece) < 2 and (L[0]-counter) > -1  and (L[1]-counter) > -1:
            moves2 += [[L[0]-counter, L[1]-counter]]
            if board[L[0]-counter][L[1]-counter] != "":
                lastpiece += [board[L[0]-counter][L[1]-counter]]
            counter += 1
            
        #BOTTOM LEFT
        lastpiece = []
        counter = 1
        moves3 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8  and (L[1]-counter) > -1:
            moves3 += [[L[0]+counter, L[1]-counter]]
            if board[L[0]+counter][L[1]-counter] != "":
                lastpiece += [board[L[0]+counter][L[1]-counter]]
            counter += 1

        #BOTTOM RIGHT
        lastpiece = []
        counter = 1
        moves4 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8  and (L[1]+counter) < 8:
            moves4 += [[L[0]+counter, L[1]+counter]]
            if board[L[0]+counter][L[1]+counter] != "":
                lastpiece += [board[L[0]+counter][L[1]+counter]]
            counter += 1
        moves.append(moves1)
        moves.append(moves2)
        moves.append(moves3)
        moves.append(moves4)

    #Rook
    if piece == "R" or piece == "r":
        
        #UP
        lastpiece = []
        counter = 1
        moves1 = []
        while len(lastpiece) < 2 and (L[0]-counter) > -1:
            moves1 += [[L[0]-counter, L[1]]]
            if board[L[0]-counter][L[1]] != "":
                lastpiece += [board[L[0]-counter][L[1]]]
            counter += 1
        #DOWN
        lastpiece = []
        counter = 1
        moves2 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8:
            moves2 += [[L[0]+counter, L[1]]]
            if board[L[0]+counter][L[1]] != "":
                lastpiece += [board[L[0]+counter][L[1]]]
            counter += 1
        #Left
        lastpiece = []
        counter = 1
        moves3 = []
        while len(lastpiece) < 2 and (L[1]-counter) > -1:
            moves3 += [[L[0], L[1]-counter]]
            if board[L[0]][L[1]-counter] != "":
                lastpiece += [board[L[0]][L[1]-counter]]
            counter += 1

        #Right
        lastpiece = []
        counter = 1
        moves4 = []
        while len(lastpiece) < 2 and (L[1]+counter) < 8:
            moves4 += [[L[0], L[1]+counter]]
            if board[L[0]][L[1]+counter] != "":
                lastpiece += [board[L[0]][L[1]+counter]]
            counter += 1
            
        moves.append(moves1)
        moves.append(moves2)
        moves.append(moves3)
        moves.append(moves4)
    #Queen
    if piece == "Q" or piece == "q":
        #UP
        lastpiece = []
        counter = 1
        moves1 = []
        while len(lastpiece) < 2 and (L[0]-counter) > -1:
            moves1 += [[L[0]-counter, L[1]]]
            if board[L[0]-counter][L[1]] != "":
                lastpiece += [board[L[0]-counter][L[1]]]
            counter += 1
        #DOWN
        lastpiece = []
        counter = 1
        moves2 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8:
            moves2 += [[L[0]+counter, L[1]]]
            if board[L[0]+counter][L[1]] != "":
                lastpiece += [board[L[0]+counter][L[1]]]
            counter += 1
        #Left
        lastpiece = []
        counter = 1
        moves3 = []
        while len(lastpiece) < 2 and (L[1]-counter) > -1:
            moves3 += [[L[0], L[1]-counter]]
            if board[L[0]][L[1]-counter] != "":
                lastpiece += [board[L[0]][L[1]-counter]]
            counter += 1

        #Right
        lastpiece = []
        counter = 1
        moves4 = []
        while len(lastpiece) < 2 and (L[1]+counter) < 8:
            moves4 += [[L[0], L[1]+counter]]
            if board[L[0]][L[1]+counter] != "":
                lastpiece += [board[L[0]][L[1]+counter]]
            counter += 1

        moves.append(moves1)
        moves.append(moves2)
        moves.append(moves3)
        moves.append(moves4)
        #TOP RIGHT
        lastpiece = []
        counter = 1
        moves1 = []
        while len(lastpiece) < 2 and (L[0]-counter) > -1  and (L[1]+counter) < 8:
            moves1 += [[L[0]-counter, L[1]+counter]]
            if board[L[0]-counter][L[1]+counter] != "":
                lastpiece += [board[L[0]-counter][L[1]+counter]]
            counter += 1
            
        #TOP LEFT
        lastpiece = []
        counter = 1
        moves2 = []
        while len(lastpiece) < 2 and (L[0]-counter) > -1  and (L[1]-counter) > -1:
            moves2 += [[L[0]-counter, L[1]-counter]]
            if board[L[0]-counter][L[1]-counter] != "":
                lastpiece += [board[L[0]-counter][L[1]-counter]]
            counter += 1
            
        #BOTTOM LEFT
        lastpiece = []
        counter = 1
        moves3 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8  and (L[1]-counter) > -1:
            moves3 += [[L[0]+counter, L[1]-counter]]
            if board[L[0]+counter][L[1]-counter] != "":
                lastpiece += [board[L[0]+counter][L[1]-counter]]
            counter += 1

        #BOTTOM RIGHT
        lastpiece = []
        counter = 1
        moves4 = []
        while len(lastpiece) < 2 and (L[0]+counter) < 8  and (L[1]+counter) < 8:
            moves4 += [[L[0]+counter, L[1]+counter]]
            if board[L[0]+counter][L[1]+counter] != "":
                lastpiece += [board[L[0]+counter][L[1]+counter]]
            counter += 1
        moves.append(moves1)
        moves.append(moves2)
        moves.append(moves3)
        moves.append(moves4)
    return moves

def pinsAndDiscoveries(FEN, square):
    sentences = []
    pinList = []
    board = virtualBoard(FEN)
    L = [8-int(square[1]),file2py[square[0]]]
    piece = board[L[0]][L[1]]
    if piece not in ["r", "R", "q", "Q", "b", "B"]:
        return sentences
    movelist = pinMovement(FEN, square, piece)
    curatedList = []
    for i in movelist:
        if len([x for x in i if board[x[0]][x[1]] != ""]) == 2:
            curatedList.append([x for x in i if board[x[0]][x[1]] != ""])

    #checking for white perspective
    if piece in whitePieces:
        pieceValue = nameValues[pieceName[piece]]
        for i in curatedList:
            piece1 = board[i[0][0]][i[0][1]]
            piece2 = board[i[1][0]][i[1][1]]
            piece1Val = nameValues[pieceName[piece1]]
            piece2Val = nameValues[pieceName[piece2]]
            if piece1 not in whitePieces and piece2 == "k":
                #print("The {0} on {1} is strongly pinned to the {2} on {3}.".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1])))
                s_temp = "The {0} on {1} is strongly pinned to the {2} on {3}.".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1]))
                sentences.append(s_temp)
                pinList.append([[piece, square], [piece1, py2board(i[0])], [piece2, py2board(i[1])]])
            if piece1 not in whitePieces and piece2 not in whitePieces and piece2 != "k":
                if piece1Val < piece2Val:
                    #print("The {0} on {1} is pinned to the {2} on {3}".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1])))
                    s_temp = "The {0} on {1} is pinned to the {2} on {3}".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1]))
                    sentences.append(s_temp)
                    pinList.append([[piece, square], [piece1, py2board(i[0])], [piece2, py2board(i[1])]])
            if piece1 in whitePieces and piece2 not in whitePieces:
                if pieceValue < piece2Val:
                    #print("The {0} on {1} threatens a discovery on the {2} on {3} if the {4} on {5} were to be moved".format(pieceName[piece],square,pieceName[piece2],py2board(i[1]),pieceName[piece1],py2board(i[0])))
                    s_temp = "The {0} on {1} threatens a discovery on the {2} on {3} if the {4} on {5} were to be moved".format(pieceName[piece],square,pieceName[piece2],py2board(i[1]),pieceName[piece1],py2board(i[0]))
                    sentences.append(s_temp)
    #checking for black perspective
    if piece not in whitePieces:
        pieceValue = nameValues[pieceName[piece]]
        for i in curatedList:
            piece1 = board[i[0][0]][i[0][1]]
            piece2 = board[i[1][0]][i[1][1]]
            piece1Val = nameValues[pieceName[piece1]]
            piece2Val = nameValues[pieceName[piece2]]
            if piece1 in whitePieces and piece2 == "K":
                #print("The {0} on {1} is strongly pinned to the {2} on {3}.".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1])))
                s_temp = "The {0} on {1} is strongly pinned to the {2} on {3}.".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1]))
                sentences.append(s_temp)
                pinList.append([[piece, square], [piece1, py2board(i[0])], [piece2, py2board(i[1])]])
            if piece1 in whitePieces and piece2 in whitePieces and piece2 != "K":
                if piece1Val < piece2Val:
                    #print("The {0} on {1} is pinned to the {2} on {3}".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1])))
                    s_temp = "The {0} on {1} is pinned to the {2} on {3}.".format(pieceName[piece1], py2board(i[0]), pieceName[piece2], py2board(i[1]))
                    sentences.append(s_temp)
                    pinList.append([[piece, square], [piece1, py2board(i[0])], [piece2, py2board(i[1])]])
            if piece1 not in whitePieces and piece2 in whitePieces:
                if pieceValue < piece2Val:
                    #print("The {0} on {1} threatens a discovery on the {2} on {3} if the {4} on {5} were to be moved".format(pieceName[piece],square,pieceName[piece2],py2board(i[1]),pieceName[piece1],py2board(i[0])))
                    s_temp = "The {0} on {1} threatens a discovery on the {2} on {3} if the {4} on {5} were to be moved.".format(pieceName[piece],square,pieceName[piece2],py2board(i[1]),pieceName[piece1],py2board(i[0]))
                    sentences.append(s_temp)
    return [sentences, pinList]
                
                    
                
def doubled(FEN, move):
    old = move[0:2]
    to = move[2:4]
    board = virtualBoard(FEN)
    piece = board[8-int(to[1])][file2py[to[0]]]
        

def tacticalExplain(FEN, move):
    sentences = []
    old = move[0:2]
    to = move[2:4]
    board = virtualBoard(FEN)
    piece = board[8-int(to[1])][file2py[to[0]]]
    attackList = attacking(FEN, to)
    defendList = defending(FEN, to, piece)
    oldDefend = defending(FEN, old, piece, to)
    numberofcenters = attackList.count(['CENTER'])
    attackList = [x for x in attackList if x != ['CENTER']]
    oldDefend = [x for x in oldDefend if x not in defendList]
    if numberofcenters == 1:
        centers = "This move pressures 1 central square."
    else:  
        centers = "This move pressures {0} central squares.".format(numberofcenters)
    if numberofcenters > 0:
        sentences.append(centers)
    for i in attackList:
        temp = "This move attacks the {0} on {1}.".format(i[0], i[1])
        sentences.append(temp)
    for i in defendList:
        if i[0] == "white King" or i[0] == "black King":
            continue
        temp = "This move defends the {0} on {1}.".format(i[0], i[1])
        sentences.append(temp)
    for i in oldDefend:
        temp = "The {0} on {1} loses a defender.".format(i[0], i[1])
        sentences.append(temp)

    return sentences
    

def allPieceLocation(FEN):
    board = virtualBoard(FEN)
    pieceList = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != "":
                pieceList.append([board[i][j], py2board([i, j])])
    return pieceList

def allPins(FEN):
    pieceLocs = [i[1] for i in allPieceLocation(FEN)]
    allPins = []
    for i in pieceLocs:
        pins = pinsAndDiscoveries(FEN, i)
        if len(pins) > 0:
            allPins.append(pins[1])
    return [x for x in allPins if x != []]

def allAttacks(FEN):
    board = virtualBoard(FEN)
    pieces = allPieceLocation(FEN)
    attacks = []
    for i in pieces:
        attackList = attacking(FEN, i[1])
        for j in attackList:
            attacks.append(i+j)
    return attacks

def allDefends(FEN):
    board = virtualBoard(FEN)
    pieces = allPieceLocation(FEN)
    defends = []
    for i in pieces:
        defendList = defending(FEN, i[1], i[0])
        for j in defendList:
            defends.append(i+j)
    return defends

def SQ_attacks(FEN, square):
    sentences = []
    attacks = attacking(FEN, square)
    numberofcenters = attacks.count(['CENTER'])
    attacks = [x for x in attacks if x != ['CENTER']]
    if numberofcenters == 1:
        centers = "This move pressures 1 central square."
    else:  
        centers = "This move pressures {0} central squares.".format(numberofcenters)
    if numberofcenters > 0:
        sentences.append(centers)

    for i in attacks:
        temp = "This move attacks the {0} on {1}.".format(i[0], i[1])
        sentences.append(temp)
    return sentences

def SQ_defends(FEN, square, piece):
    sentences = []
    defends = defending(FEN, square, piece)
    for i in defends:
        if i[0] == "white King" or i[0] == "black King":
            continue
        temp = "This move defends the {0} on {1}.".format(i[0], i[1])
        sentences.append(temp)
    return sentences

def SQ_attacked(FEN, square):
    attackList = allAttacks(FEN)
    attackList = [x for x in attackList if x[2] != 'CENTER']
    sentences = []
    for i in attackList:
        if i[3] == square:
            temp = "This piece is attacked by the {0} on {1}.".format(pieceName[i[0]], i[1])
            sentences.append(temp)
    return sentences

def SQ_defended(FEN, square):
    defendList = allDefends(FEN)
    sentences = []
    for i in defendList:
        if i[3] == square:
            temp = "This piece is defended by the {0} on {1}.".format(pieceName[i[0]], i[1])
            sentences.append(temp)
    return sentences

def SQ_pins(FEN, square):
    pinList = allPins(FEN)
    sentences = []
    for i in pinList:
        if i[0][0][1] == square:
            temp = "This piece pins the {0} on {1} to the {2} on {3}.".format(pieceName[i[0][1][0]], i[0][1][1], pieceName[i[0][2][0]], i[0][2][1])
            sentences.append(temp)
        if i[0][1][1] == square:
            temp = "This piece is pinned to the {0} on {1} by the {2} on {3}.".format(pieceName[i[0][2][0]], i[0][2][1], pieceName[i[0][0][0]], i[0][0][1])
            sentences.append(temp)
    return sentences

def isPinned(FEN, square):
    pinList = allPins(FEN)
    sentences = []
    for i in pinList:
        if i[0][1][1] == square:
            temp = "However, this piece is pinned to the {0} on {1} by the {2} on {3}.".format(pieceName[i[0][2][0]], i[0][2][1], pieceName[i[0][0][0]], i[0][0][1])
            sentences.append(temp)
    if len(sentences) > 0:
        sentences.append("This means it might be not be able to perform its duties.")
    return sentences

def SQ_explain(FEN, square):
    board = virtualBoard(FEN)
    L = [8-int(square[1]),file2py[square[0]]]
    piece = board[L[0]][L[1]]
    attacks = SQ_attacks(FEN, square)
    defends = SQ_defends(FEN, square, piece)
    attacked = SQ_attacked(FEN, square)
    defended = []
    if piece != "K" or piece != "k":
        defended = SQ_defended(FEN, square)
    pins = SQ_pins(FEN, square)
    ispinned = isPinned(FEN, square)
    sentences = pins+attacks+attacked+defends+defended+ispinned
    for i in range(len(sentences)):
        if "move" in sentences[i]:
            sentences[i] = sentences[i].replace("move", "piece")
    return paraform(sentences)


