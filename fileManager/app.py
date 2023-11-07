import os, glob
import os.path
from colored import Fore, Back, Style
targetdir = r"C:\Users\master"
files = os.listdir(targetdir); 

def convert_size(size_bytes):
    import math 
    if size_bytes == 0: 
        return "0B"
    size_name = ("B","KB","MB","GB","TB","PB","EB","ZB","YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

for i in files:
    if os.path.isdir(targetdir+r"\\"+i):
        print(f"{Fore.red}" + i + f"{Style.reset}")
    else:
        print(f"{Fore.blue}" + i + f"{Style.reset}")
        file_size = os.path.getsize(targetdir+r"\\"+i)
        print('File size:', convert_size(file_size))