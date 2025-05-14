import subprocess

def decBrightness(qtile):
    subprocess.run('brightnessctl set 10%-'.split())
def incBrightness(qtile):
    subprocess.run('brightnessctl set +10%'.split())
