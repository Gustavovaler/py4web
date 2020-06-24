from core.controller import Controller


class IndexController(Controller):
    def index(self):
        context = {}
        context['usuarios'] = [{"nombre": "Marcelo", "edad": 25},{"nombre": "gustavo", "edad": 25}]

        return ("index.html", context)


class UsersController(Controller):
    def index(self):
        
        return ("users.html", None)



class ProductosController(Controller):
    def index(self):
       
        return ("productos.html", None)