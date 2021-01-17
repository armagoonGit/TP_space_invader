#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
que fait : fichier classe des regles du jeu
qui : FOËX Vick / nael Axel
quand : 17/12/2020
que reste a faire : 
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from random import randint
from tkinter import PhotoImage

from lesObjets import vaisseau, bonus, cShelter, cAlien, projectile
from moduGraphique import fenetre


class gameRule:
    def __init__(self):
        self.affichage = fenetre(self)

        self.winStreak = 0
        
        self.nbAlien = 8
        self.alien = []

        self.alienIm = self.imageGene()
        self.alienGene()
        
        
        self.nbshelter =5*80
        self.Shelter=[]
        self.shelterIm = PhotoImage(file='imagegif/bunker.gif')
        self.ShelterGene()
        
        self.bonus = ""
        self.bonusIm = PhotoImage(file='imagegif/bonus.gif')
        
        self.missile = []
        self.missileIm = PhotoImage(file='imagegif/Projectile.gif')
        
        self.ship = ""
        self.shipIm = PhotoImage(file='imagegif/vaisseau.gif')
        
        self.cooldown=0
        
    
    def start(self):
        """
        methode a lancer pour lancer le jeu
        """
        self.affichage.go()

#les methodes de generation des objets :
        
    def imageGene(self):
        """
        return la liste de toutes les image des aliens
        """
        res = []
        for i in range(5):
            res.append( PhotoImage(file='imagegif/alien' + str(i + 1) +'.gif') )
        return(res)
            
    def choseAlienType(self):
        """
        return un nombre en 0 et 4 qui correpond a un type d'alien
        Plus le win streak est haut plus on a deux change d'avoir une valeur elever
        """
        alienType = randint(0,4) - 4 + self.winStreak
        if alienType <= 0:
            alienType = 0
        elif alienType > len(self.alienIm) - 1:
            alienType = len( self.alienIm ) - 1
        return(alienType)
        
    def alienGene(self):
        """
        genere tout les aliens et les positionne
        """
        w = int( self.affichage.can.cget('width') ) - 100
        cursorX = 100
        cursorY = 100

        for i in range(self.nbAlien):
            alienType = self.choseAlienType()
            
            self.alien.append( cAlien(cursorX, cursorY, 17, self.winStreak, alienType) )
            
            alien = self.alien[-1]

            alien.addId( self.affichage.can.create_image(alien.x, alien.y, anchor='center', image= self.alienIm[alienType]))
            self.affichage.can.image.append(self.alienIm[alienType]) #affiche l'alien
        
            cursorX += 100
            if cursorX >= w:
                cursorY += 40
                cursorX = 100
                
        self.affichage.can.tag_raise( self.affichage.idMessage ) # remetre le message au dessu des nouveaux aliens

    def ShelterGene(self):
        """
        genere tout les shelter et les positionent 
        """
        w = int( self.affichage.can.cget('width') ) - 100
        cursorX = 105
        cursorY = 500

        for i in range(self.nbshelter):
            if cursorX>=w/7 and cursorX<=2*w/7 or cursorX>=3*w/7 and cursorX<=4*w/7 or cursorX>=5*w/7 and cursorX<=6*w/7:
                self.Shelter.append( cShelter(cursorX, cursorY, 5) )
                Shelter = self.Shelter[-1]
                Shelter.addId( self.affichage.can.create_image(Shelter.x, Shelter.y, anchor='center',image=self.shelterIm) )
                self.affichage.can.image.append(self.shelterIm)

            cursorX += 10
            if cursorX >= w:
                cursorY += 10
                cursorX = 105
        
                

    def initialisationObj(self):
        """
        lance le debut de partie en creant le premire vaiseau et en
        executant les fonction de controle
        """
        self.affichage.newGameBut.configure(relief="flat",text="fight !", command = "")
        
        self.ship = vaisseau(20, self.affichage.can.cget('width') )
        self.ship.addId( self.affichage.can.create_image(self.ship.x, self.ship.y, anchor='center', image=self.shipIm ) )
        self.affichage.can.image.append(self.shipIm)

        self.affichage.can.focus_set()
        self.affichage.can.bind('<Key>',lambda x:self.pinput(x))

        self.turn()

