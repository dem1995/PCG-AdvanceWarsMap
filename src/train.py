import sys
import os
import glob
import pickle

def train_for_markovprobs(picklefile, folderlist):
	levels = [] #list of dictionaries, each dictionary a level

	for folder in folderlist:
		#Load SMB Levels
		for levelFile in glob.glob(f"{folder}/*.txt"):
			print ("Processing: "+levelFile)
			with open(levelFile) as fp:
				level = {}
				y = 0
				for line in fp:
					level[y] = line
					y+=1
				levels.append(level)

	#Extract Markov Random Field Counts from Levels

	markovCounts = {}# Dictionary of (x-1, y), (x-1, y+1), (x, y+1)
	for level in levels: 
		maxY = len(level)-1
		for y in range(maxY, -1, -1):
			for x in range(0, len(level[y])):
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

				if not key in markovCounts.keys():
					markovCounts[key] = {}
				if not level[y][x] in markovCounts[key].keys():
					markovCounts[key][level[y][x]] = 0
				markovCounts[key][level[y][x]] +=1.0

	#Normalize markov counts
	markovProbabilities = {}


	includenewline = True
	for key in markovCounts.keys():
		if includenewline or not "\n" in key:
			markovProbabilities[key] = {}
			sumVal = 0
			for key2 in markovCounts[key].keys():
				if includenewline or not "\n" in key2:
					sumVal+=markovCounts[key][key2]
			for key2 in markovCounts[key].keys():
				if includenewline or not "\n" in key2:
					markovProbabilities[key][key2] =markovCounts[key][key2]/sumVal

	pickle.dump(markovProbabilities, open(picklefile, "wb"))

if __name__ == "__main__":
	picklefile = "markovprobabilities.pickle"
	train_for_markovprobs(picklefile)