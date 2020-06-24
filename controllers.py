import model
class Controller:
    def __init__(self, path):
        self.path = path



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