from core.controller import Controller


class IndexController(Controller):
    def index(self,context,*args, **kwargs):
        context['variable'] = "algo"
        return ("index.html", context)


class UsersController(Controller):
    def index(self,context, *args, **kwargs):
        print(context)        
        return ("users.html", context)


class ProductosController(Controller):

    def index(self,context,*args, **kwargs):       
        return ("productos.html", None)