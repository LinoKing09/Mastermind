import random as rand
import cmds
import time
import coly as c
import debug

created_game = False
limit = None
guesses_made = 0
guesses_remain = 0


def create():
  if debug.mode == False:
    creation()
  elif debug.mode == True:
    print(c.color.RED + "Starting the game was denied!" + c.color.END)
    debug.write("Debugging mode still turned on! You may see the results.")
    yesno = input("Continue? Y/N ")
    if yesno.upper() == "Y":
      creation()
    elif yesno.upper() == "N":
      debug.write("back to the roots")
    else:
      print(c.color.RED + "Answer not valid!" + c.color.END)
  else:
    print(c.color.RED + "Error!" + c.color.END)


def creation():
  global digits
  digits = []
  for mnm in range(int(cmds.difficulty)):
    digits.append(str(rand.randint(0, 9)))
  debug.write(digits)
  global created_game
  created_game = True
  print("Started game! Type in your guess!")


def guess(theory):
  debug.write("now guessing!")
  global created_game, guesses_remain, guesses_made
  if created_game == True:
    icp = 0
    ccn = 0
    theory = ([*theory])
    check = []
    getem = []
    gotem = []
    emgot = []
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
              gotem.append(theory[b])
              debug.write(f"exact match: {digits[a]}/{a} - {theory[b]}/{b}")
              pass
            else:
              getem.append(theory[b])
              debug.write(f"correct number in false position! {theory[b]}/{b}")
              #check.append(b)
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

    for them in getemset:
      if them not in gotem:
        ccn += 1


    debug.write(f"{icp}/{cmds.difficulty}")
    if icp == int(cmds.difficulty):
      print(c.color.GREEN + str(icp), " ", str(ccn) + c.color.END)
      print(c.color.GREEN + f"attempts:     {guesses_made}" + c.color.END)
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
