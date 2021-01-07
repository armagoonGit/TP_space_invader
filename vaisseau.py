class vaisseau:

    def __init__ (self):
        self.max=900
        self.min=50

        self.x=450
        self.y=600

    def mouvement(self,dir):
        if dir=="droite":
            if self.x<self.max:
                self.x=self.x+10

        elif dir=="gauche":
            if self.x>self.min:
                self.x=self.x-10

    
    def tir(self):
        projectile= projectile(self.x,self.y,ally)
