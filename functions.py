import json, random, os
from PIL import Image, ImageFilter
from math import floor
from parameters import workingPath, token, nbPerWallpaper
             
def getFolderStructure(root):
	# We list pictures and subfolders inside the specified folder
	images = []
	subDirectories = []
	for item in os.listdir(root):
		if os.path.isfile(os.path.join(root, item)) and item.endswith((".jpeg", ".jpg", ".png", ".bmp")):
			images.append(item)
		elif os.path.isdir(os.path.join(root, item)):
			subDirectories.append(item)
	
	output = {}	
	
	# We execute the script recursively
	for subDir in subDirectories:
		subStructure = getFolderStructure(os.path.join(root, subDir))
		
		# We exclude folders containing no pictures
		if subStructure != {}:
			output[subDir] = subStructure
	
	# We add the folder itself as a special subdirectory
	if len(images) > 0:
		output[token] = images
		
	return output

# Retrieving statitics from file
def loadData():
	try:
		with open(workingPath + "data.json") as json_file:
			return json.load(json_file)
	except Exception:
		return {}
		
# Output usage statistics
def saveData(data):
	with open(workingPath + 'data.json', 'w') as outfile:
		json.dump(data, outfile)

# Merge multiple images into one in order to fit a certain number of screens
def fusion(filenames, screens):
	files = [Image.open(filename) for filename in filenames]
	
	# If we don't have enough files, we concatenate the list with itself until we have enough pictures
	if len(files) < nbPerWallpaper:
		files = [elt for i in range(nbPerWallpaper // len(files) + 1 * nbPerWallpaper % len(files)) for elt in files][:nbPerWallpaper]
	
	# Setting up output
	output = Image.new("RGB", (sum([screenSize[0] for screenSize in screens]), max([screenSize[1] for screenSize in screens])), "black")

	deltaX = 0
	for i, img in enumerate(files):
		# We check if the image is as the right size
		if(img.size != screens[i]):
			ratio = screens[i][0] / screens[i][1]
			print("Resizing image " + str(i + 1) + " to fit the corresponding screen")
			
			# Depending on the ratio we resize to fit the width or the height
			if(img.size[0] / img.size[1] > ratio):
				img = img.resize((floor(screens[i][1]/img.size[1] * img.size[0]), screens[i][1]), Image.LANCZOS)
				cropX = floor((img.size[0] - screens[i][0]) / 2)
				img = img.crop((cropX, 0, cropX + screens[i][0], screens[i][1]))
			else:
				img = img.resize((screens[i][0], floor(screens[i][0]/img.size[0] * img.size[1])), Image.LANCZOS)
				cropY = floor((img.size[1] - screens[i][1]) / 2)
				img = img.crop((0, cropY, screens[i][0], cropY + screens[i][1]))
		
		# Fitting the image in a box which coordinates are given in the following order : left, top, right, bottom
		output.paste(img, (deltaX, 0, deltaX + screens[i][0], screens[i][1]))
		deltaX += screens[i][0]

	#Display image
	output.save(workingPath + "output.jpg", "JPEG")
	print("Output saved")

# modified from SO : http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
# Output a list with N items, the weight
def weighted_choices(weighted_items, N, itemFormat="couple"):
	choices = {}
	for key, item in weighted_items.items():
		if(itemFormat == "couple"):
			choices[key] = item[0]
		else:
			choices[key] = item
	
	# If we do not have enough pictures registered
	assert (len(choices) != 0), "Not enough elements"
		
	output = []
	total = sum(w for c, w in choices.items())
	i = 0
	
	while choices != {} and i < N:
		r = random.uniform(0, total)
		upto = 0
		for c, w in dict(choices).items():
			if upto + w > r:
				output.append(c)
				total -= w
				del choices[c]
				break
			upto += w
		i += 1
		
	return output



