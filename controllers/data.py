import web

render = web.template.render('views/',cache=False)

class Data:
    def GET(self, records):
        db = web.database(dbn='mysql', db='agenda', user='root', pw='toor')
        #db = PostgresqlDatabase(database='', user='',password='', host='', port='5432')
        records =[]
        records = db.select('contactos')
        return render.data(records)
        