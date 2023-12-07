import random as rand
import cmds

def create():
    digits=[]
    for r in range(cmds.difficulty):
      digits.append(rand.randint(0,9))
    