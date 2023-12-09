import game, cmds
import coly as c
import debug
import mode

def do(cmdline): 
  debug.write("checking input")
  if cmdline.isnumeric():
    debug.write("-> guess")
    debug.write(game.created_game)
    if game.created_game == True:
      if game.limit != 0:
        if len(str(cmdline)) == int(cmds.difficulty):
          game.guess(str(cmdline))
        elif len(str(cmdline)) > int(cmds.difficulty):
          print(
              c.color.RED +
              f"Guess too long! Please only type in {str(cmds.difficulty)} digits"
              + c.color.END)
        elif len(str(cmdline)) < int(cmds.difficulty):
          print(
            c.color.RED +
            f"Guess too short! Please type in {str(cmds.difficulty)} digits"
            + c.color.END)
    else:
      print(c.color.RED + f"Game not started yet!" + c.color.END)
  else:
    debug.write("-> command")
    cmdline = str(cmdline)
    if cmdline.startswith(" "):
      cmdline = cmdline.replace(" ","",1)
    if cmdline == "":
      return "continue"
    elif cmdline == "restart":
      cmds.game_over()
      game.creation()
      return "continue"
    elif cmdline == "exit":
      return "break"
    elif cmdline.startswith("set limit"):
      if cmdline.split(" ", 3)[2] == "0":
        game.limit = None
      elif cmdline.split(" ", 3)[2] == " " or cmdline.split(" ", 3)[2] == "":
        print(c.color.RED + "Value not valid!" + c.color.END)
      else:
        try:
          cmds.set_lim(int(cmdline.split(" ", 3)[2]))
          cmds.lists["set limit ..."]
        except Exception as e:
          print(c.color.RED + f"Value not valid!  \n{str(e)}" + c.color.END)
      return "continue"
    elif cmdline.startswith("set level"):
      cmds.set_dif(cmdline.split(" ", 3)[2])
      cmds.lists["set level ..."]
      return "continue"
    elif cmdline.startswith("set mind"):
      if debug.mode == True:
        moechtegernguess = cmdline.split(" ", 3)[2]
        if moechtegernguess.isnumeric():
          if len(moechtegernguess) == cmds.difficulty:
            game.digits = ([*moechtegernguess])
            print("done")
        else:
          print(c.color.RED + "Value must be numeric!" + c.color.END)
        return "continue"
      elif debug.mode == False:
        print(c.color.RED + "Turn on debug mode to set mind!" + c.color.END)
        return "continue"
    elif cmdline.startswith("set mode "):
      mode.load(cmdline.split(" ", 3)[2])
      return "continue"
      
    try:
      debug.write(type(cmdline))
      cmds.lists[str(cmdline)]()
    except Exception as e:
      print(c.color.RED + f"No such command '{str(cmdline)}' \n{str(e)}" +
            c.color.END)
      debug.write(
          type(e).__name__,          # TypeError
          __file__,                  # /tmp/example.py
          e.__traceback__.tb_lineno  # 2
      )
     
