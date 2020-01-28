"""
Generation is performed using the markov probability pickle created by training.py. 
Generation involves proceeding from the bottom-left of a map and generating, left-to-right, row-by-row, the rows of a map. 
To do this, it checks which tiles have already been generated; if there are any, it uses keys corresponding to those tiles in those directions to determine the probability of a new tile being something. 
With some modification introduced by adding in a random value, it chooses the most probable tile under the circumstances at each step, or generates an unknown tile (represented by an upside-down smiley face) if there are no stored probabilities.
"""

import sys
import os
import glob
import random
import pickle
import numpy as np
import itertools
from collections import defaultdict

def generate_level(levelname, markovProbabilities, outputdirectory):
	"""Generates Advance Wars levels in .txt format probabilistically using the provided markovProbabilities"""
	print(f"Generating level: {levelname}")

	level = {}

	maxY = 25
	maxX = 25
	unvisitedspaces = list(itertools.product(range(maxX), range(maxY-1, -1, -1)))
	#random.shuffle(unvisitedspaces)

	tiles = defaultdict(lambda: "*")

	for x, y in unvisitedspaces:
		#for x in range(0, maxX):
		east = " "
		northeast = " "
		north = " "
		northwest = " "
		west = " "
		southwest = " "
		south = " "
		southeast = " "

		caneast = (tiles[(x+1, y)]!="*")
		cannorth = (tiles[(x, y-1)]!="*")
		canwest = (tiles[(x-1, y)]!="*")
		cansouthwest = (tiles[(x-1, y+1)]!="*")
		cansouth = (tiles[(x, y+1)]!="*")
		cansoutheast = (tiles[(x+1, y+1)]!="*")


		if canwest:
			west = tiles[(x-1, y)]

		if cansouthwest:
			southwest = tiles[(x-1, y+1)]

		if cansouth: 
			south = tiles[(x, y+1)]

		if cansoutheast:
			southeast = tiles[(x+1, y+1)]

		key0 = 'W SW S SE:' + west+southwest+south+southeast
		key1 = 'W SW S:' + west+southwest+south
		key2 = 'W S SE:' + west+south+southeast
		key3 = 'W SW SE:' + west+southwest+southeast
		key4 = 'SW S SE:' + south+southwest+southeast
		key5 = 'W S: ' + west+south
		key6 = 'W: ' + west
		key7 = 'S: ' + south
		keys = np.array([key0, key1, key2, key3, key4, key5, key6, key7])
		keys_set_1 = keys[[0, 1, 2, 5]]
		keys_set_2 = keys[[6, 7]]
		keys_set_3 = keys[[3, 4]]
		keys_set_4 = keys_set_2
		
		for key in keys_set_1:
			match_found = False
			if key in markovProbabilities.keys():
				#print(key)
				randomSample = random.uniform(0, 1)
				currValue = 0.0
				for key2 in markovProbabilities[key]:
					if randomSample>=currValue and randomSample<currValue+markovProbabilities[key][key2]:
						tiles[(x, y)]=key2
						match_found=True
						break
					currValue+=markovProbabilities[key][key2]
			if match_found:
				break

		if not match_found:
			match_found = False
			if keys_set_2[0] in markovProbabilities.keys() and keys_set_2[1] in markovProbabilities.keys():
				#print(key)
				randomSample = random.uniform(0, 1)
				currValue = 0.0
				for key2 in (markovProbabilities[keys_set_2[0]].keys() & markovProbabilities[keys_set_2[1]].keys()):
					if randomSample >= currValue and randomSample < currValue+markovProbabilities[keys_set_2[0]][key2]:
						tiles[(x, y)]=key2
						match_found=True
						break
					currValue+=markovProbabilities[keys_set_2[0]][key2]


		if not match_found:
			for key in keys_set_3:
				match_found = False
				if key in markovProbabilities.keys():
					print(key)
					randomSample = random.uniform(0, 1)
					currValue = 0.0
					for key2 in markovProbabilities[key]:
						if randomSample>=currValue and randomSample<currValue+markovProbabilities[key][key2]:
							tiles[(x, y)]=key2
							match_found=True
							break
						currValue+=markovProbabilities[key][key2]
				if match_found:
					break

		if not match_found:
			tiles[(x, y)]='*'
		#if set(keys).isdisjoint(set(markovProbabilities.keys())):
		

	with open(f"{outputdirectory}/{levelname}.txt", "w") as the_file:
		for y in range(0, maxY):
			for x in range(0, maxX):
				the_file.write(tiles[(x, y)])
			the_file.write("\n")