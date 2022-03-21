import engine
import auxillary

def generate(FEN, Move):
    positional = engine.explain(FEN)
    tactical = auxillary.tacticalExplain(FEN, Move)
    square = Move[2:4]
    pd = auxillary.pinsAndDiscoveries(FEN, square)
    doubleattacks = auxillary.detectDoubleAttacks(FEN, square)
    if doubleattacks != None:
        print(doubleattacks)
    for i in tactical + pd + positional:
        print(i)
