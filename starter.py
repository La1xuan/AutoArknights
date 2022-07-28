from androidController import booting
from os import popen, path, getcwd

booting()
popen("start " + path.abspath(getcwd()) + "\\main.py")