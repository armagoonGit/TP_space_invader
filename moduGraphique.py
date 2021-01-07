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
        
        
        self.quitBut = Button( self.fen, text = "quitter le jeu", command = self.fen.destroy)
        self.newGameBut = Button( self.fen, text = "nouveau jeu", command = gameRule.initialisationObj )
        
        self.score = Label( self.fen, text = "score : 0" )
        self.live = Label( self.fen, text = "lives : 3" )

        self.can = Canvas( self.fen, width = 1000, height = 700 )

        
    def go(self): #mise en place au debut du programe
        self.fen.title("Space invader")
        
        self.can.grid(row = 1, column = 1, rowspan= 4)
        
        self.live.grid(row = 1, column = 2)
        self.score.grid(row = 2, column = 2)
        
        self.newGameBut.grid(row = 3, column = 2)
        self.quitBut.grid(row = 4, column = 2)
     

        self.fen.mainloop()



