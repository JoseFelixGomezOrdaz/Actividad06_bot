import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config

'''
Metodo para seleccionar todos los registros de la tabla comandos_mysql
'''
def select_comandos():
    try:
        return db.select('comandos_mysql') # Selecciona todos los registros de la tabla comandos_mysql
    except Exception as e:
        print "Model select_comandos_mysql Error {}".format(e.args)
        print "Model select_comandos_mysql Message {}".format(e.message)
        return None

'''
Metodo para seleccionar un registro que coincida con el id_comando dado
'''
def select_comando(id_comando):
    try:
        return db.select('comandos_mysql',where='id_comando=$id_comando', vars=locals())[0] # selecciona el primer registro que coincida con el id_comando
    except Exception as e:
        print "Model select_comando Error {}".format(e.args)
        print "Model select_comando Message {}".format(e.message)
        return None

'''
Metodo para insertar un nuevo registro usando comando y funcion
'''
def insert_comando(comando, funcion):
    try:
        return db.insert('comandos_mysql', comando=comando, funcion=funcion) # inserta un registro en comandos_mysql
    except Exception as e:
        print "Model insert_comandos Error {}".format(e.args)
        print "Model insert_comandos Message {}".format(e.message)
        return None

'''
Metodo para eliminar un registro que coincida con el id_comando recibido
'''
def delete_comando(id_comando):
    try:
        return db.delete('comandos_mysql', where='id_comando=$id_comando',vars=locals()) # borra un registro de comandos_mysql
    except Exception as e:
        print "Model delete_comando Error {}".format(e.args)
        print "Model delete_comando Message {}".format(e.message)
        return None

'''
Metodo para actualizar el comando y funcion 
'''
def update_comando(id_comando, comando, funcion): # actualiza el comando y funcion de comandos_mysql que coincidan con el id_comando
    try:
        return db.update('comandos_mysql', 
            comando=comando,
            funcion=funcion, 
            where='id_comando=$id_comando',
            vars=locals())
    except Exception as e:
        print "Model update_comando Error {}".format(e.args)
        print "Model update_comando Message {}".format(e.message)
        return None
