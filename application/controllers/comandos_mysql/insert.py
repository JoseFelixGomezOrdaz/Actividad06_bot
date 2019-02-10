import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        comando = formulario['comando'] # alamcena el comando escrito en el input
        funcion = formulario['funcion'] # almacena el funcion escrito en el input
        config.model_comandos_mysql.insert_comando(comando, funcion) # llama al metodo insert_datos y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
