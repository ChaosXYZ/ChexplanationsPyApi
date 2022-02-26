from flask import Flask
from flask_restful import Api, Resource
import engine


app = Flask(__name__)
api = Api(app)



class BestMove(Resource):
    def get(self, FEN, move):
        FEN = FEN.replace("!", "/")
        best = engine.returnBest(FEN, move)
        return {"Current FEN": FEN,
                "Move Played": move,
                "Best Response": best}

class Refute(Resource):
    def get(self, FEN, move):
        FEN = FEN.replace("!", "/")
        best = engine.refute(FEN, move)
        return {"Current FEN": FEN,
                "Move Played": move,
                "Refutation": best}

api.add_resource(BestMove, "/BestMove/<string:FEN>/<string:move>")
api.add_resource(Refute, "/Refute/<string:FEN>/<string:move>")


if __name__ == "__main__":
    app.run(debug=True)
    
