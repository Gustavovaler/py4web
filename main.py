from http.server import HTTPServer, SimpleHTTPRequestHandler
from http import HTTPStatus
import os
import controllers
from controllers import IndexController, UsersController, ProductosController
from settings import routes, STATIC_DIR
from utilities.utils import static_files_maping

    

class Handler(SimpleHTTPRequestHandler):
    
    def do_GET(self):
        
        #cargo los estaticos
        static_files = static_files_maping(STATIC_DIR)
        print(STATIC_DIR+self.path)
        print(static_files)

        if self.path[1:] in static_files:
            print("serving static file : {}".format(self.path[1:]))
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/css")
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
                print("Requesting  tamplate for route: {}".format(route))
                # r son las rutas en el modulo routes.py
                self.dispach_controller(r[1])
                return
            

    
    def dispach_controller(self,path):

        #mapeo los controllers 
        if path in dir(controllers):
            #instancio el controlador llamado en la ruta
            instancia = globals()[path](path)
            #llamao al metodo index del controlador
            context = instancia.index()
            # context = tupla(view, context_obj)
            template = context[0]
            context_obj = context[1]
            # print("*******************")
            # print("Template :{}".format(template))
            # print("Context : {}".format(context_obj))
            # print("*******************")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            c = open(os.getcwd()+"/public/views/"+template)
            file = c.read()
            c.close()
            self.wfile.write(bytes(file,"utf-8"))
            

      

        # for route in routes:
        #     path = route[0]
        #     print("self path = {}".format(self.path))
        #     print(path)
        #     if path == self.path:
        #         cont= route[1]
        #         r = controller.Controller(path)
        #         respuesta = r.index()
        #         print(respuesta)
        #         break
        #     # else:
        #     #     self.send_response(HTTPStatus.NOT_FOUND)
        #     #     self.send_header("Content-type", "text/html")
        #     #     self.end_headers()
        #     #     self.wfile.write(bytes("<h1>No encontrado - 404</h1>", "utf-8"))
        #     #     return
        
        # self.directory = os.getcwd()+"/public/views"
        # f = self.send_head()
        
        # if f:
        #     try:
        #         self.copyfile(f, self.wfile)
        #     finally:
        #         f.close()

   

    def do_POST():
        return


def run(server_class=HTTPServer, handler_class=Handler):
    HOST_NAME = "localhost"
    PORT_NUMBER = 8000
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print("Server Stops {} - {}".format(HOST_NAME, PORT_NUMBER))
    

run()