import os

global BUS_ROUTE_PATH
global BUS_STOP_PATH
global SUBWAY_ROUTE_PATH
global SUBWAY_STOP_PATH
global ARTICLE_PATH

def all_page_list(MAIN_PATH):
    BUS_ROUTE_PATH = os.path.join(MAIN_PATH, "..", "data", "bus_route").replace(
        "/main.py", ""
    )
    BUS_STOP_PATH = os.path.join(MAIN_PATH, "..", "data", "bus_stop").replace(
        "/main.py", ""
    )
    SUBWAY_ROUTE_PATH = os.path.join(
        MAIN_PATH, "..", "data", "subway_route"
    ).replace("/main.py", "")
    SUBWAY_STOP_PATH = os.path.join(MAIN_PATH, "..", "data", "subway_stop").replace(
        "/main.py", ""
    )
    ARTICLE_PATH = os.path.join(MAIN_PATH, "..", "data", "article").replace(
        "/main.py", ""
    )

    bus_route_list = os.listdir(BUS_ROUTE_PATH)
    bus_stop_list = os.listdir(BUS_STOP_PATH)
    subway_route_list = os.listdir(SUBWAY_ROUTE_PATH)
    subway_stop_list = os.listdir(SUBWAY_STOP_PATH)
    article_list = os.listdir(ARTICLE_PATH)

    def is_list_a_folder(group_dir_tree):
        temp_list = []
        for i in group_dir_tree:
            # 判断是否是文件夹
            if os.path.isdir(os.path.join(BUS_ROUTE_PATH, i)):
                temp_list.append(i)
        return temp_list

    bus_route_list = is_list_a_folder(bus_route_list)
    bus_stop_list = is_list_a_folder(bus_stop_list)
    subway_route_list = is_list_a_folder(subway_route_list)
    subway_stop_list = is_list_a_folder(subway_stop_list)
    article_list = is_list_a_folder(article_list)

    print(bus_route_list)
    print(bus_stop_list)
    print(subway_route_list)
    print(subway_stop_list)
    print(article_list)
