import cmds
import menu
import debug
import lookup
import lineput

#mode.load()
#time.sleep(10)

#START-DEBUG 
"""
cmds.startup()
game.create()
time.sleep(1)
"""
#clear = lambda: os.system('cls')
cmds.startup()
menu.show()
loop = True
while loop:
  lineput.prv()

