from androidController import tap, tap2, matchImg, waitingFor
from time import sleep
from os import popen
def intro():
    if(matchImg("Home") == (0, 0)):
        waitingFor("Arknights", 3)
        waitingFor("StartingScreen", 5)
        waitingFor("Waking", 3)

    #Dist1
    while (matchImg("Home") == (0, 0)):
        tap2(matchImg("Dist1"))
        tap2(matchImg("Dist2"))
        tap2(matchImg("Dist3"))

    sleep(2)
    while (matchImg("Home") == (0, 0)):
        tap2(matchImg("Dist1"))
        tap2(matchImg("Dist2"))
        tap2(matchImg("Dist3"))

def goingHome():
    #Going Home
    while (matchImg("Home") == (0, 0)):
        tap(80, 50)
        sleep(0.5)

def dailyCollection():
    #Collect Daily
    sleep(5)
    tap2(matchImg("Daily"))
    waitingFor("CollectAll")

def outro(exitCode=0):
    #Kill Leidian Player
    sleep(5)
    popen("taskkill /f /im dnplayer.exe")
    if (exitCode == 1):
        popen("shutdown -s -t 300")