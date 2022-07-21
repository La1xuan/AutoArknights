from androidController import tap, tap2, swipe, screenshot, matchImg, waitingFor, recAtt
from SansCleaning.SansCleaning import SansCleaning
from RougeOrgEarner.RougeOrgEarner import RougeOrgEarner
from BaseClear.BaseClear import BaseClear
from time import sleep
from os import system, popen



#Preheat


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

BaseClear() 

#Going Home
while (matchImg("Home") == (0, 0)):
    tap(80, 50)
    sleep(0.5)


SansCleaning(recAtt()[2])


#Going Home
while (matchImg("Home") == (0, 0)):
    tap(80, 50)
    sleep(0.5)

#Collect Daily
sleep(5)
tap2(matchImg("Daily"))
waitingFor("CollectAll")



#Kill Leidian Player
sleep(5)
system("taskkill /f /im dnplayer.exe")

popen("shutdown -s -t 300")