import web
import config as config


class Delete:
    def __init__(self):
        pass

    def GET(self, id_comando): 
        comandos_mysql = config.model_comandos_mysql.select_comando(id_comando) # Selecciona el registro que coincida con id_comando
        return config.render.delete(comandos_mysql) # Envia el registro y renderiza delete.html
    
    def POST(self, id_comando):
        formulario = web.input() # Crea un objeto formuario con los datos enviados con el formulario
        id_comando = formulario['id_comando'] # Obtine el id_comando almacenado en el formulario
        config.model_comandos_mysql.delete_comando(id_comando) # Borra el registro del id_comando seleccionado
        raise web.seeother('/') # Redirecciona a raiz
