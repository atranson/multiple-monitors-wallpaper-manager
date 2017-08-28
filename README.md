# ABOUT #
These small scripts handle the generation of wallpapers to fit multiple screens at once.
In addition to detecting the monitors' sizes and fitting pictures to their respective sizes and positions, the scripts make sure to use pictures that are located in the same folder only. 
Moreover, the randomized selection of pictures that is done at each run of the main script is weighted so that pictures that have already been used recently tend to not reappear to quickly.
This weighted approach is applied for both folders, subfolders and pictures inside those.

For example, you could have the following folder structure:

    /Landscapes
	    /Asia
		/Europa
	/Space
	
With such a structure, the scripts would produce combinations of pictures of either Asia, Europa or Space (or it would use pictures located at the root of /Landscapes).

# PYTHON REQUIREMENTS #
Tested with Python 3.5 & Pillow 3.0.
In order to work properly this script needs the Pillow library to be installed.
To install Pillow, use pip and execute 

    pip install Pillow
	
Pillow files need to be located in the lib/site-packages/ directory of the Python installation if the script is meant to be scheduled with Windows (and not in C:/Users/...) (if the installation was done through command line with administrator rights, everything should be ok directly)

# HOW TO SETUP #
Run setup.py and enter the path to the folder with the pictures (and structure of folders) you want to use:

# HOW TO USE #
1. Put pictures in the folder you entered previously
2. Schedule the execution of ChangeDesktop.py or run it manually to obtain output.jpg

# SCHEDULING ON WINDOWS #
You can schedule the execution of ChangeDesktop.vbs. This script will replace your current wallpaper with the newly generated one and make sure that Windows applies that change immediately.

# GETTING A RIGHT CLICK MENU ENTRY TO CHANGE YOUR WALLPAPER ON WINDOWS #
1. Run createContextMenuInteractionEditor.py
2. Add the right click menu entry by double clicking the newly created addContextMenuInteraction.reg file (this will modify Windows registry)
