import random as rand
import cmds
import time
import coly as c
import debug
import logln

global created_game,digits
created_game = False
digits = []
limit = None
guesses_made = 0
guesses_remain = 0
cheating = False
cheated = False

def keyden():
  desc = input("")
  if desc.upper() ==  "Y":
    creation()
  elif desc.upper() == "N":
    debug.write("back to the roots")
  else:
      logln.red("Answer not valid!")
def create():
  if created_game == False:
    if cheating == True:
      if debug.mode == False:
        print("Cheats are still enabled. Continue? Y/N ",end = "")
        inner = input("")
        if inner.upper() == "Y" or inner.upper() == "":
          creation()
      elif debug.mode == True:
        logln.red("Starting the game was denied!")
        debug.write("Debugging mode still turned on! You may see the results.")
        print("Continue? Y/N ")
        keyden()
      else:
        logln.red("Error!")
    else:
      creation()
  else:
    print("Game already running!")


def creation():
  global created_game,digits
  if created_game == False:
    if digits == []:
      digits = []
      for mnm in range(int(cmds.difficulty)):
        digits.append(str(rand.randint(0, 9)))
    debug.write(digits)
    created_game = True
    print("Started game! Type in your guess!")
  else:
    print("Game already running!")


def guess(theory):
  if cheating == True:
    cheated = True
  else: 
    cheated = False
  try:
    debug.write("now guessing!")
    global created_game, guesses_remain, guesses_made
    if created_game == True:
      icp = 0
      ccn = 0
      theory = ([*theory])
      check = []
      queue = []
      
      if guesses_remain == 0:
        logln.red("You have no guesses left")
        fail()
      if limit != None:
        debug.write("Guesses remaining:" + str(guesses_remain))
        guesses_remain = int(guesses_remain)
        guesses_made = int(guesses_made)
        guesses_remain -= 1
      guesses_made += 1
      debug.write("guesses made:"+str(guesses_made))
  
      print(theory, end=" - ")
      
  
      a = 0
      while a < len(theory):
        debug.write("Loop a: " + str(a))
        b = 0
        while b < len(digits):
          debug.write("Loop b: ",b)
          if theory[a] == digits[b]:
            if b in check:
              b+=1
              continue
            else:
              if a == b:
                check.append(b)
                icp += 1
              else:
                queue.append(b)
          b += 1
        a += 1
        
      waiting = 0
      while waiting < len(queue):
        debug.write(waiting,queue)
        if queue[waiting] not in check:
          check.append(queue[waiting])
          ccn += 1
        waiting += 1
        
      debug.write(f"{icp}/{cmds.difficulty}")
      if icp == int(cmds.difficulty):
        logln.green(str(icp)+ "   "+ str(ccn))
        if cheated == True:
          logln.red("used cheats")
        else:
          logln.green("no cheats")
        logln.green(f"attempts:     {guesses_made}")
        if limit != None:
          logln.green(f"guesses left: {guesses_remain}")
        for youhavebeengoingtowwinthegame in range(3):
          print(c.color.GREEN + "you win!" + c.color.END, end="\r")
          time.sleep(0.7)
          print("        ", end="\r")
          time.sleep(0.7)
        logln.green("you win!")
        time.sleep(0.25)
        created_game = False
        cmds.game_over()
      else:
        if guesses_remain == 0:
          fail()
        else:
          print(icp, " ", ccn)

  except Exception as e:
    printable = (
      type(e).__name__, 
      __file__, 
      e.__traceback__.tb_lineno
    )
    print("")
    logln.red(printable)
    
def fail():
  if created_game == True:
    logln.red(str(digits))
    logln.red(f"attempts:     {guesses_made}")
    if limit != None:
      logln.red(f"guesses left: {guesses_remain}")
    for ohmanwhatabummeryoulostthegame in range(3):
      print(c.color.RED + "FAIL!" + c.color.END, end="\r")
      time.sleep(0.7)
      print("     ", end="\r")
      time.sleep(0.7)
    logln.red("FAIL!")
    cmds.game_over()
    pass

  else:
    logln.red("Start a game to fail!")
