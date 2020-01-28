from train import train_for_markovprobs
from generate import generate_level
from visualize import create_visualization
from argparse import ArgumentParser
import glob
import pickle
import os

parser = ArgumentParser(description='Perform minimax algorithm with alphabeta pruning on a provided tree.')
parser.add_argument("-w", "--workingdir", required=False, help="The default top-level directory to work with.")
parser.add_argument("-i", "--traindir", required=False, help="The top-level directory containing formatting level inputs for training.")
parser.add_argument("-o", "--outdir", required=False, help="The directory to which to write the generate levels.")
parser.add_argument("-s", "--spritedir", required=False, help="The top-level directory containing the sprites for visualization.")
args = parser.parse_args()

num_levels = 5

workingfolder = args.workingdir or "./LevelGenAW"

traindirs = [f"{workingfolder}/AWBW/Processed"]
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

#Load the markov probabilities
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