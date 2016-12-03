import web 
from web import form

render = web.template.render('views/', cache=False)

formulario = form.Form(
    form.Textbox("nombre", form.notnull, class_="form-control"),
    form.Textbox("telefono", form.notnull, class_="form-control"),
    form.Textbox("email", form.notnull, class_="form-control")
)

class Add:
    db = web.database(dbn='mysql', host='ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', db='hfl5h9jh329arfoj', user='z51bbpmzx41jy8rx', pw='ror66zkzxgb6wv7h')
    
    def __init__(self):
        pass

    def GET(self):
        result = self.db.select('contactos')
        contactos = formulario()
        return render.add(contactos, result)

    def POST(self):
        contactos = formulario()
        if not contactos.validates():
            result = self.db.select('contactos')
            return render.add(contactos, result)
        else:
            values = dict(nombre=contactos.d.nombre, telefono=contactos.d.telefono, email = contactos.d.email)
            nombre = contactos.d.nombre
            telefono = contactos.d.telefono
            email = contactos.d.email

            #self.db.query("insert into contactos(nombre,telefono,email) values('"+nombre+"','"+telefono+"','"+email+"');")
            self.db.insert('contactos', values, nombre=contactos.d.nombre, telefono=contactos.d.telefono, email=contactos.d.email)
            result = self.db.select('contactos')
            contactos = formulario()
            return render.add(contactos, result)

        