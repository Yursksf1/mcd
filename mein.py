#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, csv
import shutil

# Open a file



personas = [
    ["juan@mail.com", "juan2", "photo1.jpg"],
    ["pedro@mail.com", "pedro2", "phone.jpg"],
    ["mac@mail.com", "mac2", "phonejfh.jpg"],
    ["reyez@mail.com", "reyez2", "phoyjfhne.jpg"],
    ["manuel@mail.com", "manuel2", "phhone.jpg"],
    ["carlos@mail.com", "carlos2", "phojgjgne.jpg"],

]






def run_script():
    path_files = '/Users/yurley.sanchez/Downloads/wetransfer-973022/'
    for i in personas:
        # print(i[1], i[2])
        name = i[1]
        archivo = i[2]
        dir = path_files+archivo
        
    # dirs = os.listdir(path_files)
    # print('dirs', dirs)

    contador = 0
    
    
if __name__ == "__main__":
    run_script()