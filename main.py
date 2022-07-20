from androidController import tap, tap2, swipe, screenshot, matchImg, waitingFor
from SansCleaning.SansCleaning import SansCleaning
from RougeOrgEarner.RougeOrgEarner import RougeOrgEarner
from BaseClear.BaseClear import BaseClear
from time import sleep
from os import system



#Preheat


if(matchImg("Home") == (0, 0)):
    waitingFor("Arknights", 3)
    waitingFor("StartingScreen", 5)
    waitingFor("Waking", 3)



SansCleaning(2)


#Going Home
while (matchImg("Home") == (0, 0)):
    tap(80, 50)
    sleep(0.5)

#Collect Daily
sleep(5)
tap2(matchImg("Daily"))
waitingFor("CollectAll")

#BaseClear()

#Kill Leidian Player
system("taskkill /f /im dnplayer.exe")