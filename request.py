import requests

def sendRequest(option, FEN, move):
    BASE = "http://127.0.0.1:5000/"
    FEN = FEN.replace("/", "!")
    if option == "best":
        response = requests.get(BASE+"BestMove/"+FEN+"/"+move+"")
    else:
        response = requests.get(BASE+"Refute/"+FEN+"/"+move+"")
    print(response.json())
    
sendRequest("best", "rn1q1rk1/pbp3bp/1p1p1n2/4ppB1/7P/2NP1N2/PPPQ1PP1/2KR1B1R w - - 0 11", "g5f6")
sendRequest("best", "r1bq1rk1/ppp1bppp/2n5/4p1B1/4P1n1/2NP1N2/PPQ2PPP/2KR1B1R w - - 11 11", "g5d2")
sendRequest("refute", "r6r/1ppkq1Q1/p1n1pn2/3p4/3P4/2P1P3/PP3PPP/RN2K2R w KQ - 1 14", "g7g3")

