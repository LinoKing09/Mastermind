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

def keyden():
  desc = input("")
  if desc.upper() ==  "Y":
    creation()
  elif desc.upper() == "N":
    debug.write("back to the roots")
  else:
      print(c.color.RED + "Answer not valid!" + c.color.END)
def create():
  if created_game == False:
    if debug.mode == False:
      creation()
    elif debug.mode == True:
      print(c.color.RED + "Starting the game was denied!" + c.color.END)
      debug.write("Debugging mode still turned on! You may see the results.")
      print("Continue? Y/N ")
      keyden()
    else:
      print(c.color.RED + "Error!" + c.color.END)
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
  debug.write("now guessing!")
  global created_game, guesses_remain, guesses_made
  if created_game == True:
    icp = 0
    ccn = 0
    theory = ([*theory])
    check = []
    queue = []
    
    if guesses_remain == 0:
      print(c.color.RED + "You have no guesses left" + c.color.END)
      fail()
    if limit != None:
      debug.write("Guesses remaining:" + str(guesses_remain))
      guesses_remain = int(guesses_remain)
      guesses_made = int(guesses_made)
      guesses_remain -= 1
    guesses_made += 1
    debug.write("guesses made:"+str(guesses_made))

    print(theory, end=" - ")
    
    """
    a = 0
    while a < len(digits):
      debug.write("Loop a: " + str(a))
      b = 0
      while b < len(theory):
        #a1  b1,b2,b3
        if digits[a] == theory[b]:
          debug.write(f"matching: {digits[a]}={theory[b]}")
          if b in check:
            debug.write("pass: b in check")
            pass
          else:
            if a == b:
              icp += 1
              print(theory)
              gotem.append(theory[b])
              print(theory)
              check.append(b)
              debug.write(f"exact match: {digits[a]}/{a} - {theory[b]}/{b}")
              pass
            else:
              getem.append(theory[b])
              #notem.pop(b)
              debug.write(notem,a,b,theory,theory2)
              debug.write("correct number in false position!",theory[b],"/",b)
              check.append(b)
        b += 1
      a += 1

      if b == cmds.difficulty:
        pass

    try_digits = set(digits)
    getemset = set(getem)
    emgot = list(getemset) + list(gotem)
    notincluded = []
    for somenumberssomebodyguessed in theory:
      if somenumberssomebodyguessed not in digits:
        notincluded.append(somenumberssomebodyguessed)
    debug.write(f"notincluded: {notincluded}")
    debug.write(f"notem: {notem}")
    debug.write(emgot)
    debug.write(check)
    
    for them in getemset:
      if them not in gotem:
        ccn += 1
    for noway in check:
      print(check[noway])
      print(notem)
      notem.pop(check[noway])
    if notem == []:
      if icp + ccn + len(notem) != cmds.difficulty:
        ccn += int(cmds.difficulty)-icp-ccn
        """

    a = 0
    while a < len(theory):
      debug.write("Loop a: " + str(a))
      b = 0
      while b < len(digits):
        debug.write("Loop b: ",b)
        if theory[a] == digits[b]:
          if b in check:
            continue
          else:
            if a == b:
              check.append(b)
              icp += 1
            else:
              queue.append(b)
        b += 1
      a += 1

    for waiting in queue:
      if queue[waiting] not in check:
        check.append(queue[waiting])
        ccn += 1
      
    debug.write(f"{icp}/{cmds.difficulty}")
    if icp == int(cmds.difficulty):
      print(c.color.GREEN + str(icp), " ", str(ccn) + c.color.END)
      logln.green(f"attempts:     {guesses_made}")
      if limit != None:
        print(c.color.GREEN + f"guesses left: {guesses_remain}" + c.color.END)
      for youhavebeengoingtowwinthegame in range(3):
        print(c.color.GREEN + "you win!" + c.color.END, end="\r")
        time.sleep(0.7)
        print("        ", end="\r")
        time.sleep(0.7)
      print(c.color.GREEN + "you win!" + c.color.END)
      time.sleep(0.25)
      created_game = False
      cmds.game_over()
    else:
      if guesses_remain == 0:
        fail()
      else:
        print(icp, " ", ccn)


def fail():
  if created_game == True:
    print(c.color.RED + str(digits) + c.color.END)
    print(c.color.RED + f"attempts:     {guesses_made}" + c.color.END)
    if limit != None:
      print(c.color.RED + f"guesses left: {guesses_remain}" + c.color.END)
    for ohmanwhatabummeryoulostthegame in range(3):
      print(c.color.RED + "FAIL!" + c.color.END, end="\r")
      time.sleep(0.7)
      print("     ", end="\r")
      time.sleep(0.7)
    print(c.color.RED + "FAIL!" + c.color.END)
    cmds.game_over()
    pass

  else:
    print(c.color.RED + "Start a game to fail!" + c.color.END)
