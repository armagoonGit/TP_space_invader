# -*- coding: utf-8 -*-
"""
que fait : fichier classe graphique
qui : FOËX Vick 
quand : 17/12/2020
que reste a faire : tout
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from tkinter import Tk, Label, Canvas, Button, PhotoImage, Entry


class fentre():
    def __init__(self):

        #tkinter
        self.fen = Tk()
        
        self.quitBut = Button( self.fen, text = "quitter le jeu", command = self.fen.destroy)
        self.newGameBut = Button( self.fen, text = "nouveau jeu" )
        
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


    def change(self): #actualisation qd on soument une lettre
         askLettre(self.lettreList, self.champ.get() , self.dico)
         self.champ.delete( 0, "end" )
         
         if self.dico["error"] == 8:
             self.end()
         
         self.gWordAff.config( text =  adaptGuesWord( self.dico["guesWord"] ) )
         self.message.config( text = self.dico["message"] )
         
         self.can.delete("all")
         self.img = PhotoImage( file="image/bonhomme" + str( self.dico["error"]) + ".gif" )
         self.item = self.can.create_image( 0, 0, anchor="nw", image=self.img )


    def end(self):
        self.dico["message"] = "desoler c'est perdu, le mots etait: " + self.dico["word"]
        self.valideBut.destroy()
        
    def fatalEnd(self):
        self.dico["message"] = "Che"
        self.message.config( text = self.dico["message"] )
        self.valideBut.destroy()
        
        
         
         
         

a = fentre()
a.go()


