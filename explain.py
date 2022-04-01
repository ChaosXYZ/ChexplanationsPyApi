import engine
import random
import auxillary

def generate(FEN, Move):
    result = []
    positional = engine.explain(FEN)
    tactical = auxillary.tacticalExplain(FEN, Move)
    square = Move[2:4]
    pd = auxillary.pinsAndDiscoveries(FEN, square)
    doubleattacks = auxillary.detectDoubleAttacks(FEN, square)
    if doubleattacks != None:
        result += [doubleattacks]

    if len(pd) > 1:
        result += pd[0]
        
    return auxillary.paraform(result+tactical+positional)

def wrong(FEN, Move):
    result = []
    positional = engine.explain(FEN)
    tactical = auxillary.tacticalExplain(FEN, Move)
    square = Move[2:4]
    pd = auxillary.pinsAndDiscoveries(FEN, square)
    doubleattacks = auxillary.detectDoubleAttacks(FEN, square)
    if doubleattacks != None:
        result += [doubleattacks]

    if len(pd) > 1:
        result += pd[0]

    final = result+tactical+positional
    counter = len(final)
    while counter > 0:
        k = random.randint(0,10)
        if k > 5:
            final.pop(random.randrange(len(final)))
        counter -= 1
    newfinal = []
    for i in final:
        k = random.randint(0,10)
        if "attacks" in i and k > 5:
            i = i.replace("attacks", "defends")
        if "defends" in i and k > 5:
            i = i.replace("defends", "attacks")
        if "loses" in i and k > 5:
            i = i.replace("loses", "gains")
        if "white" in i and k > 5:
            i = i.replace("white", "black")
        if "black" in i and k > 5:
            i = i.replace("black", "white")
        newfinal.append(i)
    return auxillary.paraform(newfinal)
