#!/usr/bin/env python3

################################################################
# Text
################################################################

import csv

def read_csv(filename):
   add_remove = []
   app_name = []
   perm_name = []

   with open(filename) as csvDataFile:
      csvReader = csv.reader(csvDataFile)
      for row in csvReader:
            add_remove.append(row[1])
            app_name.append(row[5])
            perm_name.append(row[7])
   return add_remove, app_name, perm_name

file = '/csv/dataset_500.csv'
add_remove, app_name, perm_name = read_csv(file)
print(add_remove[1])
print(app_name[1])
print(perm_name[1])