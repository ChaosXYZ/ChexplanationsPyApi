from stockfish import Stockfish
s = Stockfish("/Users/44751/Desktop/stockfish.exe")
s.set_skill_level(20)

def returnBest(FEN, Move):
    s.set_fen_position(FEN)
    s.make_moves_from_current_position([Move])
    return s.get_best_move()
