from random import randint

class bonus:
    def __init__ (self):
<<<<<<< HEAD
        self.rayon = 20
        self.y = 10
=======
        self.y=20
>>>>>>> 85a9614f877380de162ffa36f533bbc1b8d96a8b
        direction=randint(0,1)
        if direction==1:
            self.dir=1
            self.x=-10
        else:
            self.dir=-1
            self.x=1000

    def mouvement(self):
            self.x=self.x+self.dir*2
