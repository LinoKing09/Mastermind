import game, cmds
import coly as c
import debug
import mode
import logln

def do(cmdline):
  if debug.mode == None:
    debug.mode = False
  debug.write("checking input")
  if cmdline.isnumeric():
    debug.write("-> guess")
    debug.write(game.created_game)
    if game.created_game == True:
      if game.limit != 0:
        if len(str(cmdline)) == int(cmds.difficulty):
          game.guess(str(cmdline))
        elif len(str(cmdline)) > int(cmds.difficulty):
          logln.red(f"Guess too long! Please only type in {str(cmds.difficulty)} digits")
        elif len(str(cmdline)) < int(cmds.difficulty):
          logln.red(f"Guess too short! Please type in {str(cmds.difficulty)} digits")
    else:
      logln.red(f"Game not started yet!")
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
    elif cmdline.startswith("set limit "):
      if cmdline.split(" ", 3)[2] == "0":
        game.limit = None
      elif cmdline.split(" ", 3)[2] == " " or cmdline.split(" ", 3)[2] == "":
        logln.red("Value not valid!")
      else:
        try:
          cmds.set_lim(int(cmdline.split(" ", 3)[2]))
          cmds.lists["set limit ..."]
        except Exception as e:
          logln.red(f"Value not valid!  \n{str(e)}")
      return "continue"
    elif cmdline.startswith("set level "):
      cmds.set_dif(cmdline.split(" ", 3)[2])
      cmds.lists["set level ..."]
      return "continue"
    elif cmdline.startswith("set mind "):
      if game.cheating == True:
        moechtegernguess = cmdline.split(" ", 3)[2]
        if moechtegernguess.isnumeric():
          if len(moechtegernguess) == cmds.difficulty:
            game.digits = ([*moechtegernguess])
            print("done")
        else:
          logln.red("Value must be numeric!")
      elif game.cheating == False:
        logln.red("Enable cheats to set mind!")
      return "continue"
    elif cmdline.startswith("read mind"):
      if game.created_game == True:
        if game.cheating == True:
          digs = []
          for digis in game.digits:
            digs.append(int(digis))
          print(digs)
          return "continue"
        else:
          logln.red("Enable cheats to read mind!")
          return "continue"
      else:
        logln.red("Start the game to read mind!")
        return "continue"
        
    elif cmdline.startswith("cheats"):
      if game.created_game == False or game.created_game == True:
        try:
          cheata = cmdline.split(" ", 2)[1].lower()
        except IndexError:
          if game.cheating == False:
            game.cheating = True
            cheata = " "
          elif game.cheating == True:
            game.cheating == False
            cheata = " "
          print("done")
        else:    
          if cheata == "on":
            game.cheating = True
            game.cheated = True
          elif cheata == "off":
            game.cheating = False
            if game.created_game == False:
              game.cheated = False
          elif cheata == " ":
            if game.cheating == False:
              game.cheating = True
              if game.created_game == False:
                game.cheated = True
            elif game.cheating == True:
              game.cheating == False
              game.cheated = False
          if cheata == "on" or cheata == "off" or cheata == " ":
            print("done")
          else:
            logln.red("Parameter not valid!")
        finally:
          return "continue"
      else:
        logln.red("Game currently running!")
        return "continue"
        
    elif cmdline.startswith("set mode "):
      mode.load(cmdline.split(" ", 3)[2])
      return "continue"
      
    try:
      debug.write(type(cmdline))
      cmds.lists[str(cmdline)]()
    except Exception as e:
      logln.red(f"No such command '{str(cmdline)}' \n{str(e)}")
      debug.write(
          type(e).__name__,          # TypeError
          __file__,                  # /tmp/example.py
          e.__traceback__.tb_lineno  # 2
      )
     
