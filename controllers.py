from core.controller import Controller


class IndexController(Controller):
    def index(self):
        context = {}
        context['users'] = [{"nombre": "Marcelo", "edad": 25, "url":"something"},
                                {"nombre": "gustavo", "edad": 26, "url":"something"},
                                {"nombre": "Juan", "edad": 30, "url":"something"}]
        context['variable'] = "hola"
        return ("index.html", context)


class UsersController(Controller):
    def index(self):
        
        return ("users.html", None)



class ProductosController(Controller):
    def index(self):
       
        return ("productos.html", None)