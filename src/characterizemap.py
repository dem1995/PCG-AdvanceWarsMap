import csv
import glob
import os
from random import randint
from tilenumbers import Player, TileType, Tile

def getplayers(iterable_map):
	players = set()
	for row in iterable_map:
		for numstring in row:
			number = int(numstring)
			player = Tile(number).player
			if player is not None:
				players.add(Tile(number).player)
	return players

def get_conversion(iterable_map):
	players = getplayers(iterable_map)
	players = list(players)
	orange_playnum = randint(0, 1)
	blue_playnum = 1-orange_playnum
	convert_to = {players[orange_playnum]: Player.ORANGE, players[blue_playnum]: Player.BLUE}
	convert_player = lambda tile, playerto: playerto.tiles[tile.tiletype]
	conversion_method = lambda tile: convert_player(tile, convert_to[tile.player])
	return conversion_method


for levelfile in glob.glob("./LevelGenAW/AWBW/Original/*.csv"):
	with open(levelfile) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		print(f"The players originally were {getplayers(csv_reader)}")
	with open(levelfile) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		convert = get_conversion(csv_reader)

	with open(levelfile) as csv_file:
		levelname = os.path.basename(levelfile)[:-4]
		with open(f"./LevelGenAW/AWBW/Processed/{levelname}.txt", 'w') as outfile:
			#Convert tile numbers in CSV to symbols
			csv_reader = csv.reader(csv_file, delimiter=',')
			for row in csv_reader:
				for numstring in row:
					tile = Tile(int(numstring))
					if tile.player is not None:
						tile = convert(tile)
					if tile.symbol is None:
						print(tile)
					outfile.write(tile.symbol)
				outfile.write('\n')
