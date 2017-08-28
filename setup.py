import os

path = ""
isValidPath = False

while(not isValidPath):
	print("Please enter the full path to the folder containing your wallpapers\n(e.g. \"D:/Pictures/Wallpapers/\")")
	path = input("> ")
	
	path = path.strip() # Trim white spaces
	if not path:
		print("\nError: you entered an empty path")
	elif '\\' in path:
		print("\nError: the path should use / and not \\")
	elif not os.path.isdir(path.strip()):
		print("\nError: the path you entered is not a folder")
	else:
		isValidPath = True
	print("")
	
with open("localConfig.py", "w") as f:
	f.write("path = \"" + path + "\"")
print("Setup complete! You can now run changeDesktop.py to generate multi desktops wallpapers based on the content of the folder you just entered")

