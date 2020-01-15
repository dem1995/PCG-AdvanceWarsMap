import csv
import glob
import os

conversionrules = {}
conversionrules[28] = 'S'
conversionrules[31] = 'd'



for levelfile in glob.glob("./LevelGenAW/AWBW/Original/*.csv"):
	with open(levelfile) as csv_file:
		levelname = os.path.basename(levelfile)[:-4]
		with open(f"./LevelGenAW/AWBW/Processed/{levelname}.txt") as outfile:
			#Convert tile numbers in CSV to symbols
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
					
			
			print(row)
