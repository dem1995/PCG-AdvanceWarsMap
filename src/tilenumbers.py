from enum import Enum, IntEnum, unique, auto

class Player(Enum):
	ORANGE	= auto() 
	BLUE	= auto()
	GREEN	= auto()
	YELLOW	= auto()
	RED		= auto()
	GREY	= auto()
	BLACK	= auto()
	BROWN	= auto()
	AMBER	= auto()
	JADE	= auto()
	COBALT	= auto()
	PINK	= auto()
	TEAL	= auto()
	PURPLE	= auto()
	ACID	= auto()
	WHITE	= auto()
	def __new__(cls, keycode, player=None, tiletype=None):
		obj = object.__new__(cls)
		obj._value_ = keycode
		obj.tiles = {}
		return obj


class TileType(Enum):
	DEFAULT	= auto()
	ROAD	= auto()
	RIVER	= auto()
	PIPE	= auto()
	AIRPORT	= auto()
	CITY	= auto()
	COMMS 	= auto()
	FACTORY = auto()
	HQ 		= auto()
	LAB		= auto()
	PORT	= auto()
	def __new__(cls, keycode, player=None, tiletype=None):
		obj = object.__new__(cls)
		obj._value_ = keycode
		obj.tiles = {}
		return obj

reverse_lookup = dict()

