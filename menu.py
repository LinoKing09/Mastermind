import json
def get_modys():
  with open("mode_storage.json","r") as file_stor:
    mode_storager = json.load(file_stor)
  for key in mode_storager:
    print(f"set mode {key}")

def show():
  print("MASTERMIND")
  print("cmds")
  print("_____________")
  get_modys()
  print("load mode          load your custom mode as json file")
  print("set level [x]      set difficulty to custom, x digits")
  print("set limit [y]      set the number of guesses allowed")
  print("show level         show the current difficulty")
  print("show limit         show the limit of guesses allowed")
  print("guesses remain     show the number of guesses remaining")
  print("guesses made       shows the guesses already made")
  print("help               show this menu")
  print("debug mode         debug the game")
  print("clear              clear the screen")
  print("reset              reset settings to default")
  print("fail               give up")
  print("start              start the game")
  print("restart            restart the game")
  print("exit               exit the game")
  print("_____________")
  print("")
  print("")