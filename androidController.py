import os
import json
import aircv
f = open("attributes.json", "r")
att = json.loads(f.read())
f.close()
if att[0] != 1008:
    exit()

enumeratorDir = att[1]
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

#screenshot()
#print(matchImg("Ending"))