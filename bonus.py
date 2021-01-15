from random import randint

class bonus:
    def __init__ (self):

        self.rayon = 20
        self.y = 20

        direction=randint(0,1)
        if direction==1:
            self.dir=1
            self.x=-10
        else:
            self.dir=-1
            self.x=1000

    def mouvement(self):
            self.x=self.x+self.dir*2
