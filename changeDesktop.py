import os
from functions import *
from parameters import *
from updateList import *
from monitorInfo import getMonitorsAreas

updateList()
fullData = loadData()

def choosePictures(data, root, isLeaf=False):
	nbElts = len(data)
	
	# If we are now chosing the pictures
	if isLeaf:
		filenames = getWeightedChoices(data, nbPerWallpaper, "singleton")
		fullNames = [os.path.join(root, filename) for filename in filenames]

		# Decreasing weigths for used elements, increasing for unused elements
		for key, item in data.items():
			data[key] = min(data[key] + nbPerWallpaper/nbElts, 1)
			
		for filename in filenames:
			data[filename] = 1/nbElts
		
		return fullNames
	
	# If we are choosing a folder
	else:
		subFolder = getWeightedChoices(data, 1, "couple")[0]
		
		# Decreasing weigths for used elements, increasing for unused elements
		for key, item in data.items():
			data[key][0] = min(data[key][0] + 1/nbElts, 1)
			
		data[subFolder][0] = 1/nbElts
		
		if subFolder == token:
			return choosePictures(data[subFolder][1], root, True)
		else:
			return choosePictures(data[subFolder][1], os.path.join(root, subFolder))
		

fullNames = choosePictures(fullData, path)

# Generate output.jpg
fusion(fullNames, getMonitorsAreas())

saveData(fullData)


