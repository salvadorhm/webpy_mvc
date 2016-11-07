import web

render = web.template.render('views/',cache=False)

class About:
    def GET(self, name):
        name = '@salvadorhm'
        return render.about(name)
        