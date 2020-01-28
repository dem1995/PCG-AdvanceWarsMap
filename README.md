# PCG-AdvanceWarsMap
A program for generating Advance Wars maps using markov mappings.

To generate levels, from the folder directory run python ./src/main.py. This will automatically populate ./LevelGenAW/GeneratedLevels with maps.

The program comprises three main parts: map conversion, training, and generation/visualization.

Conversion:
Maps are taken and converted from member creations at Advance Wars by Web at https://awbw.amarriner.com/, where they are essentially accessible as .csv files of tiles mapped to numbers. Using tilenumbers.py, we take these files and convert them to symbols for the markov model to learn from. We additionally process the maps so that the various factions AWBW supports are, in a given two-player map, converted to Orange Star and Blue Moon properties.
The conversion itself is performed by running characterizemap.py, which by default will convert .csv representations of levels in LevelGenAW/AWBW/Original and place the results in LevelGenAW/AWBW/Processed. It should be noted that there may be some maps for which the process fails; the author hand-generated the conversions of AWBW's tile numbers, but did not encounter all of the possible ones; for example, what tile numbers 58-80 (if they are used) refer to is currently unknown.

Training:
Training is performed by train.py, which scans the processed level files for patterns and determines the probabilities with which, given a tile pattern about a tile, a given tile occurs. Specifically, it keeps a dictionary of patterns; the keys are the subsets of the powerset of the ordered set of tiles adjacent to the given tile; the values themselves refer to dictionaries of probabilities. For example, given a plains tile to the west and an ocean tile to the east, the trainer would (proportionately, scaling the probabilities contained in the dictionary corresponding to ocean-to-the-east, plains-to-the-west so that their sum was one) increment the probability of the tile between a western plains and eastern ocean tile to be whatever that tile was (perhaps an east-facing coast). Which cardinal directions' probability-dictionaries are tracked are modifiable in train.py. The dictionary of dictionaries of probabilities is stored in a pickle file (markovprobabilities.pickle) for use by the generator.

Generation:
Generation is performed by generate.py using the markov probability pickle created by training.py. Generation involves proceeding from the bottom-left of a map and generating, left-to-right, row-by-row, the rows of a map. To do this, it checks which tiles have already been generated; if there are any, it uses keys corresponding to those tiles in those directions to determine the probability of a new tile being something. With some modification introduced by adding in a random value, it chooses the most probable tile under the circumstances at each step, or generates an unknown tile (represented by an upside-down smiley face) if there are no stored probabilities.

It should be noted that the directions prioritized by the generator are west and south, as some of the tiles require adjacent tiles (for example, non-terminal pipes must eventually either end in a terminal pipe or go off the map, and curved river tiles only exist adjacent to two orthogonal river tiles). The generated maps are text files where each symbol is a tile, with symbols chosen by generalization.py using tilenumbers.py.

Visualization uses visualize.py, which itself refers to tilenumbers.py to figure out which tile images correspond to each tile symbol in the genreated files.