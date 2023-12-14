import logln
mode =False

def write(*message):
  if mode == True:
    message_str = " ".join(str(msg) for msg in message)
    logln.yellow(message_str)