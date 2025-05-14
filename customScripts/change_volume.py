import subprocess


def decVolume(qtile):
    subprocess.run(["amixer","-D","pulse","sset","Master","10%-"])
def incVolume(qtile):
    subprocess.run(["amixer","-D","pulse","sset","Master","10%+"])
def muteVolume(qtile):
    subprocess.run("amixer -D pulse set Master 1+ toggle".split())
