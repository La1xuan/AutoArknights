import time
from androidController import tap, matchImg, waitingFor, failSafe, timeoutSetting


def BaseClear():
    waitingFor("Base")
    cur = 0
    while (matchImg("BaseCollectSymbol") == (0, 0)):
        print("Continue Searching For: " + "BaseCollectSymbol")
        tap(1504, 178)
        time.sleep(1)
        if cur > timeoutSetting:
            failSafe()
        cur += 1
    for _ in range(20):
        tap(260, 860)
        time.sleep(0.5)
    return