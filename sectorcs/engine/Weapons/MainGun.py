# Ryan Schumacher
# MainGun.py
#
# The standard gun controlled by the hero unit

import pygame, os, sys

from pygame.locals import *
from Weapon import Weapon

sys.path.append("../")
import Constants, Paths
from Constants import *
from Paths import *

class MainGun(Weapon):
    def __init__(self, canvas):
        Weapon.__init__(self, MAINGUN_DMG, MAINGUN_STAM, LASER_GREEN, 
                        LASER_BLUE, LASER_FIRE, LASER_EXPL, MAINGUN_SPEED, MAINGUN_COOLDOWN, TYPE_L, canvas)
