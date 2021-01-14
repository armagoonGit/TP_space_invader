#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier classe des regles du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : 
        image
        affichage des message en bien
        cooldown message 

        new game
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from random import randint
from time import sleep
from threading import Event
from tkinter import PhotoImage

from vaisseau import vaisseau
from bonus import bonus
from shelter import shelter
from alien import Alien
from moduGraphique import fenetre
from projectile import projectile

class gameRule:
    def __init__(self):
        self.affichage = fenetre(self)
        self.affichage.can.image=[]
        
        self.winStreak = 0
        
        self.nbAlien = 100
        self.alien = []
        self.idAlien = []
        self.alienGene()
        self.alienim = PhotoImage(file='imagegif/alien1.gif')
        
        self.nbshelter =5*80
        self.Shelter=[]
        self.idShelter=[]
        self.ShelterGene()
        self.shelterim = PhotoImage(file='imagegif/bunker.gif')
        
        self.bonus = ""
        self.idBonus = ""
        self.bonusim = PhotoImage(file='imagegif/bonus.gif')
        
        self.missile = []
        self.idMissile = []
        self.bonusim = PhotoImage(file='imagegif/Projectile.gif')
        
        self.ship = ""
        self.idship=""
        self.shipim = PhotoImage(file='imagegif/vaisseau.gif')
        
        self.cooldown=0
        
    
    def start(self):
        self.affichage.go()