#les methodes du jeu       

    def turn(self):
        """
        gere les mouvement de tout les objets du jeu
        """

        self.affichage.manageMessage() #baisser le cooldown des message afficher
        
        if self.cooldown>0: #pour eviter que le vaiseau tire en ilimiter
            self.cooldown= self.cooldown-1
        
        infoMov = self.adaptMovement() 

        for index,el in enumerate( self.missile ):
            rmShoot1 = el.mouvement()
            rmShoot2 = self.missileTouche(el)
            
            if rmShoot2 == "endGame": #coupe la recurciviter de la fonction en cas de game OVER
                return()
            
            elif rmShoot1 == True or rmShoot2 == True : #detruit le missile si il y a  eu un impact
                self.affichage.can.delete( el.id)
                self.missile.pop(index)
    
            else: #fait bouger l'image du misisle
                self.affichage.can.coords(el.id, el.x, el.y)
          
                
        for el in self.alien :
            if self.endGame( el.y ) == True:
                return()
            
            tireprob=(self.nbAlien / (len(self.alien)))*35
            addShoot = el.shoot(tireprob)
            
            el.mouvement( infoMov ) #mouvement de l'alien 
            self.affichage.can.coords(el.id ,el.x, el.y) #affichage de l'alien
            
            if addShoot == True:
                self.missile.append( projectile(el.x , el.y, self.affichage.height, 5, "foe") )

                missile = self.missile[-1]

                missile.addId( self.affichage.can.create_image(missile.x, missile.y, anchor='center', image=self.missileIm ))
                self.affichage.can.image.append(self.missileIm)
                
        if self.bonus == "": #si il n'y a pas deja de bonus. On en creer peut etre un
            bonusnb = randint(0, 1000)   
            if bonusnb == 1000 : #on creé un bonus
                self.bonus = bonus()
                
                self.bonus.addId( self.affichage.can.create_image(self.bonus.x,self.bonus.y ,anchor='center', image= self.bonusIm) )
                self.affichage.can.image.append(self.alienIm)
                
        else: #si un bonus est deja en jeu on le fait bouger
            if self.bonus.x <= 1000 and self.bonus.dir == 1 or self.bonus.x >= -10 and self.bonus.dir == -1: # si le bonus n'arrive pas en bout d'ecran
                self.bonus.mouvement()
        
                self.affichage.can.coords(self.bonus.id ,self.bonus.x, self.bonus.y)
    
            else:
                self.affichage.can.delete(self.bonus.id)
                self.bonus = ""
                

        self.affichage.fen.after(20, self.turn)
        
    def adaptMovement(self):
        """
        permet au alien d'avoir un mouvement adpter au nombre qu'il reste
        permet aux alien de savoir si il doivent dessendre d'une ligne
        return un dicionaire :
            "speed" : multiplicateur ppour la vitesse des aliens
            "newRow" : True si une nouvelle ligne est nescssaire
        """
        w = int( self.affichage.can.cget('width') )
        res = {}
        res["speed"] = (self.nbAlien / (len(self.alien)+5))*0.5 
        res["newRow"] = False
        
        for alien in self.alien :
            nextPosX = alien.x + alien.direction * 10
            
            if nextPosX >= w - alien.rayon or nextPosX <= 0 + alien.rayon:
                res["newRow"] = True
                return(res)

        return(res)
    
    def pinput(self,event):
        """
        gere les entre de l'utilsateur pour le mouvement du vaiseau
        """
        if self.ship != "":
            touche = event.keysym
            if touche == 'Left':
                self.ship.mouvement("gauche")
            
            elif touche == 'Right':
                self.ship.mouvement("droite")
            
            elif touche == 'space' and self.cooldown == 0:
                self.cooldown = 15
                self.missile.append( projectile( self.ship.x + 5, self.ship.y - 20, self.affichage.height, 5, "ally") )
                
                missile = self.missile[-1]
                
                missile.addId( self.affichage.can.create_image(missile.x, missile.y, anchor='center', image=self.missileIm) )
                self.affichage.can.image.append(self.missileIm)

            self.affichage.can.coords(self.ship.id ,self.ship.x, self.ship.y)
        self.affichage.fen.after(20)
    
    def respawnShip(self):
        """
        genere un nouveau vaiseau
        """
        self.affichage.newGameBut.configure(relief="flat",text="fight !", command = "")
        
        self.ship = vaisseau(20, self.affichage.can.cget('width'))
        self.ship.addId( self.affichage.can.create_image(self.ship.x, self.ship.y, anchor='center', image=self.shipIm ) )
        self.affichage.can.image.append(self.shipIm)


    def missileTouche(self, missile):
        """
        gere toutes les colision de missile avec les diffrent objet du jeu
        gere aussi leurs destructions
        """
        
        if self.ship != "":
            if ( (self.ship.x - missile.x)**2 + (self.ship.y - missile.y)**2 )**0.5 <= self.ship.rayon + missile.rayon: #si touche le vaiseau
                self.affichage.can.delete( self.ship.id )
                self.ship = ""
                
                self.affichage.lowLife()
                self.affichage.scoreup(-1000)
                
                self.affichage.changeMessage("Votre vaiseau est detruit")
                self.affichage.newGameBut.configure( relief="raised",text="Respawn", command = self.respawnShip )
                
                if self.endGame(0) == True:
                    return("endGame")
    
                return ( True )
        

        if self.bonus != "":
            if ( (self.bonus.x - missile.x)**2 + (self.bonus.y - missile.y)**2 )**0.5 <= self.bonus.rayon + missile.rayon:
                self.affichage.scoreup( self.bonus.point )
                self.affichage.can.delete( self.bonus.id )
                self.bonus = ""

                return(True)

    
        for index, alien in enumerate( self.alien ):
            if missile.shooter == "ally" and ( (alien.x - missile.x)**2 + (alien.y - missile.y)**2 )**0.5 <= missile.rayon + alien.rayon:
                self.affichage.scoreup( alien.point )
                self.affichage.can.delete( alien.id )
                self.alien.pop(index)
                
                if self.endGame(alien.y) == True:
                    return("endGame")
                
                return(True)
        

        for index, shelter in enumerate( self.Shelter ):
            if ( (shelter.x - missile.x)**2 + (shelter.y - missile.y)**2 )**0.5 < missile.rayon + shelter.rayon:
                self.affichage.can.delete( shelter.id )
                self.Shelter.pop(index)
                
                return(True)

        return(False)

