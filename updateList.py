from functions import *
from parameters import path, token

def addNewElements(structure, data):
	for key, elt in structure.items():
		if key not in data:
			data[key] = (1, {})
			
		# If the item is a subdirectory
		if key != token:
			addNewElements(elt, data[key][1])
		# If we are dealing with the images	directly
		else:
			# We create entries for the new images contained in elt (as a dictionnary)
			for img in elt:
				if img not in data[token][1]:
					data[token][1][img] = 1

def deleteUnusedEntries(structure, data):
	foldersToDelete = []
	imagesToDelete = []
	for key, couple in data.items():
		# If we directly know that the key no longer exists
		if key not in structure:
			foldersToDelete.append(key)
		else:
			# If the item is a subdirectory
			if key != token:
				deleteUnusedEntries(structure[key], data[key][1])
			# If we are dealing with the images	directly
			else:
				for imageFilename, weight in data[token][1].items():
					if imageFilename not in structure[token]:
						imagesToDelete.append(imageFilename)
						
				# We delete images
				for imageFilename in imagesToDelete:
					del data[token][1][imageFilename]
		
	# We delete folders
	for key in foldersToDelete:
		del data[key]

def updateList():
	structure = getFolderStructure(path)
	data = loadData()

	# We search for entires that are no longer associated to any concrete folder/image
	deleteUnusedEntries(structure, data)

	# We create entries for the new images
	addNewElements(structure, data)

	saveData(data)

if __name__ == '__main__':
	updateList()
