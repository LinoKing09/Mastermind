import coly as c

def red(text):
  print(c.color.RED + str(text) + c.color.END)

def yellow(text):
  print(c.color.YELLOW + str(text) + c.color.END)

def green(text):
  print(c.color.GREEN + str(text) + c.color.END)

def cyan(text):
  print(c.color.CYAN + str(text) + c.color.END)

def bold(text):
  print(c.color.BOLD + str(text) + c.color.END)