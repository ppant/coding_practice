# -*- coding: utf-8 -*-
"""
Created on Thu May 20 17:42:02 2021

@author: Pradeep

Rename files in a folder
"""

import os
path = "D:\Pradeep\Downloads\Ramcharitmanas\Ramcharitmanas"
new_filename= "" # This isn't C, we don't need to pre-declare a variable.
i = 0

filenames = os.listdir(path) # is this line needed? # not that I can see, no
for dir,subdir,listfilename in os.walk(path):
    for filename in listfilename:
        i += 1
        new_filename = str(i) +'.mp3'
        src = os.path.join(dir, filename) # NOTE CHANGE HERE
        dst = os.path.join(dir, new_filename) # AND HERE        
        os.rename(src, dst)
        
print(os.listdir(path))