#les methodes de generation :

    def ShelterGene(self):
        h = int( self.affichage.can.cget('height') ) - 200
        w = int( self.affichage.can.cget('width') ) - 100
        cursorX = 105
        cursorY = 500

        for i in range(self.nbshelter):
            if cursorX>=w/7 and cursorX<=2*w/7 or cursorX>=3*w/7 and cursorX<=4*w/7 or cursorX>=5*w/7 and cursorX<=6*w/7:
                self.Shelter.append( shelter(cursorX, cursorY, 5) )
                Shelter = self.Shelter[-1]
                ray = Shelter.rayon
                self.idShelter.append( self.affichage.can.create_rectangle(Shelter.x + ray, Shelter.y + ray, Shelter.x - ray, Shelter.y - ray,fill='DarkOrchid1') )
            
            cursorX += 10
            if cursorX >= w:
                cursorY += 10
                cursorX = 105
        
    def alienGene(self):
        h = int( self.affichage.can.cget('height') ) - 200
        w = int( self.affichage.can.cget('width') ) - 100
        cursorX = 100
        cursorY = 100

        for i in range(self.nbAlien):
            self.alien.append( Alien(cursorX, cursorY, 17, self.winStreak) )
            
            alien = self.alien[-1]
            ray = alien.rayon
            
            self.idAlien.append( self.affichage.can.create_image(alien.x, alien.y, anchor='center', image= self.alienim))
            self.affichage.can.image.append(self.alienim)
        
            cursorX += 100
            if cursorX >= w:
                cursorY += 40
                cursorX = 100

    def initialisationObj(self):
        self.affichage.newGameBut.configure(relief="flat",text="fight !", command = "")
        
        self.ship = vaisseau(25)
        self.idship=self.affichage.can.create_oval(self.ship.x - self.ship.rayon, self.ship.y - self.ship.rayon, self.ship.x + self.ship.rayon, self.ship.y + self.ship.rayon,width=1,outline='red',fill='blue')
        
        self.affichage.can.focus_set()
        self.affichage.can.bind('<Key>',lambda x:self.pinput(x))
        
        self.turn()
        
    def respawnShip(self):
        self.affichage.newGameBut.configure(relief="flat",text="fight !", command = "")
        
        self.ship = vaisseau(25)
        self.idship=self.affichage.can.create_oval(self.ship.x - self.ship.rayon, self.ship.y - self.ship.rayon, self.ship.x + self.ship.rayon, self.ship.y + self.ship.rayon,width=1,outline='red',fill='blue')
    

    def turn(self):
        self.affichage. manageMessage()
        
        if self.cooldown>0:
            self.cooldown= self.cooldown-1
        
        infoMov = self.adaptMovement()

        index = 0
        for el in zip(self.missile, self.idMissile):
            rmShoot1 = el[0].mouvement()
            rmShoot2 = self.missileTouche(el[0])
            
            if rmShoot2 == "endGame": #coupe la recurciviter de la fonction en cas de game OVER
                return()
            
            elif rmShoot1 == True or rmShoot2 == True : #detruit le missile si il y a  eu un impact
                self.affichage.can.delete( self.idMissile[index])
                self.missile.pop(index)
                self.idMissile.pop(index)
    
            else: #fait bouger l'image du misisle
                self.affichage.can.coords(el[1], el[0].x - el[0].rayon , el[0].y - el[0].rayon, el[0].x + el[0].rayon, el[0].y + el[0].rayon)
            index += 1
                
        for el in zip(self.alien, self.idAlien) :

            addShoot = el[0].mouvement( infoMov ) #mouvement de l'alien 
            self.affichage.can.coords(el[1] ,el[0].x, el[0].y) #affichage de l'alien avec un rond moche
            
            if addShoot == True:
                self.missile.append( projectile(el[0].x , el[0].y, self.affichage.height, 5, "foe") )
                missile = self.missile[-1]
                ray = missile.rayon
                self.idMissile.append( self.affichage.can.create_oval(missile.x - ray, missile.y - ray, missile.x + ray, missile.y + ray,width=1,outline='green',fill='green') )
                
        if self.bonus == "": #si il n'y a pas deja de bonus. On en creer peut etre un
            bonusnb=randint(1000, 1000)   
            if bonusnb == 1000 :
                self.bonus=bonus()
                ray = self.bonus.rayon
                self.idBonus=self.affichage.can.create_oval(self.bonus.x - ray ,self.bonus.y - ray ,self.bonus.x + ray, self.bonus.y + ray,width=1,outline="blue",fill="lime")

        else: #si on a un bonus en jeu on le fait bouger
            if self.bonus.x <= 1000 and self.bonus.dir == 1 or self.bonus.x >= -10 and self.bonus.dir == -1:
                self.bonus.mouvement()
                ray = self.bonus.rayon
                self.affichage.can.coords(self.idBonus ,self.bonus.x - ray, self.bonus.y - ray, self.bonus.x + ray, self.bonus.y + ray )
            else:
                self.affichage.can.delete(self.idBonus)
                self.bonus = ""
                

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
        if self.ship != "":
            touche=event.keysym
            if touche=='Left':
                self.ship.mouvement("gauche")
            elif touche=='Right':
                self.ship.mouvement("droite")
            elif touche=='space' and self.cooldown==0:
                self.cooldown=15
                self.missile.append( projectile(self.ship.x + 5, self.ship.y - 20,self.affichage.height,5, "ally") )
                missile = self.missile[-1]
                self.idMissile.append( self.affichage.can.create_oval(missile.x - missile.rayon, missile.y - missile.rayon, missile.x + missile.rayon, missile.y - missile.rayon, width=1,outline='green',fill='green') )
            
            self.affichage.can.coords(self.idship ,self.ship.x - self.ship.rayon, self.ship.y - self.ship.rayon, self.ship.x + self.ship.rayon, self.ship.y + self.ship.rayon)
        self.affichage.fen.after(20)

    def missileTouche(self, missile):
        index = 0
        
        if self.ship != "":
            if ( (self.ship.x - missile.x)**2 + (self.ship.y - missile.y)**2 )**0.5 <= self.ship.rayon + missile.rayon: #si touche le vaiseau
                self.affichage.can.delete( self.idship )
                self.ship = ""
                
                self.affichage.lowLife()
                self.affichage.scoreup(-1000)
                
                self.affichage.changeMessage("Votre vaiseau est detruit")
                self.affichage.newGameBut.configure( relief="raised",text="Respawn", command = self.respawnShip )
                
                if self.endGame() == True:
                    return("endGame")
    
                return ( True )
        

        if self.bonus != "":
            if ( (self.bonus.x - missile.x)**2 + (self.bonus.y - missile.y)**2 )**0.5 <= self.bonus.rayon + missile.rayon:
                self.affichage.can.delete( self.idBonus )
                self.bonus = ""
                self.idBonus = ""
                self.affichage.scoreup(1000)
                
                return(True)

    
        for alien in self.alien:
            if missile.shooter == "ally" and ( (alien.x - missile.x)**2 + (alien.y - missile.y)**2 )**0.5 <= missile.rayon + alien.rayon:
                self.affichage.can.delete( self.idAlien[index])
                self.alien.pop(index)
                self.idAlien.pop(index)
                self.affichage.scoreup(100)
                
                if self.endGame() == True:
                    return("endGame")
                
                return(True)
            index += 1
        
        index = 0
        for shelter in self.Shelter:
            if ( (shelter.x - missile.x)**2 + (shelter.y - missile.y)**2 )**0.5 < missile.rayon + shelter.rayon:
                self.affichage.can.delete( self.idShelter[index] )
                self.Shelter.pop(index)
                self.idShelter.pop(index)
                
                return(True)
    
            index += 1

        return(False)

    def endGame(self):
        if len( self.alien ) == 0 :
            self.affichage.changeMessage("Youpi vous avez gagner")
            self.winStreak += 1
            self.alienGene()

        if self.affichage.getLife() <= 0:
            self.affichage.changeMessage("Game Over")
            
            self.cleanGame()
            self.ShelterGene()
            self.alienGene()
            return(True)

            
    def cleanGame(self):
        for el in self.idAlien:
            self.affichage.can.delete( el )
        
        self.alien = []
        self.idAlien = []
        
        for el in self.idShelter:
            self.affichage.can.delete( el )
        
        self.Shelter=[]
        self.idShelter=[]
        
        for el in self.idMissile:
            self.affichage.can.delete( el )
        
        self.missile = []
        self.idMissile = []
                
        self.affichage.can.delete( self.idBonus )
        self.bonus = ""
        self.idBonus = ""
        
        self.affichage.resetLife()
        self.affichage.resetScore()
        
        self.affichage.newGameBut.configure( relief="raised",text="New Game", command = self.initialisationObj )


a = gameRule()

a.start()


