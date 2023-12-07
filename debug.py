import coly as c
mode =False
def write(message):
  if mode == True:
    print(c.color.YELLOW + str(message) + c.color.END)