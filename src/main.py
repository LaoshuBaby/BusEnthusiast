import json
import os
from bus_enthusiastic.init import *

global MAIN_PATH
global BUS_ROUTE_PATH
global BUS_STOP_PATH
global SUBWAY_ROUTE_PATH
global SUBWAY_STOP_PATH
global ARTICLE_PATH

def get_single_page(page_name):
    # page_name can be a route/stop's name and get all json in its folder
    pass

def build_single_page(page_name):
    pass

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

    # 接下来的流程大体是逐个page读取并且build

    def build(template):
        pass

    # templete_brief=["introduction"+"route"]