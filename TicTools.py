#!/usr/bin/python3

from sys import argv, stderr
from os import listdir,mkdir
from os.path import  isfile
from importlib import import_module

#CONSTANTES
ERROR = "\x1b[31m\x1b[1m/!\\\x1b[0m ERROR :"
PLG = "plugins"
#Header
print(r"""
__/\\\\\\\\\\\\\\\______________________/\\\\\\\\\\\\\\\______________________________/\\\\\\_________________        
 _\///////\\\/////______________________\///////\\\/////______________________________\////\\\_________________       
  _______\/\\\________/\\\_____________________\/\\\______________________________________\/\\\_________________      
   _______\/\\\_______\///______/\\\\\\\\_______\/\\\___________/\\\\\________/\\\\\_______\/\\\_____/\\\\\\\\\\_     
    _______\/\\\________/\\\___/\\\//////________\/\\\_________/\\\///\\\____/\\\///\\\_____\/\\\____\/\\\//////__    
     _______\/\\\_______\/\\\__/\\\_______________\/\\\________/\\\__\//\\\__/\\\__\//\\\____\/\\\____\/\\\\\\\\\\_   
      _______\/\\\_______\/\\\_\//\\\______________\/\\\_______\//\\\__/\\\__\//\\\__/\\\_____\/\\\____\////////\\\_  
       _______\/\\\_______\/\\\__\///\\\\\\\\_______\/\\\________\///\\\\\/____\///\\\\\/____/\\\\\\\\\__/\\\\\\\\\\_ 
        _______\///________\///_____\////////________\///___________\/////________\/////_____\/////////__\//////////__
""")

if("plugins" not in listdir(".")):
    mkdir("plugins")
    print("You dont have any plugins installed... You should consider install some... You can use our super plugin manager with python3 ticpip.py -h")

plugins = listdir("./"+PLG)

def _import(plugin,argv):
    try:
        if not isfile(plugin) and plugin in plugins: plugin = plugin + '.' + plugin
        import_module(PLG+'.' + plugin).main(argv)
    except:
        print(f"{ERROR} {plugin} is not a plugin",file=stderr)

if len(argv) < 2 :
    print(f"{ERROR} Missing Argument\n",file=stderr)
    exit()


if '-p' in argv : _import(argv[argv.index('-p')+1],argv)
else :
    print("Liste des plugins :\n- "+' \n- '.join(plugins))

   
