
import os

routes = [
    
    ("/users", "UsersController"),
    ("/productos", "ProductosController"),
    ("/" , "IndexController")

]

STATIC_DIR = os.getcwd()+"/public/static/"