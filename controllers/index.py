import web

render = web.template.render('views/',cache=False)

class Index:
    def GET(self):
        return render.index()
        