import logln
mode =False
def write(*message):
  if mode == True:
    message = " ".join(list(message))
    logln.yellow(message)