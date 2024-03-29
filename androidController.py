from os import popen, path, getcwd
from json import loads
from aircv import imread, find_template
from time import sleep
from pyautogui import confirm
from setting import setParam

f = open("attributes.json", "r")
att = loads(f.read())
f.close()
if att[0] != 1008:
    exit()

timeoutSetting = 100

enumeratorDir = att[1]

curScreen = enumeratorDir + "\\curScreen.png"

#Helper functions, which controls aircv and adb shells.
def tap(X,Y):
    popen("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input tap " + str(X) + " " + str(Y))

def tap2(X):
    tap(X[0],X[1])

def swipe(X1, Y1, X2, Y2):
    popen("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input swipe " + str(X1) + " " + str(Y1) + " "  + str(X2) + " " + str(Y2))

def screenshot():
    popen("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//Pictures//curScreen.png")
    sleep(1)

def matchImg(imgobj,confidencevalue=0.93):
    screenshot()
    imsrc = imread(curScreen)
    imobj = imread("Assets\\" + imgobj + ".png")
    match_result = find_template(imsrc,imobj,confidencevalue)
    if match_result != None:
        return match_result["result"]
    else:
        return (0,0)

def waitingFor(imgobj, length=1, cur=0):
    while (matchImg(imgobj) == (0, 0)):
        print("Continue Searching For: " + imgobj)
        sleep(length)
        cur += 1
        if cur > timeoutSetting:
            failSafe()
    tap2(matchImg(imgobj))

def failSafe():
    popen("taskkill /f /im dnplayer.exe")
    sleep(10)
    popen("start " + path.abspath(getcwd()) + "\\main.py")
    sleep(5)
    exit()


def recAtt():
    return att

def timeout():
    return timeoutSetting

def booting():
    global timeoutSetting, curScreen, enumeratorDir, att
    if (str(popen("tasklist").readlines()).find("dnplayer.exe") == -1):
        popen("D:" + "&" + "cd " + enumeratorDir + "&" + "start dnplayer.exe")
        sleep(3)
    res = confirm(text="Click OK if you want to change setting \n if you don't want to change setting, \n don't click until the enumerator is fully operational",timeout=60000)
    print(res)
    if res == "OK":
        setParam()
        f = open("attributes.json", "r")
        att = loads(f.read())
        f.close()
        enumeratorDir = att[1]
        curScreen = enumeratorDir + "\\curScreen.png"
        print(att)
    return

#failSafe()
#screenshot()
#print(matchImg("Dist1"))
#tap(1357, 713)
#booting()
