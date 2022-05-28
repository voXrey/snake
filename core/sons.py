import os
import random
import playsound

manger_dossier = './core/assets/sons/manger'
manger_sons = [os.path.join(manger_dossier, manger_son) for manger_son in os.listdir(manger_dossier)]
def manger():
    son = random.choice(manger_sons)
    playsound.playsound(son, block=False)

psss_son = './core/assets/sons/autres/avancer.wav'
def psss():
    playsound.playsound(psss_son, block=False)

mort_son = './core/assets/sons/autres/mort.wav'
def mort():
    playsound.playsound(mort_son, block=False)
