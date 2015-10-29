import os

workingPath = os.path.dirname(os.path.realpath(__file__)) + "\\"

output = 'Windows Registry Editor Version 5.00 \n\
\n\
[HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\Next Wallpaper]\n\
@="Next Wallpaper"\n\
\n\
[HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\Next Wallpaper\\command]\n\
@="wscript.exe \\"' + workingPath.replace("\\", "\\\\") + 'ChangeDesktop.vbs\\""'

with open('addContextMenuInteraction.reg', 'w') as file_:
    file_.write(output)
    print("addContextMenuInteraction.reg created successfully")
