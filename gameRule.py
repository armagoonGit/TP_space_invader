#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier classe des regles du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : les mouvement des alien en fct de infoMov. save la speed ?
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from time import sleep
from threading import Event

from vaisseau import vaisseau
from alien import Alien
from moduGraphique import fenetre
from projectile import projectile

class gameRule:
    def __init__(self):
        self.affichage = fenetre(self)
        
        self.nbAlien = 56

        self.alien = []
        self.idAlien = []
        self.alienGene()
        
        self.missile = []
        self.idMissile = []
        
        self.ship = vaisseau()
        self.idship=""
    
    def start(self):
        self.affichage.go()
        
    def alienGene(self):
        h = int( self.affichage.can.cget('height') ) - 200
        w = int( self.affichage.can.cget('width') ) - 100
        cursorX = 100
        cursorY = 100

        for i in range(self.nbAlien):
            self.alien.append( Alien(cursorX, cursorY) )
            alien = self.alien[-1]
            self.idAlien.append( self.affichage.can.create_oval(alien.x, alien.y, alien.x + 20, alien.y + 20,width=1,outline='red',fill='blue') )
            
            cursorX += 100
            if cursorX >= w:
                cursorY += 40
                cursorX = 100


    def initialisationObj(self):
        self.idship=self.affichage.can.create_oval(self.ship.x,self.ship.y,self.ship.x+50,self.ship.y+50,width=1,outline='red',fill='blue')
        self.affichage.can.focus_set()
        self.affichage.can.bind('<Key>',lambda x:self.pinput(x))
        self.turn()

    def turn(self):
        infoMov = self.adaptMovement()
        index = 0
        
        for el in zip(self.missile, self.idMissile):
            rmShoot1 = el[0].mouvement()
            self.affichage.can.coords(el[1], el[0].x, el[0].y, el[0].x + 10, el[0].y + 10)

            rmShoot2 = self.missileTouche(el[0])

            if rmShoot1 == True or rmShoot2 == True :
                self.affichage.can.delete( self.idMissile[index])
                self.missile.pop(index)
                self.idMissile.pop(index)
    
            index += 1
                
        for el in zip(self.alien, self.idAlien) :

            addShoot = el[0].mouvement( infoMov ) #mouvement de l'alien 
            self.affichage.can.coords(el[1] ,el[0].x, el[0].y, el[0].x + 20, el[0].y + 20 ) #affichage de l'alien avec un rond moche
            
            if addShoot == True:
                self.missile.append( projectile(el[0].x + 5, el[0].y + 20, self.affichage.height , "foe") )
                missile = self.missile[-1]
                self.idMissile.append( self.affichage.can.create_oval(missile.x, missile.y, missile.x + 10, missile.y + 10,width=1,outline='green',fill='green') )
                
                

        self.affichage.fen.after(20, self.turn)
        
    def adaptMovement(self):
        w = int( self.affichage.can.cget('width') )
        res = {}
        res["speed"] = (len(self.alien) / self.nbAlien) / ( len(self.alien) / 2 ) #vitesse max pour un seul alien est de 2
        res["newRow"] = False
        
        for alien in self.alien :
            nextPosX = alien.x + alien.direction * 10
            
            if nextPosX >= w or nextPosX <= 0:
                res["newRow"] = True
                return(res)

        return(res)
    
    def pinput(self,event):
        touche=event.keysym
        if touche=='Left':
            self.ship.mouvement("gauche")
        elif touche=='Right':
            self.ship.mouvement("droite")
        elif touche=='space':
            self.missile.append( projectile(self.ship.x + 5, self.ship.y - 20, self.affichage.height, "ally") )
            missile = self.missile[-1]
            self.idMissile.append( self.affichage.can.create_oval(missile.x, missile.y, missile.x + 10, missile.y + 10,width=1,outline='green',fill='green') )
        self.affichage.can.coords(self.idship,self.ship.x,self.ship.y,self.ship.x+50,self.ship.y+50)
        self.affichage.fen.after(20)

    def missileTouche(self, missile):
        index = 0
        
        if ( (self.ship.x - missile.x)**2 + (self.ship.y - missile.y)**2 )**0.5 <= 10:
            self.affichage.can.delete( self.idship )
            self.affichage.message.config( text = "Votre vaiseau est detruit" )
            self.affichage.lowLife()
    
        
        for alien in self.alien:
            if missile.shooter == "ally" and ( (alien.x - missile.x)**2 + (alien.y - missile.y)**2 )**0.5 <= 10:
                self.affichage.can.delete( self.idAlien[index])
                self.alien.pop(index)
                self.idAlien.pop(index)
                
                return(True)
            index += 1
        return(False)
           

a = gameRule()

a.start()


