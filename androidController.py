import os
import json
import aircv
import time
f = open("attributes.json", "r")
att = json.loads(f.read())
f.close()
if att[0] != 1008:
    exit()

enumeratorDir = att[1]
if (str(os.popen("tasklist").readlines()).find("dnplayer.exe") == -1):
    os.popen("D:" + "&" + "cd " + enumeratorDir + "&" + "start dnplayer.exe")
    time.sleep(30)
curScreen = enumeratorDir + "\\curScreen.png"

#Helper functions, which controls aircv and adb shells.
def tap(X,Y):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input tap " + str(X) + " " + str(Y))

def tap2(X):
    tap(X[0],X[1])

def swipe(X1, Y1, X2, Y2):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input swipe " + str(X1) + " " + str(Y1) + " "  + str(X2) + " " + str(Y2))

def screenshot():
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//Pictures//curScreen.png")

def matchImg(imgobj,confidencevalue=0.93):
    screenshot()
    imsrc = aircv.imread(curScreen)
    imobj = aircv.imread("Assets\\" + imgobj + ".png")
    match_result = aircv.find_template(imsrc,imobj,confidencevalue)
    if match_result != None:
        return match_result["result"]
    else:
        return (0,0)

def waitingFor(imgobj, length=1, cur=0):
    while (matchImg(imgobj) == (0, 0)):
        print("Continue Searching For: " + imgobj)
        time.sleep(length)
        cur += 1
        if cur > 100:
            return
    tap2(matchImg(imgobj))

#screenshot()
#print(matchImg("Banner"))
#tap(1357, 713)

