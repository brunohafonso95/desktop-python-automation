class Home: 
    def __init__(self, app):
        self.app = app

    def clicar_item_menu(self):
        self.app.elemento_list('PROJECTS', 'name', 0).click()
  
