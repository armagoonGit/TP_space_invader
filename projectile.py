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
