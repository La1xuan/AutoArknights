import aircv
import time
import os
import json
import sys
f = open("Assets\\attributes.json", "r")
att = json.loads(f.read())
f.close()
if att[0] != 1008:
    exit()
mytime = 0
enumeratorDir = att[1]

print(sys.argv)
print(len(sys.argv))
if len(sys.argv) == 2:
    prefix = "adb -s emulator-" + sys.argv[1] + " "
    curScreen = enumeratorDir + "\\curScreen" + sys.argv[1] + ".png"
    curs = "curScreen" + sys.argv[1] + ".png"
else:
    prefix = "adb "
    curScreen = enumeratorDir + "\\curScreen.png"
    curs = "curScreen.png"

state = True

Preset = [
[1450, 750], 
[1450, 750], 
[925, 785], 
[925, 785], 
[1000, 785], 
[1000, 785],

[440,  685], 
[1260, 350], #煌位置
[1460, 835], 
[1460, 835], 

[780,  685], 
[750,  200], 
[1460, 835], 
[1050, 685], 

[1050, 685], 
[750,  200], 
[1460, 835], 
[1460, 835], 

[1460, 835], 

[1460, 550],
[480,  400],
[480,  400]
]

fight1 = [
[480,  400], 
[1500, 530], 
[250,  200], 
[750,  200], 
[1460, 835], 
[1460, 780], 
[1460, 780]
]

depAtt = [0, 0, 0, 0]

#Helper functions, which controls aircv and adb shells.
def tap(X,Y):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + prefix + "shell input tap " + str(X) + " " + str(Y))

def tap2(X):
    tap(X[0],X[1])

def swipe(X1, Y1, X2, Y2):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + prefix + "shell input swipe " + str(X1) + " " + str(Y1) + " "  + str(X2) + " " + str(Y2))

def screenshot():
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + prefix + "shell screencap //sdcard//" + curs + " &" + prefix + "pull //sdcard//" + curs)
    time.sleep(3)

def matchImg(imgobj,confidencevalue=0.93):
    imsrc = aircv.imread(curScreen)
    imobj = aircv.imread("Assets\\" + imgobj + ".png")
    match_result = aircv.find_template(imsrc,imobj,confidencevalue)
    if match_result != None:
        return match_result["result"]
    else:
        return (0,0)

def selectMode():
    global depAtt
    screenshot()
    print("selecting")
    if matchImg("fire", confidencevalue=0.95) != (0, 0):
        #礼炮小队
        print("switching to fire")
        depAtt = [630, 425, -1, 0, "fire"]
    elif matchImg("house", confidencevalue=0.95) != (0, 0):
        #驯兽小屋
        print("switching to house")
        depAtt = [400, 600, 1, 0, "house"]
    elif matchImg("acc", confidencevalue=0.95) != (0, 0):
        #意外
        print("switching to acc")
        depAtt = [900, 400, 1, 0, "acc"]
    elif matchImg("with", confidencevalue=0.95) != (0, 0):
        #与虫为伴
        print("switching to with")
        depAtt = [900, 540, -1, 0, "with"]
    else:
        depAtt = [900, 540, -1, 0, "with"]
    return

def deploy(X, Y, dirX, dirY):
    tap(1500, 780)
    time.sleep(0.5)
    swipe(1500, 800, X, Y)
    swipe(X, Y, X + dirX * 300, Y + dirY * 300)
    tap(1175, 65)

#Fighting phase. 
def fight(num=0):
    if num > 15: #In case of timeout in a fight
        return
    deploy(depAtt[0], depAtt[1], depAtt[2], depAtt[3])
    print(depAtt[4])
    
    #划到战利品的最右侧
    swipe(1230, 425, 930, 425)
    tap(1175, 65)
    time.sleep(1)
    screenshot()

    res = matchImg("NoThanks", confidencevalue=0.8)
    if res == (0,0):
        res = matchImg("Failed", confidencevalue=0.9)
        if res != (0, 0):
            global state
            state = False
        else:
            fight(num + 1)
    else:
        print(res)
        tap2(res)
        time.sleep(5)
        tap(res[0] + 70 , res[1] + 245)

def postfight():
    if state:
        time.sleep(6)
        randomPhase()

def randomPhase():
    screenshot()
    Phs2 = matchImg("Game")
    Phs3 = matchImg("Event")
    if Phs2 != (0,0) or Phs3 != (0, 0):
        if Phs3 != (0, 0):
            Phs2 = Phs3
        tap2(Phs2)
        time.sleep(5)
        for j in range(10):
            tap(1520, 615)
            time.sleep(0.5)
        for j in range(5):
            tap(1520, 509)
            time.sleep(0.5)
    else:
        Phs2 = matchImg("FightingHard")
        Phs3 = matchImg("Fighting")
        if Phs2 != (0,0) or Phs3 != (0, 0):
            if Phs3 != (0, 0):
                Phs2 = Phs3
                tap2(Phs2)
                selectMode()
                time.sleep(5)
                tap(1520, 615)
                time.sleep(5)
                tap(1460, 780)
                time.sleep(13)
                tap(1375, 65) #二倍速
                time.sleep(3)
                fight(0)
                #TODO

def buyTarget():
    screenshot()
    target = matchImg("12", confidencevalue=0.94)
    if target == (0, 0):
        print("No Target Found")
        return False
    tap2(target)
    time.sleep(4)
    tap(1250, 630)
    time.sleep(4)
    print("Target Found")
    return True


def saving():
    if state:
        tap(1075,400)
        time.sleep(5)
        tap(1520, 615)
        time.sleep(5)
        while (buyTarget()):
            tap(750, 750)
        tap(630, 250)
        time.sleep(5)
        tap(820, 450)
        time.sleep(5)
        for j in range(20):
            tap(1230, 620)
            time.sleep(0.5)
        global mytime
        mytime += 1
        print("******************************************************************************")
        print(mytime)
        print("******************************************************************************")

def Introing():
    for i in Preset:
        time.sleep(4)
        tap2(i)
    selectMode()
    for i in fight1:
        time.sleep(4)
        tap2(i)

def quitting():
    global state
    print("Quiting")
    screenshot()
    state = True
    if matchImg("QuitPrevent") == (0, 0):
        tap(50, 40)
        time.sleep(5)
        screenshot()
        while matchImg("Exit", confidencevalue=0.8) != (0, 0):
            print(matchImg("Exit", confidencevalue=0.8))
            tap2(matchImg("Exit", confidencevalue=0.8))
            time.sleep(5)
            screenshot()
        tap(1456, 431)
        time.sleep(5)
        tap(1050, 620)
        time.sleep(20)
        tap(800, 745)
        for j in range(10):
            tap(1000, 820)
            time.sleep(0.5)
    time.sleep(5)
#screenshot()
#saving()
#tap(750, 650)
#buyTarget()
#exit()
while True:
    print("I am starting a new term")
    state = True
    Introing()
    print("Getting in the first fight")
    time.sleep(13)
    tap(1375, 65) #二倍速
    time.sleep(3)
    fight(0)
    for i in range(2):
        postfight()
    
    #Phase Saving
    saving()

    quitting()