from time import sleep
import easygui

class Home: 
    def __init__(self, context):
        self.context = context
        self.app = context.app

    def clicar_item_menu(self):
        path = self.context.path
        sleep(2) 
        coords = self.context.inspecionador.localliza_com_precisao(path + "data/images/java_project.PNG", 80)
        self.context.documentacao.print_local(int(coords[0])+150,int(coords[3])+50,int(coords[1])+150,int(coords[2])+50, path + 'docs/teste.PNG')
        texto = self.context.dados.tela_texto(int(coords[0]),int(coords[3]),int(coords[1]),int(coords[2]),True,190,64,False) 
        easygui.msgbox(texto, title="coordenadas")

