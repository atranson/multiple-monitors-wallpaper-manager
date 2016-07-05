import os

# To be modified
path = 'D:/Pictures/Wallpapers/' # Path to the current folder containing wallpapers

# DON'T MODIFY
if(not(path.endswith("/")) and not(path.endswith("\\"))):
	path += "/"

workingPath = os.path.dirname(os.path.realpath(__file__)) + "\\"
nbPerWallpaper = len(screens)
token = "0a5ed3376d044f5c707b0327219547f3e0b46f70" # Do not name a folder of your library with this string
