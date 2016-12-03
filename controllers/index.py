import web

render = web.template.render('views/', cache=False)

class Index:
    def __init__(self):
        pass
        
    def GET(self):
        return render.index()
        