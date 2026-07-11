# Healthy Programmer

# Water - water.mp3 - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 50 min
# Physical activity - physical.mp3 every - 90 min - ExDone - log

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("Mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    water_time = 40 * 60
    eyes_time = 50 * 60
    phy_time = 90 * 60


    while True:
        if time() - init_water > water_time:
            print("Water Drinking Time. Enter 'Drank water' to stop the alarm.")
            musiconloop('water.mp3', 'Drank water')
            init_water = time()
            log_now("Drank Water at")


        if time() - init_eyes > eyes_time:
            print("Eye Exercise Time. Enter 'Eyes done' to stop the alarm.")
            musiconloop('eyes.mp3', 'Eyes done')
            init_eyes = time()
            log_now("Eyes Relaxed at")

        if time() - init_exercise > phy_time:
            print("Physical Activity Time. Enter 'Phy Act done' to stop the alarm.")
            musiconloop('physical.mp3', 'Phy Act done')
            init_exercise = time()
            log_now("Physical Activity done at")
