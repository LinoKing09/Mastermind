from tkinter import filedialog
import json
import cmds
import debug as db
import lookup
import time
import debug
import lineput


def dumpling(file):
  with open(file, "r") as file_jsn:
    data_jsn = json.load(file_jsn)
  for value in data_jsn:
    if data_jsn[value] == "None":
      data_jsn[value] = None
    elif data_jsn[value] == "True":
      data_jsn[value] = True
    elif  data_jsn[value] == "False":
      data_jsn[value] = False
      
  debug.write(data_jsn)
  cmds.set_dif(data_jsn["level"])
  cmds.set_lim(data_jsn["limit"])
  db.mode = data_jsn["debug_mode"]
  if data_jsn["cmds"] != "":
    if "," in data_jsn["cmds"]:
      commys = data_jsn["cmds"].split(",")
      debug.write("yes")
    else:
      commys = list(data_jsn["cmds"])
    for thermosbottle in range(len(commys)):
      debug.write("hello:", thermosbottle)
      prvexit = lineput.prv(commys[thermosbottle])
      if prvexit == "break":
        lineput.loop = Falsevv
        break

def load(tech=""):
  if tech == "":
    jsn_cfg = filedialog.askopenfilename(
        title="Select a JSON file",
        filetypes=[("JSON files", "*.json")]
    )
    debug.write(str(jsn_cfg) + str(type(jsn_cfg)))
    if str(jsn_cfg)!="":
      dumpling(jsn_cfg)

  else:
    with open("mode_storage.json","r") as file_stor:
      mode_storager = json.load(file_stor)
     
    jsn_cfg = mode_storager[tech]
    print(jsn_cfg)
    dumpling(jsn_cfg)

  #set limit,level,debug,cmds
