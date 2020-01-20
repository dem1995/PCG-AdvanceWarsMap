import sys
import os
import glob
from PIL import Image
from tilenumbers import Tile


# visualization = {}
# visualization['P']	= 'plains'
# visualization['M']	= 'mountains'
# visualization['W']	= 'woods'
# visualization['═']	= 'river'#'river-ew'
# visualization['║']	= 'river'#'river-ns'
# visualization['¤']	= 'river'#'river-c'
# visualization['╔']	= 'river'#'river-se'
# visualization['╗']	= 'river'#'river-sw'
# visualization['╝']	= 'river'#'river-nw'
# visualization['╚']	= 'river'#'river-ne'
# visualization['╦']	= 'river'#'river-sew'
# visualization['╣']	= 'river'#'river-nsw'
# visualization['╩']	= 'river'#'river-new'
# visualization['╠']	= 'river'#'river-nse'
# visualization['━']	= 'road'#'road-ew'
# visualization['┃']	= 'road'#'road-ns'
# visualization['•']	= 'road'#'road-c'
# visualization['┏']	= 'road'#'road-se'
# visualization['┓']	= 'road'#'road-sw'
# visualization['┛']	= 'road'#'road-nw'
# visualization['┗']	= 'road'#'road-ne'
# visualization['┳']	= 'road'#'road-sew'
# visualization['┫']	= 'road'#'road-nsw'
# visualization['┻']	= 'road'#'road-new'
# visualization['┣']	= 'road'#'road-nse'
# visualization['╍']	= 'bridge-ew'
# visualization['╏']	= 'bridge-ns'
# visualization['O']	= 'ocean'
# visualization['🠹']	= 'ocean'#'shore-north-facing'
# visualization['🠻']	= 'ocean'#'shore-south-facing'
# visualization['🠺']	= 'ocean'#'shore-east-facing'
# visualization['🠸']	= 'ocean'#'shore-west-facing'
# visualization['S']	= 'shoal' 
# visualization['E']	= 'city-neutral'
# visualization['▦'] 	= 'factory-neutral'
# visualization['⋄'] 	= 'airport-neutral'
# visualization['◍'] 	= 'port-neutral' #visualization[37] = '🍚'
# visualization['Ⅎ'] 	= 'city-orange' #visualization[38] = '🧡'
# visualization['⬓'] 	= 'factory-orange' #visualization[39] = '🟧'
# visualization['⬙'] 	= 'airport-orange' #visualization[40] = '🔶'
# visualization['◒'] 	= 'port-orange' #visualization[41] = '🟠'
# visualization['⭐'] 	= 'hq-orange' #visualization[42] = '🌟'
# visualization['F'] 	= 'city-blue' #visualization[43] = '💙'
# visualization['◨'] 	= 'factory-blue' #visualization[44] = '🟦'
# visualization['⬗'] 	= 'airport-blue' #visualization[45] = '🔷'
# visualization['◑'] 	= 'port-blue' #visualization[46] = '🔵'
# visualization['☾'] 	= 'hq-blue' #visualization[47] = '🌙'


def create_visualization(levelname, leveldirectory, spritesdirectory):
	#Load sprites
	sprites = {}
	for filename in glob.glob(f"{spritesdirectory}/**/*.png", recursive=True):
		im = Image.open(filename)
		name = filename.split("/")[-1][:-4]
		sprites[name] = im.convert("RGBA")

	level = {}
	with open(f"{leveldirectory}/{levelname}.txt") as fp:
		for y, line in enumerate(fp):
			level[y] = line[:-1]
			print(f"{y}:")
			print(line)

	maxX = len(level[0])
	maxY = y+1
	print(f"Max y is {y}")



	#Create backdrop of tiled plains sprites to which to write actual sprites
	def createTiledPlainsImage():
		image = Image.new("RGB", (maxX*16, (maxY)*16), color=(91, 153, 254))
		pixels = image.load()

		imageToUse = sprites[Tile.reverse_lookup["P"].filename]
		pixelsToUse = imageToUse.load()
		for y in range(0, maxY):
			for x in range(0, maxX):
				for x2 in range(0, 16):
					for y2 in range(0, 16):
						pixels[x*16+x2,y*16+y2] = pixelsToUse[x2,y2][:-1]
		return image, pixels

	image, pixels = createTiledPlainsImage()

	#Draw the actual building/terrain sprites to the image
	for y in range(0, maxY):
		for x in range(0, maxX):
			imageToUse = None
			print(y)
			print(maxY)
			print(levelname)
			print(f"{x}, {y}")
			if level[y][x] in Tile.reverse_lookup.keys():
				print(Tile.reverse_lookup[level[y][x]])
				imageToUse = sprites[Tile.reverse_lookup[level[y][x]].filename]
			if not imageToUse == None:
				pixelsToUse = imageToUse.load()
				x2max = imageToUse.size[0]
				y2max = imageToUse.size[1]
				for x2 in range(0, x2max):
					for y2 in range(0, y2max):
						if pixelsToUse[x2,y2][3]>0:
							upwardoffset = y2max-16
							ywritepixel = y*16+y2-upwardoffset if y*16+y2-upwardoffset>=0 else y*16+y2
							#print(ywritepixel)
							#ywritepixel=y*16+y2
							pixels[x*16+x2,ywritepixel] = pixelsToUse[x2,y2][:-1]

	#save the resulting level image
	absleveldir = os.path.abspath(f"{leveldirectory}")
	print(leveldirectory)
	print(absleveldir)
	image.save(rf"{absleveldir}/{levelname}.png","PNG")

if __name__ == "__main__":
	leveldirectory = "./LevelGenAW/GeneratedLevels"
	spritesdirectory = "./LevelGenAW/sprites"
	#create_visualization("battle-of-thermopylae", leveldirectory, spritesdirectory)
	for levelfile in glob.glob(f"{leveldirectory}/*.txt"):
		levelname = os.path.basename(levelfile)[:-4]
		print(levelname)
		create_visualization(levelname, leveldirectory, spritesdirectory)
