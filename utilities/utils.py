import os
from os.path import isfile, isdir



def static_files_maping(static_dir):
    return [obj for obj in os.listdir(static_dir) if isfile(static_dir+obj)]