
"""		Pyautomator Framework de teste 

			poc_itau"""

from Pyautomators.desk import Desk
from pages.pages.HomePage import Home
from Pyautomators import Log 
from Pyautomators import Ambiente
from Pyautomators import Inspecionador
from time import sleep
from Pyautomators import Documentacao
from Pyautomators import Dados

Log.setup('log/report.log')

@Log.before_scenario
def before_scenario(context, scenario):
	context.path = Ambiente.path_atual()
	context.inspecionador = Inspecionador
	context.documentacao = Documentacao
	context.dados = Dados
	context.app = Desk('C:/Users/bhenriquea/Desktop/xauthomation-win32-x64/xauthomation.exe', './driver/Winium.Desktop.Driver.exe')
	context.homePage = Home(context)

@Log.after_scenario
def after_scenario(context, scenario):
	sleep(3)
	context.app.fechar_programa()

