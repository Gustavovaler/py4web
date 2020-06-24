from core.controller import Controller

class IndexController(Controller):
    def index(self):
        print("el path ingresado es {} desde controller".format(self.path))
        return ("index.html", None)


class UsersController(Controller):
    def index(self):
        print("el path ingresado es {} desde controller".format(self.path))
        return ("users.html", None)



class ProductosController(Controller):
    def index(self):
        print("el path ingresado es {} desde controller".format(self.path))
        return ("productos.html", None)