import menu
import os
import sys
import game
import debug
import coly as c
import mode

x=None
y=None
clear = lambda: os.system('cls')

def default(cl=True):
  if cl==True:
    clear()
  global difficulty,limit
  difficulty = 3
  game.limit = None
  debug.mode = False
  if cl==False:
    print("done")
    
def game_over():
  game.guesses_remain = game.limit if game.guesses_remain is not None else None
  game.guesses_made = 0
  game.created_game = False
  game.digits = []

def set_dif(value):
  global difficulty
  if game.created_game == False: 
    difficulty = value
    print("done")
  else:
    print(c.color.RED + "Game currently running!" + c.color.END)
    debug.write("tried to change difficulty")
def set_lim(value):
  game.limit = value
  game.guesses_remain = value
  debug.write("Limit:" + str(game.limit))
  print("done")

def debug_mode_change():
  if debug.mode == False:
    if game.created_game == True:
      print(c.color.RED + "Turning on Debug Mode was denied!" + c.color.END)
      debug.write("The game is currently running! If you turn on Debug mode now you'll probably see the results.")
      yesno = input("Continue? Y/N ")
      if yesno.upper() == "Y":
        debug.mode = True
        print(c.color.YELLOW + "Debug Mode on" + c.color.END)
      elif yesno.upper() == "N":
        debug.write("back")
    else:
      debug.mode = True
      print(c.color.YELLOW + "Debug Mode on" + c.color.END)
  elif debug.mode == True:
    debug.mode = False
    print("Debug Mode off")
  else:
    print(c.color.RED + "An error occured!" + c.color.END)
    
def startup():
  default()
  game_over()

lists = {
        f"load mode": lambda: mode.load(),
        f"set level ...": lambda: print("",end=""), 
        f"set limit ...": lambda: print("",end=""),
        f"show level": lambda: print(difficulty),
        f"show limit": lambda: print(game.limit),
        f"guesses remain": lambda: print(f"{game.guesses_remain} guesses remaining"),
        f"guesses made": lambda: print(f"{game.guesses_made} guesses made"),
        f"help": menu.show,
        f"debug mode": lambda: debug_mode_change(),
        f"clear": clear,
        f"reset": lambda: default(False),
        f"fail": lambda: game.fail(),
        f"start": lambda: game.create(),
        f"exit": lambda: sys.exit()
}