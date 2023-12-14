import time, cmds
import menu
import debug, lookup, game, coly, mode
import lineput
import startu
import logln

#mode.load()
#time.sleep(10)

#START-DEBUG 
time.sleep(2)

#clear = lambda: os.system('cls')
print("")
startu.p()
menu.show()
lineput.loop = True
while lineput.loop:
  lineput.prv()

