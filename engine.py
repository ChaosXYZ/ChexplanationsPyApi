from stockfish import Stockfish
import ast
s = Stockfish("/Users/44751/Desktop/stockfish.exe")
s.set_skill_level(20)
wPieces = ["R", "B", "N", "Q", "K", "P"]
bPieces = ["r", "b", "n", "q", "k", "p"]
activeBlack = ["r","b","n","q"]
pieceValue = {
    "p":1,
    "k":0,
    "q":8,
    "n":3,
    "b":3,
    "r":5
    }
digits = ['1','2','3','4','5','6','7','8']
def returnBest(FEN, Move):
    """Returns the best move in response to a proposed move"""
    s.set_fen_position(FEN)
    s.make_moves_from_current_position([Move])
    return s.get_best_move()

def countPieces(FEN):
    """Auxillary Function to count material advantage"""
    boardLayout = FEN.split()[0]
    wCount = [x for x in boardLayout if x in wPieces]
    wnum = sum([pieceValue[x.lower()] for x in boardLayout if x in wPieces])
    bActive = sum([1 for x in boardLayout if x in activeBlack])
    bCount = [x for x in boardLayout if x in bPieces]
    bnum = sum([pieceValue[x.lower()] for x in boardLayout if x in bPieces])
    return [len(wCount), wnum, len(bCount), bnum, bActive, wnum-bnum]

def centralised(FEN):
    centralisation, kFlag = 0, 0
    boardLayout = FEN.split()[0]
    boardLayout = boardLayout.split('/')
    focusedArea = []
    for i in range(2, 6):
        temp = [['']*int(x) if x in digits else x for x in boardLayout[i]]
        flat_temp = [item for sublist in temp for item in sublist]
        focusedArea.append(flat_temp)
    #Outer Ring Calculation
    k = focusedArea
    for i in k[0][2:6]+k[3][2:6]+[k[1][2]]+[k[1][5]]+[k[2][2]]+[k[2][5]]:
        if i == "p":
            centralisation -= 1
        elif i in bPieces:
            centralisation -= 2
        if i == 'P':
            centralisation += 1
        elif i in wPieces:
            if i == "K":
                if countPieces(FEN)[4] > 3:
                    kFlag = 1
                    centralisation -= 1.5
                    #print("Slightly UNSAFE KING")
                if countPieces(FEN)[4] < 2:
                    kFlag = 3
                    centralisation += 0.5
                    #print("Slightly UNSAFE KING")
            centralisation += 2
    #Inner Center Calculation
    for i in k[1][3:5]+k[2][3:5]:
        if i == "p":
            centralisation -= 2
        elif i in bPieces:
            centralisation -= 5
        if i == 'P':
            centralisation += 2
        elif i in wPieces:
            if i == "K":
                if countPieces(FEN)[4] > 3:
                    kFlag = 2
                    centralisation -= 3
                    #print("UNSAFE KING")
                if countPieces(FEN)[4] < 2:
                    kFlag = 4
                    centralisation += 2
                    #print("UNSAFE KING")
        
            centralisation += 5

    if countPieces(FEN)[4] < 2 and "K" not in k[1][3:5]+k[2][3:5]+k[0][2:6]+k[3][2:6]+[k[1][2]]+[k[1][5]]+[k[2][2]]+[k[2][5]]:
        kFlag = 5
    return [centralisation, kFlag]
        

def refute(FEN, Move):
    moveList = []
    s.set_fen_position(FEN)
    s.make_moves_from_current_position([Move])
    evaluation = ast.literal_eval(str(s.get_evaluation()))['value']
    ply = 10
    checks = [0,0] #Material Difference, 
    while ply != 0 or 1 in checks:
        moveList.append(s.get_best_move())
        s.make_moves_from_current_position([s.get_best_move()])
        ply -= 1
    return ' '.join(moveList)

def explain(FEN):
    sentences = []
    if countPieces(FEN)[5] > 6: sentences.append('You have an overwhelming material advantage.')
    elif countPieces(FEN)[5] > 2: sentences.append('You have a strong material advantage.')
    elif countPieces(FEN)[5] > 0: sentences.append('You have a slight material advantage.')
    if countPieces(FEN)[5] < -6: sentences.append('You have an overwhelming material disadvantage.')
    elif countPieces(FEN)[5] < -2: sentences.append('You have a strong material disadvantage.')
    elif countPieces(FEN)[5] < 0: sentences.append('You have a slight material disadvantage.')

    cScore = centralised(FEN)
    if cScore[0] > 3: sentences.append("Your pieces are much better centralised.")
    elif cScore[0] > 0: sentences.append("You have slightly better central piece placement.")
    if cScore[0] < -3: sentences.append("Your opponents pieces are much better centralised.")
    elif cScore[0] < 0:sentences.append("Your opponent has slightly better central piece placement.")

    if cScore[1] == 1:sentences.append('Your king is slightly unsafe this close to the center')
    if cScore[1] == 2:sentences.append('Your king is unsafe in the center.')
    if cScore[1] == 3:sentences.append('Your king is slightly strong.')
    if cScore[1] == 4:sentences.append('You have a strong, active king for the endgame.')
    if cScore[1] == 5:sentences.append('You have an inactive king for the endgame.')

    return sentences
    
