from Map import Map
from Bot import Bot
from Game import Game
import importlib
import traceback



settings = {
	'mapName' : "map1.csv",
	'nrCols' : 30,
	'nrRows' : 30,
	'nrStains' : 3,
	'nrPillars' : 3,
	'nrWalls' : 3,
	'sizeStains' : 3,
	'sizePillars' : 3,
	'sizeWalls' : 6,
	'checkpoint' : [1,1],
}


MAX_STEPS = 1000
LATENCY = .1
VISUALS = True
CLS = True

botName = 'BruteBot'
module = importlib.import_module(botName)
cls = getattr(module, botName)

myMap = Map(settings)
bot = cls(settings)
if not getattr(bot, 'name', False):
	bot.setName(botName)
game = Game(bot, myMap, MAX_STEPS, LATENCY, VISUALS, CLS)


try:
	game.play()
except Exception:
	print("Encountered error: ", traceback.format_exc())