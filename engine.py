from stockfish import Stockfish
import ast
s = Stockfish("/Users/44751/Desktop/stockfish.exe")
s.set_skill_level(20)
pieces = ["r", "b", "n", "q", "k", "p", "R", "B", "N", "Q", "K", "P"]

def returnBest(FEN, Move):
    """Returns the best move in response to a proposed move"""
    s.set_fen_position(FEN)
    s.make_moves_from_current_position([Move])
    return s.get_best_move()

def countPieces(FEN):
    """Auxillary Function to detect how many pieces remain on the board"""
    boardLayout = FEN.split()[0]
    pieceCount = [x for x in boardLayout if x in pieces]
    return len(pieceCount)

def refute(FEN, Move):
    moveList = []
    s.set_fen_position(FEN)
    s.make_moves_from_current_position([Move])
    evaluation = ast.literal_eval(str(s.get_evaluation()))['value']
    ply = 10
    while ply != 0 or evaluation - ast.literal_eval(str(s.get_evaluation()))['value'] > 100:
        moveList.append(s.get_best_move())
        s.make_moves_from_current_position([s.get_best_move()])
        ply -= 1
    return moveList
