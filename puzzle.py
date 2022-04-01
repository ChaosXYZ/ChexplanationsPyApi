from stockfish import Stockfish
import ast
import sqlite3
s = Stockfish("/Users/44751/Desktop/stockfish.exe", depth=15)
s.set_skill_level(20)
def createTable(c):
    c.execute("""CREATE TABLE puzzles(
                FEN text,
                Move text,
                Counter integer
                )""")

def checkMistake(FEN, move, c):
    s.set_fen_position(FEN)
    boardval = ast.literal_eval(str(s.get_evaluation()))['value']
    s.make_moves_from_current_position([move])
    if boardval - ast.literal_eval(str(s.get_evaluation()))['value'] > 200:
        dbadd = "INSERT INTO Puzzles VALUES ('"+currpos+"', '"+move+"', 1)"
        c.execute(dbadd)
        return True
    return False
        
def fetchMistake(c):
    c.execute("SELECT * FROM Puzzles WHERE  Counter = 1")
    result = c.fetchall()
