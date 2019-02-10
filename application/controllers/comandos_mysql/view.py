import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, id_comando):  
        comandos_mysql = config.model_comandos_mysql.select_comando(id_comando) # Selecciona el registro que coincida con id_comando
        return config.render.view(comandos_mysql) # Envia el registro y renderiza view.html
