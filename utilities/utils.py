import os
from os.path import isfile, isdir



def static_files_maping(static_dir):
    list_of_static_files = [obj for obj in os.listdir(static_dir) if isfile(static_dir+obj)]
    list_of_static_files.append("/js/index")
    list_of_static_files.append("js/index")
    return list_of_static_files