@unique
class Tile(IntEnum):
	UNKNOWN				= 0,	None, TileType.DEFAULT, '*', 'unknown'
	PLAINS				= 1,	None, TileType.DEFAULT, 'P', 'plains'
	MOUNTAIN			= 2,	None, TileType.DEFAULT, 'M', 'mountains'
	WOODS				= 3,	None, TileType.DEFAULT, 'W', 'woods'
	RIVER_EW			= 4,	None, TileType.RIVER, '═', 'river-ew'
	RIVER_NS			= 5,	None, TileType.RIVER, '║', 'river-ns'
	RIVER_C				= 6,	None, TileType.RIVER, '¤', 'river-nsew'
	RIVER_SE			= 7,	None, TileType.RIVER, '╔', 'river-se'
	RIVER_SW			= 8,	None, TileType.RIVER, '╗', 'river-sw'
	RIVER_NW			= 9,	None, TileType.RIVER, '╝', 'river-nw'
	RIVER_NE			= 10,	None, TileType.RIVER, '╚', 'river-ne'
	RIVER_SEW			= 11,	None, TileType.RIVER, '╦', 'river-sew'
	RIVER_NSW			= 12,	None, TileType.RIVER, '╣', 'river-nsw'
	RIVER_NEW			= 13,	None, TileType.RIVER, '╩', 'river-new'
	RIVER_NSE			= 14,	None, TileType.RIVER, '╠', 'river-nse'
	ROAD_EW				= 15,	None, TileType.ROAD, '━', 'road-ew'
	ROAD_NS				= 16,	None, TileType.ROAD, '┃', 'road-ns'
	ROAD_C 				= 17,	None, TileType.ROAD, '•', 'road-nsew'
	ROAD_SE				= 18,	None, TileType.ROAD, '┏', 'road-se'
	ROAD_SW				= 19,	None, TileType.ROAD, '┓', 'road-sw'
	ROAD_NW				= 20,	None, TileType.ROAD, '┛', 'road-nw'
	ROAD_NE				= 21,	None, TileType.ROAD, '┗', 'road-ne'
	ROAD_SEW			= 22,	None, TileType.ROAD, '┳', 'road-sew'
	ROAD_NSW			= 23,	None, TileType.ROAD, '┫', 'road-nsw'
	ROAD_NEW			= 24,	None, TileType.ROAD, '┻', 'road-new'
	ROAD_NSE			= 25,	None, TileType.ROAD, '┣', 'road-nse'
	BRIDGE_EW			= 26,	None, TileType.DEFAULT, '╍', 'bridge-ew'
	BRIDGE_NS			= 27,	None, TileType.DEFAULT, '╏', 'bridge-ns'
	OCEAN				= 28,	None, TileType.DEFAULT, 'O', 'ocean'
	SOUTH_FACING_BEACH	= 29,	None, TileType.DEFAULT, '🠹', 'beach-south-facing'
	NORTH_FACING_BEACH	= 30,	None, TileType.DEFAULT, '🠻', 'beach-north-facing'
	WEST_FACING_BEACH	= 31,	None, TileType.DEFAULT, '🠺', 'beach-west-facing'
	EAST_FACING_BEACH	= 32,	None, TileType.DEFAULT, '🠸', 'beach-east-facing'
	SHOAL				= 33,	None, TileType.DEFAULT, 'S', 'shoal'
	NEUTRAL_CITY		= 34,	None, TileType.CITY, 'E', 'city-neutral'
	NEUTRAL_FACTORY		= 35,	None, TileType.FACTORY, '▦', 'factory-neutral'
	NEUTRAL_AIRPORT		= 36,	None, TileType.AIRPORT, '⋄', 'airport-neutral'
	NEUTRAL_PORT		= 37,	None, TileType.PORT, '◍', 'port-neutral'
	ORANGE_CITY			= 38,	Player.ORANGE, TileType.CITY, 'Ⅎ', 'city-orange'
	ORANGE_FACTORY		= 39,	Player.ORANGE, TileType.FACTORY, '⬓', 'factory-orange'
	ORANGE_AIRPORT		= 40,	Player.ORANGE, TileType.AIRPORT, '⬙', 'airport-orange'
	ORANGE_PORT			= 41,	Player.ORANGE, TileType.PORT, '◒', 'port-orange'
	ORANGE_HQ			= 42,	Player.ORANGE, TileType.HQ, '⭐', 'hq-orange'
	BLUE_CITY			= 43,	Player.BLUE, TileType.CITY, 'F', 'city-blue'
	BLUE_FACTORY		= 44,	Player.BLUE, TileType.FACTORY, '◨', 'factory-blue'
	BLUE_AIRPORT		= 45,	Player.BLUE, TileType.AIRPORT, '⬗', 'airport-blue'
	BLUE_PORT			= 46,	Player.BLUE, TileType.PORT, '◑', 'port-blue'
	BLUE_HQ				= 47,	Player.BLUE, TileType.HQ, '☾', 'hq-blue'
	GREEN_CITY			= 48,	Player.GREEN, TileType.CITY
	GREEN_FACTORY		= 49,	Player.GREEN, TileType.FACTORY
	GREEN_AIRPORT		= 50,	Player.GREEN, TileType.AIRPORT
	GREEN_PORT			= 51,	Player.GREEN, TileType.PORT
	GREEN_HQ			= 52,	Player.GREEN, TileType.HQ
	YELLOW_CITY			= 53,	Player.YELLOW, TileType.CITY
	YELLOW_FACTORY		= 54,	Player.YELLOW, TileType.FACTORY
	YELLOW_AIRPORT		= 55,	Player.YELLOW, TileType.AIRPORT
	YELLOW_PORT			= 56,	Player.YELLOW, TileType.PORT
	YELLOW_HQ			= 57,	Player.YELLOW, TileType.HQ
	RED_CITY			= 81,	Player.RED, TileType.CITY
	RED_FACTORY			= 82,	Player.RED, TileType.FACTORY
	RED_AIRPORT			= 83,	Player.RED, TileType.AIRPORT
	RED_PORT			= 84,	Player.RED, TileType.PORT
	RED_HQ				= 85,	Player.RED, TileType.HQ
	GREY_CITY			= 86,	Player.GREY, TileType.CITY
	GREY_FACTORY		= 87,	Player.GREY, TileType.FACTORY
	GREY_AIRPORT		= 88,	Player.GREY, TileType.AIRPORT
	GREY_PORT			= 89,	Player.GREY, TileType.PORT
	GREY_HQ				= 90,	Player.GREY, TileType.HQ
	BLACK_CITY			= 91,	Player.BLACK, TileType.CITY
	BLACK_FACTORY		= 92,	Player.BLACK, TileType.FACTORY
	BLACK_AIRPORT		= 93,	Player.BLACK, TileType.AIRPORT
	BLACK_PORT			= 94,	Player.BLACK, TileType.PORT
	BLACK_HQ			= 95,	Player.BLACK, TileType.HQ
	BROWN_CITY			= 96,	Player.BROWN, TileType.CITY
	BROWN_FACTORY		= 97,	Player.BROWN, TileType.FACTORY
	BROWN_AIRPORT		= 98,	Player.BROWN, TileType.AIRPORT
	BROWN_PORT			= 99,	Player.BROWN, TileType.PORT
	BROWN_HQ			= 100, 	Player.BROWN, TileType.HQ
	PIPE_NS				= 101,	None, TileType.PIPE, '|', 'pipe-ns'
	PIPE_EW				= 102,	None, TileType.PIPE, '─', 'pipe-ew'
	PIPE_NE				= 103,	None, TileType.PIPE, '└', 'pipe-ne'
	PIPE_SE				= 104,	None, TileType.PIPE, '┌', 'pipe-se'
	PIPE_SW				= 105,	None, TileType.PIPE, '┐', 'pipe-sw'
	PIPE_NW				= 106,	None, TileType.PIPE, '┘', 'pipe-nw'
	PIPE_S				= 107,	None, TileType.PIPE, '╷', 'pipe-s'
	PIPE_W				= 108,	None, TileType.PIPE, '╴', 'pipe-w'
	PIPE_N				= 109,	None, TileType.PIPE,	'╵', 'pipe-n'
	PIPE_E				= 110,	None, TileType.PIPE, '╶', 'pipe-e'
	MISSILE_SILO		= 111,	None, TileType.DEFAULT, 'm', 'missile-silo'
	EMPTY_SILO			= 112,	None, TileType.DEFAULT, 'e', 'empty-silo'
	PIPE_SEAM_EW		= 113,	None, TileType.PIPE,	'╎', 'pipe-seam-ew'
	PIPE_SEAM_NS		= 114,	None, TileType.PIPE,	'╌', 'pipe-seam-ns'
	PIPE_SEAM_NS_RUPTURE= 115,	None, TileType.PIPE, 'ͷ', 'pipe-seam-ns-ruptured'
	PIPE_SEAM_EW_RUPTURE= 116,	None, TileType.PIPE, 'z', 'pipe-seam-ew-ruptured'
	AMBER_AIRPORT		= 117,	Player.AMBER, TileType.AIRPORT
	AMBER_FACTORY		= 118,	Player.AMBER, TileType.FACTORY
	AMBER_CITY			= 119,	Player.AMBER, TileType.CITY
	AMBER_HQ			= 120,	Player.AMBER, TileType.HQ
	AMBER_PORT			= 121,	Player.AMBER, TileType.PORT
	JADE_AIRPORT		= 122,	Player.JADE, TileType.AIRPORT
	JADE_FACTORY		= 123,	Player.JADE, TileType.FACTORY
	JADE_CITY			= 124,	Player.JADE, TileType.CITY
	JADE_HQ				= 125,	Player.JADE, TileType.HQ
	JADE_PORT			= 126,	Player.JADE, TileType.PORT
	NEUTRAL_COMMS_TOWER	= 133,	None, TileType.COMMS, 't', 'comms-tower-neutral'
	AMBER_LAB			= 138,	Player.AMBER, TileType.LAB
	BROWN_LAB			= 139,	Player.BROWN, TileType.LAB
	BLACK_LAB			= 140,	Player.BLACK, TileType.LAB
	BLUE_LAB			= 141,	Player.BLUE, TileType.LAB
	GREEN_LAB			= 142,	Player.GREEN, TileType.LAB
	GREY_LAB			= 143,	Player.GREY, TileType.LAB
	JADE_LAB			= 144,	Player.JADE, TileType.LAB
	NEUTRAL_LAB			= 145,	None, TileType.LAB, '⊢', 'lab-neutral' 
	ORANGE_LAB			= 146,	Player.ORANGE, TileType.LAB
	RED_LAB				= 147,	Player.RED, TileType.LAB
	YELLOW_LAB			= 148,	Player.YELLOW, TileType.LAB
	COBALT_AIRPORT		= 149,	Player.COBALT, TileType.AIRPORT
	COBALT_FACTORY		= 150,	Player.COBALT, TileType.FACTORY
	COBALT_CITY			= 151,	Player.COBALT, TileType.CITY
	COBALT_COMMS_TOWER	= 152,	Player.COBALT, TileType.COMMS
	COBALT_HQ			= 153,	Player.COBALT, TileType.HQ
	COBALT_LAB			= 154,	Player.COBALT, TileType.LAB
	COBALT_PORT			= 155,	Player.COBALT, TileType.PORT
	PINK_AIRPORT		= 156,	Player.PINK, TileType.AIRPORT
	PINK_FACTORY		= 157,	Player.PINK, TileType.FACTORY
	PINK_CITY			= 158,	Player.PINK, TileType.CITY
	PINK_COMMS_TOWER	= 159,	Player.PINK, TileType.COMMS
	PINK_HQ				= 160,	Player.PINK, TileType.HQ
	PINK_LAB			= 161,	Player.PINK, TileType.LAB
	PINK_PORT			= 162,	Player.PINK, TileType.PORT
	TEAL_AIRPORT		= 163,	Player.TEAL, TileType.AIRPORT
	TEAL_FACTORY		= 164,	Player.TEAL, TileType.FACTORY
	TEAL_CITY			= 165,	Player.TEAL, TileType.CITY
	TEAL_COMMS_TOWER	= 166,	Player.TEAL, TileType.COMMS
	TEAL_HQ				= 167,	Player.TEAL, TileType.HQ
	TEAL_LAB			= 168,	Player.TEAL, TileType.LAB
	TEAL_PORT			= 169,	Player.TEAL, TileType.PORT
	PURPLE_AIRPORT		= 170,	Player.PURPLE, TileType.AIRPORT
	PURPLE_FACTORY		= 171,	Player.PURPLE, TileType.FACTORY
	PURPLE_CITY			= 172,	Player.PURPLE, TileType.CITY
	PURPLE_COMMS_TOWER	= 173,	Player.PURPLE, TileType.COMMS
	PURPLE_HQ			= 174,	Player.PURPLE, TileType.HQ
	PURPLE_LAB			= 175,	Player.PURPLE, TileType.LAB
	PURPLE_PORT			= 176,	Player.PURPLE, TileType.PORT
	ACID_AIRPORT		= 181,	Player.ACID, TileType.AIRPORT
	ACID_FACTORY		= 182,	Player.ACID, TileType.FACTORY
	ACID_CITY			= 183,	Player.ACID, TileType.CITY
	ACID_COMMS_TOWER	= 184,	Player.ACID, TileType.COMMS
	ACID_HQ				= 185,	Player.ACID, TileType.HQ
	ACID_LAB			= 186,	Player.ACID, TileType.LAB
	ACID_PORT			= 187,	Player.ACID, TileType.PORT
	WHITE_AIRPORT		= 188,	Player.WHITE, TileType.AIRPORT
	WHITE_FACTORY		= 189,	Player.WHITE, TileType.FACTORY
	WHITE_CITY			= 190,	Player.WHITE, TileType.CITY
	WHITE_COMMS_TOWER	= 191,	Player.WHITE, TileType.COMMS
	WHITE_HQ			= 192,	Player.WHITE, TileType.HQ
	WHITE_LAB			= 193,	Player.WHITE, TileType.LAB
	WHITE_PORT			= 194,	Player.WHITE, TileType.PORT
	def __new__(cls, keycode, player=None, tiletype=None, symbol = None, filename=None):
		obj = int.__new__(cls, keycode)
		obj._value_ = keycode
		obj.player=player
		obj.tiletype = tiletype
		obj.symbol = symbol
		obj.filename = filename
		if player is not None:
			player.tiles[tiletype]=obj
		if tiletype is not None:
			tiletype.tiles[player]=obj

		reverse_lookup[symbol] = obj
		return obj

Tile.reverse_lookup=reverse_lookup


print(Player.BLUE.tiles)



































