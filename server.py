from http.server import HTTPServer, SimpleHTTPRequestHandler
from core.handler import Handler  
from settings import SERVER_HOST, SERVER_PORT


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = (SERVER_HOST, SERVER_PORT)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
    print("Server Stops {} - {}".format(SERVER_HOST, SERVER_PORT))
    

run()