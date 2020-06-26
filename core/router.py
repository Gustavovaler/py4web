import re

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
    """

    Route.get(path, url, *args, controller=None, method = None, template = None, **kwargs)
    path = is the route to be matched
    url = is the url from Handler
    controller = controller that will recieve the dict whit the values 
    method = method in controller 
    Route.get("/stadiums/<country>:string/<state>:string/<city>:string/<section>:int")
        match whit url: "/stadiums/peru/buenos_aires/caba/3"
        doesn't match with: "/stadiums/peru/11/caba/3" because argument 3 is an int but the path expected for a string
   """


    @staticmethod
    def get(path, url, *args, method = None, template = None, **kwargs):
        components = path.split("/")
        url_args = []
        c=1
        for seccion in components[1:]:
            if re.search("<", seccion):
                d = seccion.split(":")
                d[0]=d[0][1:-1]
                url_args.append((d[0],d[1]))
            else:
                url_args.append(("controller",seccion))
            c+=1
        lista_url = evaluate(url_args, url)
        if lista_url:
            conditions = {}
            for t in range(len(url_args)):
                try:
                    conditions[url_args[t][0]] = int(lista_url[t])
                except:
                    conditions[url_args[t][0]] = lista_url[t]

            conditions['method'] = method
            conditions['template'] = template
        
            return conditions
        else:
            return None 




