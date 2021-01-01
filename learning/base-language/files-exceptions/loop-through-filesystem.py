#!/usr/bin/env python3

################################################################
# Moving files in the file system
################################################################

import os
import shutil

directory = '/myapp'

try:
   items = os.scandir(directory)
except Exception as e:
   print("No files in the directory")
   exit(0)

match = 0

for item in items:
   # print('processing :', item.name)
   if item.path.endswith(".csv") and item.is_file() and item.name.find('dataset') == 0:
      match = match + 1
      print('Found file to process: ', item.path)
      dest = '/myapp/processed/' + item.name
      # do something with the file
      # move file to destination
      try:
            shutil.move(item.path, dest)
      except Exception as e:
            print("Unable to move folder to destination: ", item.name)
   else:
      pass
      
   if match == 0:
      print("No files in the directory that match expected format")
      exit(0)
   else:
      pass
