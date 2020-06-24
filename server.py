from http.server import HTTPServer, SimpleHTTPRequestHandler
from core.handler import Handler  


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