import glob
from PIL import Image

leveldirectory = "./LevelGenAW/AWBW/Processed"
spritesdirectory = "./LevelGenAW/sprites"
levelname = "2_islands_war"
level = {}
with open(f"{leveldirectory}/{levelname}.txt") as fp:
	for y, line in enumerate(fp):
		level[y] = line

sprites = {}
for filename in glob.glob(f"{spritesdirectory}/**/*.png", recursive=True):
	im = Image.open(filename)
	name = filename.split("/")[-1][:-4]
	sprites[name] = im

imagetest = sprites["hq-blue"].convert("RGBA")
imageloaded = imagetest.load()
#imagetest.show()
print(imageloaded[10, 10])