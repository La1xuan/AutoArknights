from time import sleep
from androidController import tap, tap2, swipe, screenshot, matchImg

state = 0

Preset = [
    (1450, 750), 
    (1450, 750), 
    (1575, 785), 
    (1575, 785), 
    (1000, 785), 
    (1000, 785), 
    (440, 685),
    (1260, 520), 
    (1460, 835), 
    (1460, 835), 
    (780, 685),
    (750, 200),
    (1460, 835), 
    (1050, 685), 
    (1050, 685), 
    (750, 200),
    (1460, 835), 
    (1460, 835), 
    (1460, 835), 
    (1460, 550), 
    (480, 400),
    (480, 400),
    (1500, 530), 
    (250, 200),
    (750, 200),
    (1460, 835), 
    (1460, 780), 
    (1460, 780)]

def deploy(X, Y, dirX, dirY):
    tap(1500, 780)
    sleep(0.5)
    swipe(1500, 800, X, Y)
    swipe(X, Y, X + dirX * 300, Y + dirY * 300)
    tap(1175, 65)

#Fighting phase. 
def fight(num=0):
    if num > 10: #In case of timeout in a fight
        return

    #礼炮小队
    deploy(630, 425, -1, 0)

    #驯兽小屋
    deploy(400, 600, 1, 0)

    #意外
    deploy(900, 400, 1, 0)

    #与虫为伴
    deploy(900, 500, -1, 0)
    
    #划到战利品的最右侧
    swipe(1230, 425, 930, 425)
    tap(1175, 65)
    sleep(1)
    screenshot()

    res = matchImg("NoThanks", confidencevalue=0.8)
    if res == (0,0):
        res = matchImg("Failed", confidencevalue=0.9)
        if res != (0, 0):
            global state
            state = 1008
        else:
            fight(num + 1)
    else:
        print(res)
        tap2(res)
        sleep(5)
        tap(res[0] + 70 , res[1] + 245)

def postfight():
    if state == 0:
        sleep(10)
        randomPhase()

def randomPhase():
    screenshot()
    Phs2 = matchImg("Event")
    Phs3 = matchImg("Game")
    if Phs2 != (0,0) or Phs3 != (0, 0):
        if Phs3 != (0, 0):
            Phs2 = Phs3
        tap2(Phs2)
        sleep(5)
        for j in range(10):
            tap(1520, 615)
            sleep(0.5)
        for j in range(5):
            tap(1520, 509)
            sleep(0.5)
    else:
        Phs2 = matchImg("FightingHard")
        Phs3 = matchImg("Fighting")
        if Phs2 != (0,0) or Phs3 != (0, 0):
            if Phs3 != (0, 0):
                Phs2 = Phs3
                tap2(Phs2)
                sleep(5)
                tap(1520, 615)
                sleep(5)
                tap(1460, 780)
                sleep(13)
                tap(1375, 65) #二倍速
                sleep(3)
                fight(0)

def saving():
    if state == 0:
        tap(1075,400)
        sleep(5)
        tap(1520, 615)
        sleep(5)
        tap(630, 250)
        sleep(5)
        tap(820, 450)
        sleep(5)
        for j in range(20):
            tap(1230, 620)
            sleep(0.5)

def Introing():
    for i in Preset:
        sleep(4)
        tap2(i)

def RougeOrgEarner():
    while True:
        print("I am starting a new term")
        Introing()
        print("Getting in the first fight")
        sleep(13)
        tap(1375, 65) #二倍速
        sleep(3)
        fight()
        for i in range(5):
            postfight()
        
        #Phase Saving
        saving()

        #Phase quit
        print("Quiting")
        screenshot()
        state = 0
        if matchImg("QuitPrevent") == (0, 0):
            tap(50, 40)
            sleep(5)
            screenshot()
            while matchImg("Exit", confidencevalue=0.8) != (0, 0):
                print(matchImg("Exit", confidencevalue=0.8))
                tap2(matchImg("Exit", confidencevalue=0.8))
                sleep(5)
                screenshot()
            tap(1456, 431)
            sleep(5)
            tap(1050, 620)
            sleep(30)
            tap(800, 745)
            for j in range(10):
                tap(1000, 820)
                sleep(0.5)
        sleep(5)

#RougeOrgEarner()