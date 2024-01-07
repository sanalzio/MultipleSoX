''' Multiple SOX by Virtualzio/Sanalzio '''
import sys
from tkinter import filedialog as fd
from json import loads, dumps
import os
thdir=None
if ":" in sys.argv[0]: thdir=os.path.dirname(sys.argv[0])
else: thdir=os.getcwd()
dirpath = None
files=[]
config=None
try:
    with open(thdir+"\\config.json", "r") as f:
        readd=f.read()
        if readd=="":
            raise Exception("config yooh!")
        config = loads(readd)
except:
    config = {
        "sox-dir":"",
        "start-path":"/",
        "include-subfolders":True,
        "input-types":["wav", "mp3", "ogg"],
        "output-type":"",
        "additional-global-options":"",
        "additional-format-options":""
    }
    with open(thdir+"\\config.json", "w") as f:
        f.write(dumps(config))
if config["sox-dir"]=="":
    config["sox-dir"]=thdir+"\\sox\\sox.exe"
def fileyesok(file):
    fops=""
    for k, v in config.items():
        if k.lower().startswith("default-"):
            fops += f" --{k.replace('default-','')} {v}"
    outfile=file
    if config["output-type"]!="":
        outfile=file[:-len(file.split(".").pop())]+config["output-type"]
    os.system(f"{config['sox-dir']} {config['additional-global-options']} {config['additional-format-options']} {file}{fops} {outfile}")
if len(sys.argv)<2:
    dirpath = fd.askdirectory(title="Select Directory", initialdir=config["start-path"])
else:
    if sys.argv[1].startswith("\"") and sys.argv[1].endswith("\""): dirpath = sys.argv[1][1:-1]
    else: dirpath = sys.argv[1]
if os.path.isdir(dirpath):
    if config["include-subfolders"]:
        walk=os.walk(dirpath)
        for root, dirs, filenames in walk:
            for filename in filenames:
                for ftype in config["input-types"]:
                    if filename.lower().endswith(ftype.lower()): files.append(os.path.join(root, filename).replace("/","\\"))
    else:
        for filename in os.listdir(dirpath):
            for ftype in config["input-types"]:
                if filename.lower().endswith(ftype.lower()): files.append(os.path.join(dirpath, filename).replace("/","\\"))
    for file in files:
        fileyesok(file)
else:
    fileyesok(dirpath)