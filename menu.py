import json
import os
import logln
def get_modys():
  try:
    with open("mode_storage.json","r") as file_stor:
      mode_storager = json.load(file_stor)
  except Exception:
    logln.red("ERROR: Couldn't load default modes!")
  else:
    for key in mode_storager:
      if str(key) == "easy":
        print(f"set mode ",end="")
        logln.green("easy")
      elif str(key) == "medium":
        print(f"set mode ",end="")
        logln.yellow("medium")
      elif str(key) == "hard":
        print(f"set mode ",end="")
        logln.red("hard")
      else:
        print(f"set mode ",end="")
        logln.cyan(key)

def querypr():
  size = os.get_terminal_size()
  for rar in range(int(size.columns)):
    print("-",end="")
  print("")

def show():
  logln.bold("MASTERMIND")
  print("")
  logln.bold("CMDS")
  querypr()
  get_modys()
  print("load mode            load your custom mode as json file")
  print("set level [x]        set difficulty to custom, x digits")
  print("set limit [y]        set the number of guesses allowed")
  print("set mind [z]         set the number to guess",end="")
  logln.blue("*")
  print("read mind            show the number to guess",end="")
  logln.blue("*")
  print("show level           show the current difficulty")
  print("show limit           show the limit of guesses allowed")
  print("guesses remain       show the number of guesses remaining")
  print("guesses made         shows the guesses already made")
  print("debug mode           debug the game",end="")
  logln.blue("*")
  print("cheats on/off        ",end="") 
  logln.blue("*",ende="")
  print("enable cheats")
  print("help                 show this menu")
  print("clear                clear the screen")
  print("reset                reset settings to default")
  print("fail                 give up")
  print("start                start the game")
  print("restart              restart the game")
  print("exit                 exit the game")
  querypr()
  print("")
  print("")