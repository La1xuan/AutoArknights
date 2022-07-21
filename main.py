from androidController import recAtt
from SansCleaning.SansCleaning import SansCleaning
from RougeOrgEarner.RougeOrgEarner import RougeOrgEarner
from BaseClear.BaseClear import BaseClear
from Utilities.Utilities import intro, dailyCollection, outro, goingHome

intro()

BaseClear() 

goingHome()

SansCleaning(int(recAtt()[2]))

goingHome()

dailyCollection()

goingHome()

outro(int(recAtt()[3]))