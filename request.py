import requests

def sendRequest(FEN, move):
    BASE = "http://127.0.0.1:5000/"
    FEN = FEN.replace("/", "!")
    response = requests.get(BASE+"BestMove/"+FEN+"/"+move+"")
    print(response.json())
    
sendRequest("rn1q1rk1/pbp3bp/1p1p1n2/4ppB1/7P/2NP1N2/PPPQ1PP1/2KR1B1R w - - 0 11", "g5f6")
sendRequest("r1bq1rk1/ppp1bppp/2n5/4p1B1/4P1n1/2NP1N2/PPQ2PPP/2KR1B1R w - - 11 11", "g5d2")
