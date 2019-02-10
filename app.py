import web
        
urls = (
    '/', 'application.controllers.comandos_mysql.index.Index',
    '/insert', 'application.controllers.comandos_mysql.insert.Insert',
    '/update/(.*)', 'application.controllers.comandos_mysql.update.Update',
    '/delete/(.*)', 'application.controllers.comandos_mysql.delete.Delete',
    '/view/(.*)', 'application.controllers.comandos_mysql.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
