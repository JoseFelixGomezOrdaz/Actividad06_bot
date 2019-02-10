import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, id_comando): 
        comandos_mysql = config.model_comandos_mysql.select_comando(id_comando) # Selecciona el registro que coincida con id_comando
        return config.render.update(comandos_mysql) # Envia el registro y renderiza update.html
    
    def POST(self, id_comando, comando, funcion):
        formulario = web.input() # almacena los datos del formulario web
        id_comando = formulario['id_comando'] # almacena el id_comando del input formulario
        comando = formulario['comando'] # almacena el comando del input formulario
        funcion = formulario['funcion'] # almacena el funcion del input formulario        
        config.model_comandos_mysql.update_comando(id_comando, comando, funcion) # actuliza los valores
        raise web.seeother('/') # redirecciona al index
