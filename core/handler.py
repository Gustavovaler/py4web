from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus
import os
import controllers
from controllers import UsersController, IndexController, ProductosController
from settings import STATIC_DIR, STATIC_DIRS
from urls import routes
from utilities.utils import static_files_maping
from core.error_messages import error_no_such_view
from core import render
from core.router import Route




class Handler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        
        #cargo los estaticos
        static_files = static_files_maping(STATIC_DIR)
        for static_dir in STATIC_DIRS:
            n_std = static_files_maping(static_dir)
            static_files += n_std
        print(static_files)
            
        if self.path == "/":
            self.path = "/index"
        
        if self.path[1:] in static_files:
            print("serving static file : {}".format(self.path[1:]))
            file_type = self.path.split('.')[1]
            if file_type == "css":
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "text/css")
                self.end_headers()
                f = open(STATIC_DIR+self.path[1:], "r")
                file = f.read()
                f.close()
                self.wfile.write(bytes(file, "utf-8"))
                return

            file_image_list = ["png", "jpeg", "jpg", "bmp", "webp"]
            if file_type in file_image_list :
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "image/"+file_type)
                self.end_headers()
                f = open(STATIC_DIR+self.path[1:], "rb")
                file = f.read()
                f.close()
                self.wfile.write(file)
                return
            if file_type == "js":
                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", "text/javascript")
                self.end_headers()
                f = open(STATIC_DIR+self.path[1:], "r")
                file = f.read()
                f.close()
                self.wfile.write(bytes(file, "utf-8"))
                return
        else:
            for route in routes:
                match = Route.get(route[0], self.path)
                if match:
                    self.dispach_controller(match)
                    print(match)
                    return

    def dispach_controller(self,match):

        #mapeo los controllers 
        p = match['controller'].capitalize()
        path = f"{p}Controller"
        if path in dir(controllers):
            #instancio el controlador llamado en la ruta
            instancia = globals()[path](path)
            #llamo al metodo index del controlador
            context = instancia.index(match)
            # context = tupla(view, context_obj)
            template = context[0]
            context_obj = context[1]
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                self.wfile.write(render.render(template,context_obj))
            except FileNotFoundError:
                self.wfile.write(bytes(error_no_such_view,"utf-8"))

            
      

    def do_POST():
        return
