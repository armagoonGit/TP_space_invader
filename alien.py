import time
import random

class Alien:

    def __init__ (self, x, y):
        self.speed = 1
        self.direction = 1
        self.x = x
        self.y = y

    def mouvement (self, newRow):
        if newRow == True:
            self.direction *= -1
            self.y += 50 

        self.x = self.x + self.direction * 10

        
        tire=random.randint(self.speed,90)
        """
        if tire>=85:
            self.tire()
"""
"""
    def tire(self):
        projectile= projectile(self.x,self.y,ennemi)
        
"""
        
        
        

