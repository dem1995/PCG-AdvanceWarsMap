"""
Scans processed level files for patterns and determines the probabilities with which, given a tile pattern about a tile, a given tile occurs. 
Specifically, it keeps a dictionary of patterns; the keys are the subsets of the powerset of the ordered set of tiles adjacent to the given tile; the values themselves refer to dictionaries of probabilities. 
Which cardinal directions' probability-dictionaries are tracked are modifiable via considereddirections and considerednames. 
The dictionary of dictionaries of probabilities is stored in a pickle file (markovprobabilities.pickle) for use by the generator.
"""

import sys
import os
import glob
import pickle

from itertools import chain, combinations

def train_for_markovprobs(picklefile, folderlist):
	"""Generates a pickle file for holding generated markov probabilities of tile occurrences"""
	levelreadins = [] #list of levels (each level a list of rows) and level names
	
	#Load levels
	for folder in folderlist:	
		for levelFile in glob.glob(f"{folder}/*.txt"):
			print ("Reading in: " + levelFile)
			with open(levelFile) as rows:
				level = [row.rstrip("\n") for row in rows if not row.isspace()]
			levelreadins.append((level, levelFile))


	#Extract Markov Random Field Counts from Levels
	markovCounts = {}# Dictionary of (x-1, y), (x-1, y+1), (x, y+1)
	for level, levelname in levelreadins:		#For each level
		print ("Processing: " + levelname)
		maxY = len(level)
		maxX = len(level[0])
		for y in range(maxY-1, -1, -1):			#For each (x, y) position in the level
			for x in range(0, maxX):
				east = " "
				northeast = " "
				north = " "
				northwest = " "
				west = " "
				southwest = " "
				south = " "
				southeast = " "

				canwest = (x>0)
				caneast = (x<maxX-1)
				cannorth = (y>0)
				cansouth = (y<maxY-1)

				if caneast:
					east = level[y][x-1]
				
				if cannorth and caneast:
					northeast = level[y-1][x-1]

				if cannorth:
					north = level[y-1][x]
				
				if cannorth and canwest:
					northwest = level[y-1][x-1]

				if canwest:
					west = level[y][x-1]

				if canwest and cansouth:
					southwest = level[y+1][x-1]

				if cansouth: 
					south = level[y+1][x]

				if cansouth and caneast:
					southeast = level[y+1][x+1]			

				def powerset(iterable):
					"powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
					s = list(iterable)
					return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

				#Which directions are tracked for the markov model
				#Add directions to this to track additional cardinal directions.
				considereddirections = [east, west, southwest, south, southeast]
				considerednames = ["E", "W", "SW", "S", "SE"]

				keys = []
				key_values = powerset(considereddirections)
				key_prefixes = [" ".join(keyname) + ": " for keyname in powerset(considerednames)]
				for index in range(len(key_values)):
					prefix = key_prefixes[index]
					value = "".join(key_values[index])
					keys.append(prefix + value)

				#Augment markov probabilities
				for key in keys:
					if not key in markovCounts.keys():
						markovCounts[key] = {}
				for key in keys:
					if not level[y][x] in markovCounts[key].keys():
						markovCounts[key][level[y][x]] = 0
					markovCounts[key][level[y][x]] +=1.0

	#Normalize markov counts
	markovProbabilities = {}
	for key in markovCounts.keys():
		markovProbabilities[key] = {}
		sumVal = 0
		for key2 in markovCounts[key].keys():
			sumVal+=markovCounts[key][key2]
		for key2 in markovCounts[key].keys():
			markovProbabilities[key][key2] = markovCounts[key][key2]/sumVal

	#store the markov counts to a pickle file for use by the generator.
	pickle.dump(markovProbabilities, open(picklefile, "wb"))

if __name__ == "__main__":
	workingfolder = "./LevelGenAW"
	picklefile = f"{workingfolder}/markovprobabilities.pickle"
	traindirs = [f"{workingfolder}/AWBW/Processed"]
	train_for_markovprobs(picklefile, traindirs)
	markovProbabilities = pickle.load(open(picklefile, "rb"))
	print(markovProbabilities)