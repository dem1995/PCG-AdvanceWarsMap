import sys
import os
import glob
import random
import pickle

def generate_level(levelname, markovProbabilities, outputdirectory):

	level = {}

	maxY = 14
	maxX = 100

	for y in range(maxY, -1, -1):
		level[y] =""
		for x in range(0, maxX):
			west = " "
			southwest = " "
			south = " "

			if x>0: 
				west = level[y][x-1]
			if y<maxY: 
				south = level[y+1][x-1]
			if x>0 and y<maxY: 
				southwest = level[y+1][x]

			key = west+southwest+south

			if key in markovProbabilities.keys():
				randomSample = random.uniform(0, 1)
				currValue = 0.0
				for key2 in markovProbabilities[key]:
					if randomSample>=currValue and randomSample<currValue+markovProbabilities[key][key2]:
						level[y] += key2
						break
					currValue+=markovProbabilities[key][key2]
			else:
				level[y] +="-"

	with open(f"{outputdirectory}/{levelname}.txt", "a") as the_file:
		for y in range(0, maxY+1):
			the_file.write(level[y]+"\n")

if __name__ == "__main__":
	#The filepath of the folder to which to write files
	outputdir = "./SMBGeneration/Generated Levels"

	#Wiping the files currently in that directory
	files = glob.glob(f"{outputdir}/*")
	for f in files:
		os.remove(f)
	
	#Load the ??? probabilities
	markovProbabilities = pickle.load(open("markovprobabilities.pickle", "rb"))

	#Generate a level
	generate_level("output", markovProbabilities, outputdir)