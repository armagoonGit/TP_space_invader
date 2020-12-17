import random

class bonus:
    def__init__(self):
    self.y=500
    dir=random.randint(0,1)
    if dir==1:
        self.dir=1
        self.x=0
    else:
        self.dir=-1
        self.x=500

    def mouvement(self)
            self.x=self.x+self.dir
            if self.x<0 or self.x>500:
                destroy(self)
            