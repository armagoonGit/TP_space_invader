class Alien:

    def __init__ (self):
        self.max=300
        self.min=0
        self.x=150
        self.y=20

    def mouvement(self,dir):
        if dir=="droite":
            self.x=self.x+1
        elif dir=="gauche":
            self.x=self.x-1
    
    #def tir(self):
     #   projectile= projectile(self.x,self.y,ally)
