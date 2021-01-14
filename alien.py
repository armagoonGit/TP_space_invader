import time
from random import random

class Alien:

    def __init__ (self, x, y, rayon):
        self.speed = 1
        self.direction = 1
        self.x = x
        self.y = y
        self.rayon = rayon

    def mouvement (self, infoMov):
        if infoMov["newRow"] == True:
            self.direction *= -1
            self.y += 20 

        self.x +=  self.direction * 1 * infoMov["speed"]
        
        tire=random() * 100

        if tire>=99.9:
            return(True) #cree un projo
        return(False)

    def tire(self):
        projectile= projectile(self.x,self.y,ennemi)
        
        
        
        

