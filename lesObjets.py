"""
que fait : fichier des objets du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : 
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from random import random, randint

class vaisseau:

    def __init__ (self, rayon, yMax):
        self.max= int(yMax) - rayon
        self.min=20

        self.x=450
        self.y=600
        self.rayon = rayon
        self.id = ""

    def mouvement(self,dir):
        if dir=="droite":
            if self.x<self.max:
                self.x=self.x+10

        elif dir=="gauche":
            if self.x>self.min:
                self.x=self.x-10
   
    def addId(self, ID):
        self.id = ID

class cShelter:
    def __init__(self,x,y, rayon):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.id = ''
    
    def addId(self, ID):
        self.id = ID

class cAlien:
    """
    les nosu avons 5 type d'aliens
    leur probabilite de faire feu augmente en focntion de alien type 
    et de winstreak
    """
    def __init__ (self, x, y, rayon, winStreak, alienType):
        self.speed = 1 + winStreak
        self.direction = 1
        self.x = x
        self.y = y
        self.rayon = rayon
        self.fireChance = winStreak * 0.01 + (alienType / 4) * 0.01
        self.point = 100 *( alienType + 1 )
        self.id = ''

    def mouvement (self, infoMov):
        if infoMov["newRow"] == True:
            self.direction *= -1
            self.y += 20 

        self.x +=  self.direction * self.speed * infoMov["speed"]
    
    def shoot(self,tireprob):
        tire=random() * 100 + self.fireChance + tireprob*0.01 - 0.3
    
        if tire>=99.9:
            return(True) #cree un projo
        return(False)
        
    def addId(self, ID):
        self.id = ID
        
class projectile:
    def __init__ (self, x, y, yMax, rayon, shooter):
        self.x = x
        self.y = y
        
        self.yMax = yMax
        self.rayon = rayon
        self.id = ""

        self.speed=1
        self.shooter = shooter
        
        if shooter == "foe":
            self.direction = 1
        elif shooter == "ally":
            self.direction = -1

    def mouvement(self):
        self.y = self.y + self.direction*10
        
        if self.y == self.yMax or self.y <= 0:
            return(True)
        return(False)

    def addId(self, ID):
        self.id = ID


class bonus:
    def __init__ (self):

        self.rayon = 20
        self.y = 20
        self.point = 1000
        self.id = ""

        direction=randint(0,1) # le bonsu travers de gauche a droit ou inversment
        if direction==1:
            self.dir=1
            self.x=-10
        else:
            self.dir=-1
            self.x=1000

    def mouvement(self):
        self.x=self.x+self.dir*2
    
    def addId(self, ID):
        self.id = ID
        

