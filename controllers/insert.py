import web 
from web import form

render = web.template.render('views/', cache=False)


insert_form = form.Form(
    form.Textbox("nombre", description="nombre"),
    form.Textbox("telefono", description="telefono"),
    form.Textbox("email",  description="E-Mail"),
    form.Button("submit", type="submit", description="Insertar")
    )

class Insert:
    def __init__(self):
        pass

    def GET(self):
        form = insert_form()
        return render.insert(form)

    def POST(self):
        form = insert_form()
        conecction = web.database(dbn='mysql', db='agenda', user='root', pw='toor')
        print form['nombre'].value
        print form.d.telefono
        print form.d.email
        return render.insert(form)
