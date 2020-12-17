import time
import random

class Alien:

    def __init__ (self):
        self.speed=1
        self.direction=1
        self.max=300
        self.min=0
        self.x=100
        self.y=100

    def mouvement (self):

        self.x=self.x+self.direction*10
        if self.x==self.max or self.x==self.min:
            self.y=self.y-10
            self.direction=-self.direction
        tire=random.randint(self.speed,90)
        if tire>=85:
            self.tire()


    def tire(self):
        projectile= projectile(self.x,self.y,ennemi)
        

        
        
        

