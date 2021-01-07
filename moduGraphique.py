# -*- coding: utf-8 -*-
"""
que fait : fichier classe graphique
qui : FOËX Vick / Nael Axel
quand : 17/12/2020
que reste a faire : tout
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from tkinter import Tk, Label, Canvas, Button, PhotoImage, Entry


class fenetre():
    def __init__(self, gameRule):

        #tkinter
        self.fen = Tk()
        
        self.width = 1000
        self.height = 700 
        
        
        self.quitBut = Button( self.fen, text = "quitter le jeu", command = self.fen.destroy)
        self.newGameBut = Button( self.fen, text = "nouveau jeu", command = gameRule.initialisationObj )
        
        self.message =Label( self.fen, text = "Le jeu est LOOOOOURD")

        
        self.score = Label( self.fen, text = "score : 0" )
        self.live = Label( self.fen, text = "lives : 3" )

        self.can = Canvas( self.fen, width = self.width, height = self.height )

        
    def go(self): #mise en place au debut du programe
        self.fen.title("Space invader")
        
        self.message.grid(row= 1, column = 1)
        
        self.can.grid(row = 2, column = 1, rowspan= 4)
        
        self.live.grid(row = 1, column = 2)
        self.score.grid(row = 2, column = 2)
        
        self.newGameBut.grid(row = 3, column = 2)
        self.quitBut.grid(row = 4, column = 2)
     

        self.fen.mainloop()
    
    def lowLife(self):
        text = self.live.cget("text")
        text = text.split(" ")
        text = int( text[-1] ) - 1
        self.live.config(text = str( "lives : " + str( text ) ))
        self.live.config( bg = "red")
    
    def scoreup(self,points):
        text = self.score.cget("text")
        text = text.strip(" ")
        text = int(text[8:]) + points
        if text<0:
            text=0
        self.score.config(text= str("score : " +str(text)))
        

