import json
import os
from bus_enthusiastic.init import all_page_list

if __name__ == "__main__":
    MAIN_PATH=__file__
    print(MAIN_PATH)
    all_page_list(MAIN_PATH)