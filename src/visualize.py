import sys
import os
import glob
from PIL import Image




def create_visualization(levelname, leveldirectory, spritesdirectory):
	#Load sprites
	sprites = {}
	for filename in glob.glob(f"{spritesdirectory}/*.png"):
		im = Image.open(filename)
		splits = filename.split("/")
		name = splits[-1][:-4]
		sprites[name] = im
		print (str(im.size))

	visualization = {}
	visualization["S"] = "brick"
	visualization["?"] = "questionMark"
	visualization["Q"] = "emptyBlock"
	visualization["E"] = "goomba"
	visualization["<"] = "topLeftPipe"
	visualization[">"] = "topRightPipe"
	visualization["["] = "leftPipe"
	visualization["]"] = "rightPipe"
	visualization["o"] = "coin"
	visualization["B"] = "cannonTop"
	visualization["b"] = "cannonBottom"

	#Visualize Output Level

	level = {}
	with open(f"{leveldirectory}/{levelname}.txt") as fp:
		y = 0
		maxX = 0
		for line in fp:
			level[y] = line
			y+=1
			maxX = len(line)-1 if len(line)-1 > maxX else maxX
	maxY = 15

	image = Image.new("RGB", (maxX*16, maxY*16), color=(91, 153, 254))
	pixels = image.load()

	maxY = len(level)
	print(maxY)
	for y in range(0, maxY):
		maxX = len(level[y])-1
		for x in range(0, maxX):
			imageToUse = None
			if level[y][x] in visualization.keys():
				imageToUse = sprites[visualization[level[y][x]]]
			elif level[y][x]=="X":
				if y>maxY-2:
					imageToUse = sprites["ground"]
				else:
					imageToUse = sprites["stair"]
			if not imageToUse == None:
				pixelsToUse = imageToUse.load()
				for x2 in range(0, 16):
					for y2 in range(0, 16):
						if pixelsToUse[x2,y2][3]>0:
							pixels[x*16+x2,y*16+y2] = pixelsToUse[x2,y2][0:-1]

	absleveldir = os.path.abspath(f"{leveldirectory}")
	print(leveldirectory)
	print(absleveldir)
	image.save(rf"{absleveldir}/{levelname}.jpeg", "JPEG")

if __name__ == "__main__":
	create_visualization("output", "./SMBGeneration/Generated Levels", "./SMBGeneration/sprites")
