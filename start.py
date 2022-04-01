from flask import Flask
from flask_restful import Api, Resource
import engine
import auxillary
import random
import explain
from stockfish import Stockfish
import ast
import sqlite3
import time
app = Flask(__name__)
api = Api(app)



class BestMove(Resource):
    def get(self, FEN, move):
        FEN = FEN.replace("!", "/")
        best = engine.returnBest(FEN, move)
        return {"Current FEN": FEN,
                "Move Played": move,
                "BestResponse": best}

class Best(Resource):
    def get(self, FEN):
        FEN = FEN.replace("!", "/")
        best = engine.bestMove(FEN)
        return {"Current FEN": FEN,
                "BestResponse": best}

class Refute(Resource):
    def get(self, FEN, move):
        FEN = FEN.replace("!", "/")
        best = engine.refute(FEN, move)
        return {"Current FEN": FEN,
                "Move Played": move,
                "Refutation": best}
class ExplainSquare(Resource):
    def get(self, FEN, square):
        FEN = FEN.replace("!", "/")
        text = auxillary.SQ_explain(FEN, square)
        return {"FEN": FEN,
                "Square": square,
                "explain": text}

class Explain(Resource):
    def get(self, FEN, Move):
        FEN = FEN.replace("!", "/")
        text = explain.generate(FEN, Move)
        return {"FEN": FEN,
                "Move": Move,
                "explain": text}
class Wrong(Resource):
    def get(self, FEN, Move):
        FEN = FEN.replace("!", "/")
        text = explain.wrong(FEN, Move)
        return {"FEN": FEN,
                "Move": Move,
                "explain": text}
class fetchPuzzle(Resource):
    def get(self):
        k = fetch(c)
        return {"FEN": k[0],
                "Move": k[1]}
class Check(Resource):
    def get(self, FEN, Move):
        k = puzzle.checkMistake(FEN, Move, c)
        return {"Result:" k}

def fetch(c):
    c.execute("SELECT * FROM Puzzles WHERE  Counter = 1")
    result = c.fetchall()
    string = "You played {}. This was a mistake, find the correct move.".format(random.choice(result)[1])
    return [random.choice(result)[0],string]
def run():
    fetch(c)
api.add_resource(BestMove, "/BestMove/<string:FEN>/<string:move>")
api.add_resource(Best, "/Best/<string:FEN>")
api.add_resource(Refute, "/Refute/<string:FEN>/<string:move>")
api.add_resource(ExplainSquare, "/ExplainSquare/<string:FEN>/<string:square>")
api.add_resource(Explain, "/Explain/<string:FEN>/<string:Move>")
api.add_resource(Wrong, "/Wrong/<string:FEN>/<string:Move>")
api.add_resource(Check, "/Check/<string:FEN>/<string:Move>")
api.add_resource(fetchPuzzle, "/Fetch/")

if __name__ == "__main__":
    global conn
    conn = sqlite3.connect('Puzzles.db')
    c = conn.cursor()
    try:
        createTable(c)
    except:
        pass
    run()
    app.debug = True
    app.run(host='10.204.199.233')
    
