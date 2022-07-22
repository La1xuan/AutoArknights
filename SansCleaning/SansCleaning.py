from time import sleep
from androidController import tap, tap2, matchImg, waitingFor, failSafe, timeoutSetting
def SansCleaning(status):
    status = int(status)
    cur = 0
    while (matchImg("Home") == (0, 0)):
        print("Continue Searching For: Home")
        tap(80, 50)
        sleep(1)
        cur += 1
    tap2(matchImg("Home"))

    cur = 0
    while (matchImg("Selection") == (0, 0)):
        if cur > timeoutSetting:
            failSafe()
        cur += 1
        print("Continue Searching For: Selection")
    sleep(1)
    tap(1400, 730)
    fight(status)

def fight(status):
    waitingFor("Ready")
    if CheckSans(status) == 0:
        return
    #waitingFor("Set")
    waitingFor("Ending", 10)
    sleep(2)
    tap2(matchImg("Ending"))
    fight(status)

def CheckSans(status,cur=0):
    #(1357, 713) use it
    #(978, 719) refuse
    #Modes:
    #0: Use Nothing
    #1: targeted for within a day
    #2: Use only within a week
    #3: Use only res
    #4: Use org
    #Red state is needed
    if cur > timeoutSetting:
        failSafe()
    if matchImg("Ready") != (0, 0):
        #Rare Case
        tap2(matchImg("Ready"))
        return CheckSans(status,cur=cur+1)
    if matchImg("Set") != (0, 0):
        tap2(matchImg("Set"))
        print("important Line executed")
        return 2
    if matchImg("WithinTwoDays") != (0, 0):
        if status > 0:
            tap(1357, 713)
            waitingFor("Ready")
            waitingFor("Set")
            return 1
    if matchImg("WithinTheWeek") != (0, 0):
        if status > 1:
            tap(1357, 713)
            waitingFor("Ready")
            waitingFor("Set")
            return 1
    if matchImg("UseBoost") != (0, 0):
        if status > 2:
            tap(1357, 713)
            waitingFor("Ready")
            waitingFor("Set")
            return 1
    if matchImg("BoostWithOrg") != (0, 0):
        if status > 3:
            tap(1357, 713)
            waitingFor("Ready")
            waitingFor("Set")
            return 1

    tap(978, 719)
    return 0