import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        comandos_mysql = config.model_comandos_mysql.select_comandos().list() # Selecciona todos los registros de comandos_mysql
        return config.render.index(comandos_mysql) # Envia todos los registros y renderiza index.html
