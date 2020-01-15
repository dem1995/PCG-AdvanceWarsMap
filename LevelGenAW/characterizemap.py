import csv
import glob
import os


conversionrules = {}
conversionrules[1] = 'P'
conversionrules[2] = 'M'
conversionrules[3] = 'W'
conversionrules[4]	='═'
conversionrules[5]	='║'
conversionrules[6]	='¤'
conversionrules[7]	='╔'
conversionrules[8]	='╗'
conversionrules[9]	='╝'
conversionrules[10]	='╚'
conversionrules[11]	='╦'
conversionrules[12]	='╣'
conversionrules[13]	='╩'
conversionrules[14]	='╠'
conversionrules[15]	='═'
conversionrules[16]	='║'
conversionrules[17]	='•'
conversionrules[18]	='┏'
conversionrules[19]	='┓'
conversionrules[20]	='┛'
conversionrules[21]	='┗'
conversionrules[22]	='┳'
conversionrules[23]	='┫'
conversionrules[24]	='┻'
conversionrules[25]	='┣'
conversionrules[26]	='╍'
conversionrules[27]	='╏'
conversionrules[28] = 'O'
conversionrules[29] = '⬓'
conversionrules[30] = '⬒'
conversionrules[31] = '◧'
conversionrules[32] = '◨'
conversionrules[33] = 'S' 
conversionrules[34] = '🤍'
conversionrules[35] = '⬜'
conversionrules[36] = '♢'
conversionrules[37] = '🍚'
conversionrules[38] = '🧡'
conversionrules[39] = '🟧'
conversionrules[40] = '🔶'
conversionrules[41] = '🟠'
conversionrules[42] = '🌟'
conversionrules[43] = '💙'
conversionrules[44] = '🟦'
conversionrules[45] = '🔷'
conversionrules[46] = '🔵'
conversionrules[47] = '🌙'



for levelfile in glob.glob("./LevelGenAW/AWBW/Original/*.csv"):
	with open(levelfile) as csv_file:
		levelname = os.path.basename(levelfile)[:-4]
		with open(f"./LevelGenAW/AWBW/Processed/{levelname}.txt") as outfile:
			#Convert tile numbers in CSV to symbols
			csv_reader = csv.reader(csv_file, delimiter=',')
			line_count = 0
			for row in csv_reader:
				for numstring in row:
					number = int(numstring)

					
			print(row)
