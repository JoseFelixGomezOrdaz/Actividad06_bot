import web # importa la libreria web.py
import application.models.model_comandos_mysql as model_comandos_mysql # importa el modelo_comandos_mysql 


render = web.template.render('application/views/comandos_mysql/', base='master') # configura la ubicacion de las vistas