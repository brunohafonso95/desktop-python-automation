
"""		Pyautomator Framework de teste 

			poc_itau"""

from Pyautomators.desk import Desk
from pages.pages.HomePage import Home
from Pyautomators import Log 
from time import sleep

Log.setup('log/report.log')

@Log.before_scenario
def before_scenario(context, scenario):
	context.app = Desk('C:/Users/bhenriquea/Desktop/xauthomation-win32-x64/xauthomation.exe', './driver/Winium.Desktop.Driver.exe')
	context.homePage = Home(context.app)

@Log.after_scenario
def after_scenario(context, scenario):
	context.app.fechar_programa()

