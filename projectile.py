class projectile:
    def __init__ (self, x, y, yMax, shooter):
        self.x = x
        self.y = y
        self.yMax = yMax

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

    def collision(self):
        pass
    #if len( canvas.find_overlapping(canvas.coords(self)[0], canvas.coords(self)[1], canvas.coords(self)[2], canvas.coords(self)[3]) ) > 1:
         #   destroy(canvas.find_overlapping(canvas.coords(self)[0],canvas.coords(self)[1],canvas.coords(self)[2],canvas.coords(self)[3])[1])
            #plutot que [1], on peut récupérer les indexs dans la liste et on teste, selon les indexs si l'objet est un ennemi, le joueur, un shelter ou un missile -> pn doit tout détruire après.

        
