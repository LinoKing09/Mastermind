import json
import coly as c
def get_modys():
  try:
    with open("mode_storage.json","r") as file_stor:
      mode_storager = json.load(file_stor)
  except Exception:
    print(c.color.RED + "ERROR: Couldn't load default modes!" + c.color.END)
  else:
    for key in mode_storager:
      print(f"set mode {key}")

def show():
  print("cmds")
  print("_____________")
  get_modys()
  print("load mode          load your custom mode as json file")
  print("set level [x]      set difficulty to custom, x digits")
  print("set limit [y]      set the number of guesses allowed")
  print("set mind [z]       set the number to guess")
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