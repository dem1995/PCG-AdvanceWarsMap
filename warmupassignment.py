from src.train import train_for_markovprobs
from src.generate import generate_level
from src.visualize import create_visualization
import glob
import pickle
import os

num_levels = 20

workingfolder = "./LevelGenSMB"

traindirs = [f"{workingfolder}/Super Mario Bros/Processed", "./Super Mario Bros 2 (Japan)/Processed"]
markovpickle = f"{workingfolder}/markovprobabilities.pickle"
outputdir = f"{workingfolder}/GeneratedLevels"
spritesdir = f"{workingfolder}/sprites"

if not os.path.exists(outputdir):
    os.makedirs(outputdir)

#Train on the level sets to obtain markov probabilities
train_for_markovprobs(markovpickle, traindirs)

#Wiping the files currently in that directory
files = glob.glob(f"{outputdir}/*")
for f in files:
	os.remove(f)

#Load the ??? probabilities
markovProbabilities = pickle.load(open(markovpickle, "rb"))

#Generate levels

levelnum = 0
while levelnum < num_levels:
	levelname = f"Level{levelnum}"
	try:
		generate_level(levelname, markovProbabilities, outputdir)
		create_visualization(levelname, outputdir, spritesdir)
		levelnum = levelnum+1
		print("f")
	except:
		os.remove(f"{outputdir}/{levelname}.txt")
		pass