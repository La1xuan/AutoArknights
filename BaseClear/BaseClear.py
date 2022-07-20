import time
from androidController import tap, tap2, swipe, screenshot, matchImg, waitingFor

def BaseClear():
    tap2(matchImg("Base"))
    return