#!/usr/bin/python3

################################################################
# Example of package dotenv
################################################################

# Step 1: Create your venv folder and add the python-dotenv package:

# cd /myuser/scripts
# mkdir csv
# cd csv
# scl enable rh-python36 bash
# python -m venv /myuser/scripts/csv/venv
# source /myuser/scripts/csv/venv/bin/activate
# pip install --upgrade pip
# python3 -m pip install python-dotenv

# Step 2: Create an .env file at the root of your csv folder and enter

# EMAIL="somePass"
# MYVAR="hunter2"

# Step 3: Enter the following in your .py file that should also be at root of csv folder

from dotenv import load_dotenv

load_dotenv()

try:
   myvar = os.environ["MYVAR"]
except Exception as e:
   print("Unable to get environmental variable: myvar")
   exit(1)
# same for EMAIL
