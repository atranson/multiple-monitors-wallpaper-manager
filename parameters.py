import os, sys

try:
	from localConfig import path
except ModuleNotFoundError:
	sys.exit("Error: no local configuration could be found. Make sure you ran the setup.py file first")

if(not(path.endswith("/")) and not(path.endswith("\\"))):
	path += "/"

workingPath = os.path.dirname(os.path.realpath(__file__)) + "\\"
token = "0a5ed3376d044f5c707b0327219547f3e0b46f70" # Do not name a folder of your library with this string
