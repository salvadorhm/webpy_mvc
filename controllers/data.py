import web

render = web.template.render('views/',cache=False)

class Data:
    def GET(self, records):
        #db = web.database(dbn='mysql', db='agenda', user='root', pw='toor')
        db = web.database(dbn='mysql', host='ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', db='hfl5h9jh329arfoj', user='z51bbpmzx41jy8rx', pw='ror66zkzxgb6wv7h')
        #db = PostgresqlDatabase(database='', user='',password='', host='', port='5432')
        records =[]
        records = db.select('contactos')
        return render.data(records)
        
