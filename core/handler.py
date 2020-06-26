from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus
import os
import controllers
from settings import STATIC_DIR
from urls import routes
from utilities.utils import static_files_maping
from core.error_messages import error_no_such_view
from core import render
from controllers import IndexController, UsersController, ProductosController


class Handler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        
        #cargo los estaticos
        static_files = static_files_maping(STATIC_DIR)
        
        if self.path[1:] in static_files:
            # print("serving static file : {}".format(self.path[1:]))
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


        # itero en las rutas para encontrar conincidencia        
        for r in routes:
            route = r[0]
            #ruta encontrada
            if route == self.path:
                # print("Requesting  tamplate for route: {}".format(route))
                # r son las rutas en el modulo routes.py
                self.dispach_controller(r[1])
                return
            

    
    def dispach_controller(self,path):

        #mapeo los controllers 
        if path in dir(controllers):
            #instancio el controlador llamado en la ruta
            instancia = globals()[path](path)
            #llamo al metodo index del controlador
            context = instancia.index()
            # context = tupla(view, context_obj)
            template = context[0]
            context_obj = context[1]
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                # c = open(os.getcwd()+"/public/views/"+template)
                # file = c.read()
                # c.close()
                self.wfile.write(render.render(template,context_obj))
            except FileNotFoundError:
                self.wfile.write(bytes(error_no_such_view,"utf-8"))

            
      

    def do_POST():
        return
