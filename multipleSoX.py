''' Multiple SOX by Virtualzio/Sanalzio '''
from sys import argv
from tkinter import filedialog as fd
from json import loads, dumps
from colorama import Fore, init
from os import system, getcwd, path, listdir, walk

init()
system('title Smdcut for goldsrc')
print(Fore.YELLOW + f"\n\n                  Multiple So{Fore.RESET}und e{Fore.YELLOW}X{Fore.RESET}change")
print("    A utility tool for organizing audio files in multiples.\n")

if len(argv)==2 and (argv[1].lower()=="help" or argv[1]=="?"):
    print(Fore.GREEN + "    Usage" + Fore.RESET + ": multipleSoX.exe <file/dir1> <file/dir2> ...")
    print("    Or you can simply drag and drop the files or directorys you want to cut into " + Fore.GREEN + "multipleSoX.exe" + Fore.RESET + ".\n\n")
    exit(0)

thdir=None

if ":" in argv[0]: thdir=path.dirname(argv[0])
else: thdir=getcwd()

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
    print("Organizing \""+Fore.LIGHTBLUE_EX+path.basename(file)+Fore.RESET+"\" file...")
    system(f"{config['sox-dir']} {config['additional-global-options']} {config['additional-format-options']} {file}{fops} {outfile}")
    print(Fore.GREEN+"Saved \""+Fore.LIGHTBLUE_EX+path.basename(file)+Fore.GREEN+"\" file.\n"+Fore.RESET)

def nor(dirpath):
    for filename in listdir(dirpath):
        for ftype in config["input-types"]:
            if filename.lower().endswith(ftype.lower()): files.append(path.join(dirpath, filename).replace("/","\\"))

def ano(dirpath):
    walks=walk(dirpath)
    for root, dirs, filenames in walks:
        for filename in filenames:
            for ftype in config["input-types"]:
                if filename.lower().endswith(ftype.lower()): files.append(path.join(root, filename).replace("/","\\"))

if len(argv)<2:
    dirpath = fd.askdirectory(title="Select Directory", initialdir=config["start-path"])
elif len(argv)==2: dirpath = argv[1]
else:
    for arg in argv:
        if ":" in arg:
            if path.isdir(arg):
                if config["include-subfolders"]:
                    ano(arg)
                else:
                    nor(arg)
            else:
                fileyesok(arg)

if dirpath:
    if path.isdir(dirpath):
        if config["include-subfolders"]:
            ano(dirpath)
        else:
            nor(dirpath)
        for file in files:
            fileyesok(file)
    else:
        fileyesok(dirpath)