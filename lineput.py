import debug
import lookup
import main

def prv(cmdline = ""):
  cmdline = cmdline.lower()
  if cmdline == "":
    print("> ", end="")
    cmdline = input("").lower()
  comms = []
  if "," in cmdline:
    debug.write("more than one command detected!")
    comms = cmdline.split(",")
    debug.write(comms)
  else:
    comms.append(cmdline)
    debug.write(comms)

  for yoiligeit in range(len(comms)):
    debug.write(comms[yoiligeit])
    retcmd = lookup.do(comms[yoiligeit])
    if retcmd == "break":
      debug.write("breakpoint")
      main.loop = False
      break
    elif retcmd == "continue":
      continue
