import time
from androidController import tap, matchImg, waitingFor

def BaseClear():
    waitingFor("Base")
    while (matchImg("BaseCollectSymbol") == (0, 0)):
        print("Continue Searching For: " + "BaseCollectSymbol")
        tap(1504, 178)
        time.sleep(1)
    for _ in range(20):
        tap(260, 860)
    return