from core.controller import Controller


class IndexController(Controller):
    def index(self):
        
        return ("index.html", None)


class UsersController(Controller):
    def index(self):
        
        return ("users.html", None)



class ProductosController(Controller):
    def index(self):
       
        return ("productos.html", None)