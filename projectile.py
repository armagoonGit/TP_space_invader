from tkinter import canvas
import time

class projectile:
    def __init__ (self,x,y,type):
        self.x=x
        self.y=y
        self.ymax==500
        if type==ennemie:
            self.type=-1
        elif type==ally:
            self.type=1
        self.speed=1

    def mouvement(self):
        self.y=self.y+self.type
        if self.y==self.ymax:
            destroy(self)

    def collision(self):
        if len(canvas.find_overlapping(canvas.coords(self)[0],canvas.coords(self)[1],canvas.coords(self)[2],canvas.coords(self)[3]))>1:
            destroy(canvas.find_overlapping(canvas.coords(self)[0],canvas.coords(self)[1],canvas.coords(self)[2],canvas.coords(self)[3])[1])
            #plutot que [1], on peut récupérer les indexs dans la liste et on teste, selon les indexs si l'objet est un ennemi, le joueur, un shelter ou un missile -> pn doit tout détruire après.

        
