### PYTHON REQUIREMENTS ###
Tested with Python 3.5 & Pillow 3.0
In order to work properly this script needs the Pillow library to be installed
To install Pillow, use pip and execute pip install Pillow
Pillow files need to be located in the lib/site-packages/ directory of the Python installation if the script is meant to be scheduled (and not in C:/Users/...)
Normally, if you executed the installation command with administrator rights, everything should be ok directly

### HOW TO SETUP ###
In parameters.py, change the following as needed :
1. Screen resolutions (Format : "[(width, height), (width, height), (width, height), ...]")
2. Path to the folder with the pictures (absolute path)

### HOW TO USE ###
1. Put pictures in the folder you set up in parameters.py
2. Schedule the execution of ChangeDesktop.vbs or run it manually
