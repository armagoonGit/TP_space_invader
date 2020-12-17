#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier classe des regles du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : tout
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from time import sleep

from alien import Alien
from moduGraphique import fenetre

class gameRule:
    def __init__(self):
        self.affichage = fenetre(self)
        
        self.nbAlien = 56
        self.alien = []
        self.idAlien = []
        self.alienGene()
        
        self.ship = "a pas"
    
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
        self.turn()

    def turn(self):
        newRow = self.checkNewRow()

        for el in zip(self.alien, self.idAlien) :

            el[0].mouvement( newRow )
            self.affichage.can.coords(el[1] ,el[0].x, el[0].y, el[0].x + 20, el[0].y + 20 )
            
        self.affichage.fen.after(50, self.turn)
        
    def checkNewRow(self):
        w = int( self.affichage.can.cget('width') )
        
        for alien in self.alien :
            nextPosX = alien.x + alien.direction * 10
            
            if nextPosX >= w or nextPosX <= 0:
                return(True)

        return(False)
            
        
        
a = gameRule()
print(a.affichage.can.cget('height') )
a.start()


