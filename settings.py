
import os



#****************************************
#        server settings
#****************************************
SERVER_HOST = "localhost"
SERVER_PORT = 8000



#****************************************
#        static settings
#****************************************

STATIC_DIR = os.getcwd()+"/public/static/"

STATIC_DIRS = [
    STATIC_DIR+"css/",
    STATIC_DIR+"js/",
    STATIC_DIR+"img/"
    ]