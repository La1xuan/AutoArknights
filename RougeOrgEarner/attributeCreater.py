import json
import pyautogui

attributes = [1008]

attributes.append(pyautogui.prompt("Enumerator Address"))
print(attributes)

f = open("attributes.json", "w+")
f.write(json.dumps(attributes))
f.close()