#fin de partie
    def endGame(self, y):
        """
        Gere les differante possibilite de fin de partie ou de niveau suivant
        Game over si :
            le joueur n'a plus de vie
            les alien son trop bas
        """
        if len( self.alien ) == 0 :
            self.winStreak += 1
            self.affichage.changeMessage("Niveau " + str(self.winStreak) )

            self.nbAlien = 8 * self.winStreak # plus d'alien a chaque niveau
            
            if self.nbAlien > 72 :
                self.nbAlien = 72
            
            self.alienGene()

        if self.affichage.getLife() <= 0 or y > 550 :
            self.affichage.changeMessage("Game Over")
            
            self.affichage.manageScore()
            
            self.cleanGame()
            self.ShelterGene()
            self.alienGene()
            return(True)

            
    def cleanGame(self):
        """
        reinsitalise les atributs de la classe pour preparer le jeu a une 
        nouvelle partie
        """
        for el in self.alien:
            self.affichage.can.delete( el.id )

        self.alien = []
        self.nbAlien = 8

        for el in self.Shelter:
            self.affichage.can.delete( el.id )
        
        self.Shelter=[]

        
        for el in self.missile:
            self.affichage.can.delete( el.id )
        
        self.missile = []
          
        if self.bonus != "":
            self.affichage.can.delete( self.bonus.id )
            self.bonus = ""
       
        self.affichage.resetLife()
        self.affichage.resetScore()
        self.winStreak = 0
        

        self.affichage.newGameBut.configure( relief="raised",text="New Game", command = self.initialisationObj )
