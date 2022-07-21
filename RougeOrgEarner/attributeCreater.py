from json import  loads, dumps
from pyautogui import prompt

f = open("attributes.json", "r")
attributes = loads(f.read())
f.close()
while len(attributes) < 4:
    attributes.append(0)
addr = (prompt("Enumerator Address \n Default to be Nonchanged."))
if addr != None:
    attributes[1] = addr
addr = (prompt("Sans Cleaning Mode: \n 0: Use Nothing \n 1: targeted for within 2 days \n 2: Use only within a week \n 3: Use only res \n 4: Use org"))
if addr != None:
    attributes[2] = addr
addr = (prompt("Shutdown after completing \n 0: Don\'t do that \n 1: Shutdown"))
if addr != None:
    attributes[3] = addr

print(attributes)

f = open("attributes.json", "w+")
f.write(dumps(attributes))
f.close()