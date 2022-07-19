from androidController import tap, tap2, swipe, screenshot, matchImg, waitingFor
from SansCleaning.SansCleaning import SansCleaning
from RougeOrgEarner.RougeOrgEarner import RougeOrgEarner
from time import sleep



#Preheat

""""""
tap2(matchImg("Arknights"))

waitingFor("StartingScreen", 5)

waitingFor("Waking", 3)



SansCleaning(1)


#Going Home
while (matchImg("Home") == (0, 0)):
    tap(80, 50)
    sleep(0.5)


