import cmds
import menu
import debug, lookup, game, coly, mode
import lineput
import startu
import logln

#mode.load()
#time.sleep(10)

#START-DEBUG 
"""
cmds.startup()
game.create()
time.sleep(1)
"""
#clear = lambda: os.system('cls')
logln.bold("MASTERMIND")
print("")
startu.p()
menu.show()
loop = True
while lineput.loop:
  lineput.prv()

