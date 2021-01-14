import time
from random import random

class Alien:

    def __init__ (self, x, y, rayon, winStreak):
        self.speed = 1 + winStreak
        self.direction = 1
        self.x = x
        self.y = y
        self.rayon = rayon
        self.fireChance = 0 + winStreak * 0.01

    def mouvement (self, infoMov):
        if infoMov["newRow"] == True:
            self.direction *= -1
            self.y += 20 

        self.x +=  self.direction * self.speed * infoMov["speed"]
        
        tire=random() * 100 + self.fireChance

        if tire>=99.9:
            return(True) #cree un projo
        return(False)

