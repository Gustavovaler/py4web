import re

routes = [    
    ("/users", "UsersController"),
    ("/productos", "ProductosController"),
    ("/" , "IndexController")
]


def evaluate(path,url):
    lista_url = url[1:].split("/")    
    if (len(path)) != (len(lista_url)):
        return False
    for x in range(len(lista_url)):
        if path[x][1] == 'string':
            if not isinstance(lista_url[x] , str):
                return False
            try:
                int(lista_url[x])
                return False
            except:
                pass                
        elif path[x][1] == 'int':
            try:
                int(lista_url[x])
            except:
                return False
    return lista_url            
    


class Route:

    @staticmethod
    def get(path, url, *args, controller=None, method = None, template = None, **kwargs):
        url_parts = path.split("/")
        url_args = []
        c=1
        for seccion in url_parts[1:]:
            if re.search("<", seccion):
                d = seccion.split(":")
                d[0]=d[0][1:-1]
                url_args.append((d[0],d[1]))
            else:
                url_args.append(("space"+str(c),seccion))
            c+=1
        if evaluate(url_args, url):
            print(f"match   ** {url} - {path} ** ")
        else:
            print(f"dont match   ** {url} - {path} ** ")
        # conditions = {}
        # for t in url_args:
        #     conditions[t[0]] = t[1]

        # conditions['controller'] = controller
        # conditions['method'] = method
        # conditions['template'] = template
        # return conditions
        # # print(conditions)

        





        



resultado_ideal={"controller":"stadiums", "country":"argentina"}


Route.get("/stadiums/<country>:string/<state>:string/<city>:string/<section>:int", "/stadiums/peru/buenos_aires/caba/3",controller="IndexController", method = "index")
Route.get("/users/<user_id>:int","/users/25")
Route.get("/products/white_line/<product_id>:int", "/products/white_line/1568")
Route.get("/products/white_line/<product_id>:int","/products/other/white_line/1568")





