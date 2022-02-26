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

api.add_resource(BestMove, "/BestMove/<string:FEN>/<string:move>")


if __name__ == "__main__":
    app.run(debug=True)
    
