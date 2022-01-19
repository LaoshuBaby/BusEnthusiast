import json
import os
from bus_enthusiastic.init import *

global MAIN_PATH
global BUS_ROUTE_PATH
global BUS_STOP_PATH
global SUBWAY_ROUTE_PATH
global SUBWAY_STOP_PATH
global ARTICLE_PATH

if __name__ == "__main__":
    MAIN_PATH = __file__
    # log print(MAIN_PATH)
    path = init_path(MAIN_PATH)
    # log print(path[0])
    library = all_page_list(path[0], path[1], path[2], path[3], path[4])
    print(library)

    module_file=open(MAIN_PATH.replace("main.py","module.json"),"r",encoding="utf-8").read()
    module_json=json.loads(module_file)
    module=module_json["module"]
    module_name=[]
    for i in module:
        module_name.append(i["name"])
    print(module_name)