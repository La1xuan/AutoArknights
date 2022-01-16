import pyautogui
import time
import os
from PIL import Image
import cv2
import aircv

running = True
enumeratorDir = "D:\\leidian\\LDPlayer4"
timeInbtwn = 3
currentScreen = "D:\\leidian\\LDPlayer4\\curScreen.png"
def tap(X,Y):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input tap " + str(X) + " " + str(Y))

def tap2(X):
    tap(X[0],X[1])

def swipe(X1, Y1, X2, Y2):
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input swipe " + str(X1) + " " + str(Y1) + str(X2) + " " + str(Y2))

def matchImg(imgobj,confidencevalue=0.93):
    imsrc = aircv.imread(currentScreen)
    imobj = aircv.imread("RougeOrgEarner\\" + imgobj + ".png")
    match_result = aircv.find_template(imsrc,imobj,confidencevalue)
    if match_result != None:
        return match_result["result"]

    else:
        return (0,0)

def checkState():
    stateNum = 0
    return stateNum

def fight(num):
    if num > 10:
        return
    tap(1500, 780)
    time.sleep(0.5)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1500 800 400 600") #驯兽小屋，
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 400 600 600 600")
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "tap 1175 65")

    tap(1500, 780)
    time.sleep(0.5)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1500 800 900 400") #意外
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 900 400 770 250")

    tap(1500, 780)
    time.sleep(0.5)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1500 800 900 500") #与虫为伴，done
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 900 500 640 500")
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "tap 1175 65")

    tap(1500, 780)
    time.sleep(0.5)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1500 800 630 425") #礼炮小队
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 630 425 930 425")
    

    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "tap 1175 65")
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1230 425 930 425")
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "tap 1175 65")

    time.sleep(1)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
    time.sleep(3)#扫描屏幕确认状态的时间
    res = matchImg("NoThanks", confidencevalue=0.8)
    if res == (0,0):
        res = matchImg("Failed", confidencevalue=0.9)
        if res != (0, 0):
            return 2
        return fight(num + 1)

    else:
        print(res)
        tap2(res)
        time.sleep(5)
        tap(res[0] + 70 , res[1] + 245)
    return 0

Preset = ["tap 1450 750", 
"tap 1450 750", 
"tap 1575 785", 
"tap 1575 785", 
"tap 1000 785", 
"tap 1000 785", 
"tap 440 685", 
"tap 1260 520", 
"tap 1460 835", 
"tap 1460 835", 
"tap 780 685", 
"tap 750 200", 
"tap 1460 835", 
"tap 1050 685", 
"tap 1050 685", 
"tap 750 200", 
"tap 1460 835", 
"tap 1460 835", 
"tap 1460 835", 
"tap 1460 550", 
"tap 480 400" ,
"tap 480 400", 
"tap 1500 530", 
"tap 250 200", 
"tap 750 200", 
"tap 1460 835", 
"tap 1460 780", 
"tap 1460 780"]

def prefight():
    for i in prefight:
        os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + i)
        time.sleep(4)
while running:
    """
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
"""
    print("Starting")

    for i in Preset:
        time.sleep(4)
        os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + i)
        


    time.sleep(13)
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input tap 1375 65") #二倍速
    time.sleep(5) 

    if fight(0) == 0:


        time.sleep(10)
        os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")

        time.sleep(3)#扫描屏幕确认状态的时间

        for i in range(5):
            os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
            time.sleep(3)#扫描屏幕确认状态的时间
            Phs2 = matchImg("Event")
            Phs3 = matchImg("Game")
            if Phs2 != (0,0) or Phs3 != (0, 0):
                if Phs3 != (0, 0):
                        Phs2 = Phs3
                print(Phs2)
                tap2(Phs2)
                time.sleep(5)
                for j in range(20):
                    tap(1520, 615)
                    time.sleep(0.5)
                for j in range(20):
                    tap(1520, 509)
                    time.sleep(0.5)
            else:
                Phs2 = matchImg("FightingHard")
                Phs3 = matchImg("Fighting")
                if Phs2 != (0,0) or Phs3 != (0, 0):
                    if Phs3 != (0, 0):
                        Phs2 = Phs3
                    print(Phs2)
                    tap2(Phs2)
                    time.sleep(5)
                    tap(1520, 615)
                    time.sleep(5)
                    tap(1460, 780)
                    time.sleep(10)
                    tap(1500, 780)
                    time.sleep(0.5)
                    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 1500 800 630 425") #礼炮小队
                    time.sleep(1)
                    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input " + "swipe 630 425 930 425")
                    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell input tap 1375 65") #二倍速
                    fight(0)

        #Phase Saving
        tap(1075,400)
        time.sleep(5)
        tap(1520, 615)
        time.sleep(5)
        tap(630, 250)
        time.sleep(5)
        tap(820, 450)
        time.sleep(5)
        for j in range(20):
            tap(1230, 620)
            time.sleep(0.5)

    #Phase Quit
    print("Quiting")
    os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
    time.sleep(3)#扫描屏幕确认状态的时间
    if matchImg("QuitPrevent") == (0, 0):
        tap(50, 40)
        time.sleep(5)
        print("scanning")
        os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
        time.sleep(3)#扫描屏幕确认状态的时间
        print(matchImg("Exit", confidencevalue=0.8))
        while matchImg("Exit", confidencevalue=0.8) != (0, 0):
            print(matchImg("Exit", confidencevalue=0.8))
            tap2(matchImg("Exit", confidencevalue=0.8))
            time.sleep(5)
            os.system("D:" + "&" + "cd " + enumeratorDir + "&" + "adb shell screencap //sdcard//curScreen.png & adb pull //sdcard//curScreen.png")
            time.sleep(3)#扫描屏幕确认状态的时间

        tap(1456, 431)
        time.sleep(5)
        tap(1050, 620)
        time.sleep(30)
        tap(800, 745)
        for j in range(10):
            tap(1000, 820)
            time.sleep(0.5)
    
    time.sleep(5)


    
    #os.system(str(Loc) + ":" + "&" + cding + "&" + settings)
# adb shell screencap /curScreen.png 
# adb shell input tap X Y 
# adb shell input swipe X1 Y1 X2 Y2 

