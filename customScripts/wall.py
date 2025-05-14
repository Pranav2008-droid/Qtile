import time
import subprocess
import os
import random

l = subprocess.run(['ls','../../Pictures/wallpapers'],capture_output=True,text=True).stdout.split("\n")[0:-1]

def change_bg(x):
    subprocess.run(['feh','--bg-fill','../../Pictures/wallpapers/'+x])
def change_ran_bg():
    r = random.randint(0,len(l))
    change_bg(l[r])
def cont():
    while True:
        for i in l:
            change_bg(i)
            time.sleep(5)



