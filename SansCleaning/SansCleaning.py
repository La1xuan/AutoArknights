import time
from androidController import tap, tap2, swipe, screenshot, matchImg, waitingFor
def SansCleaning(status):
    waitingFor("Home")
    while (matchImg("Selection") == (0, 0)):
        print("Continue Searching For: Selection")
    tap(1400, 730)
    fight(status)

def fight(status):
    waitingFor("Ready")
    ret = CheckSans(status)
    if ret == 0:
        return
    waitingFor("Set")
    waitingFor("Ending", 10)
    time.sleep(2)
    tap2(matchImg("Ending"))
    fight(status)

def CheckSans(status):
    #(1357, 713) use it
    #(978, 719) refuse
    #Modes:
    #0: Use Nothing
    #1: Unimplemented, targeted for within a day
    #2: Use only within a week
    #3: Use only res
    #4: Use org
    #Red state is needed
    if matchImg("Ready") != (0, 0):
        #Rare Case
        tap2(matchImg("Ready"))
        return CheckSans(status)
    if matchImg("Set") != (0, 0):
        return 2
    """
    if matchImg("WithinTheWeek") != (0, 0):
        if status > 0:
            tap(1357, 713)
            waitingFor("Ready")
            return 1
    """
    if matchImg("WithinTheWeek") != (0, 0):
        if status > 1:
            tap(1357, 713)
            waitingFor("Ready")
            return 1
    if matchImg("UseBoost") == (0, 0):
        if status > 2:
            tap(1357, 713)
            waitingFor("Ready")
            return 1
    if matchImg("BoostWithOrg") == (0, 0):
        if status > 3:
            tap(1357, 713)
            waitingFor("Ready")
            return 1

    tap(978, 719)
    return 0