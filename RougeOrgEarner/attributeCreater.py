import json
import pyautogui

attributes = [1008]

attributes.append(pyautogui.prompt("Enumtor Address"))
print(attributes)

f = open("Assets\\attributes.json", "w+")
f.write(json.dumps(attributes))
f.close()