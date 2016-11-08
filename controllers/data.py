import web

render = web.template.render('views/',cache=False)

class Data:
    def GET(self, records):
        db = web.database(dbn='mysql', host='ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com' db='dj6fjvy0zpy56ntr', user='rpdu2zcvkh9rpllh', pw='dpgqepye9p3ucdlp')
        #db = PostgresqlDatabase(database='', user='',password='', host='', port='5432')
        records =[]
        records = db.select('contactos')
        return render.data(records)
        
