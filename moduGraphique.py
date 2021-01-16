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
        
        self.fondim=PhotoImage(file = 'imagegif/fond.gif')
        
        self.width = 1000
        self.height = 700 
        
        
        self.quitBut = Button( self.fen, text = "quitter le jeu", command = self.fen.destroy)
        self.newGameBut = Button( self.fen, text = "nouveau jeu", command = gameRule.initialisationObj )
        
        self.message =Label( self.fen, text = "Le jeu est LOOOOOURD")

        
        self.score = Label( self.fen, text = "score : 1000" )
        self.live = Label( self.fen, text = "lives : 1" )

        self.can = Canvas( self.fen, width = self.width, height = self.height )
        self.can.create_image(0, 0, image=self.fondim, anchor='nw')
        self.can.image=[self.fondim]
        
        self.idMessage =  self.can.create_text(self.width/2, 50, fill="darkblue",
                        font="systemfixed 20 italic bold", text="Le jeu est LOURD !", anchor = "n")

        
    def go(self): #mise en place au debut du programe
        self.fen.title("Space invader")
        
        self.message.grid(row= 2, column = 1)
        
        self.can.grid(row = 2, column = 1, rowspan= 4)
        
        self.live.grid(row = 1, column = 2)
        self.live.config( bg = "green")
        self.score.grid(row = 2, column = 2)
        
        self.newGameBut.grid(row = 3, column = 2)
        self.quitBut.grid(row = 4, column = 2)

        self.cooldownMessage = 0

        self.fen.mainloop()
        
    def changeMessage(self, message):

        self.can.itemconfig(self.idMessage, text = message )
        self.cooldownMessage = 50
        
    def manageMessage(self):
        if self.cooldownMessage > 0:
            self.cooldownMessage -= 1
        else:
            self.changeMessage("")
        

    def lowLife(self):
        text = self.live.cget("text")
        text = text.split(" ")
        text = int( text[-1] ) - 1
        self.live.config(text = str( "lives : " + str( text ) ))
        if text >= 3:
            self.live.config( bg = "green")
        elif text == 2:
            self.live.config( bg = "coral")
        else:
            self.live.config( bg = "red")
    
    
    def getLife(self):
        life = self.live.cget("text")
        life = life.split(" ")
        life = int( life[-1] ) 
        return( life )
    
    def resetLife(self):
        self.live.config(text = "lives : 3")
        
    
    def scoreup(self,points):
        text = self.score.cget("text")
        text = text.strip(" ")
        text = int(text[8:]) + points
        if text<0:
            text=0
        self.score.config(text= str("score : " +str(text)))
        
    def resetScore(self):
        self.score.config(text= "score : 0") 
        
    def getScore(self):
        text = self.score.cget("text")
        text = text.split(":")
        return(text[1])
        
        
    def manageScore(self):
        scoreDoc = open('score.txt',"r")
        scoreList = []
        
        for el in scoreDoc :
            scoreList.append( el.rstrip('\n'))
            
        scoreDoc.close()
        
        index = 0
        score = int (self.getScore() )

        scoreList.append(score)
        scoreList = [ int(x) for x in scoreList ]
        scoreList.sort()
        scoreList.reverse()
        

            
        scoreDoc = open('score.txt',"w")
        strScore = ""
        print("oui", score)
        print(scoreList)
        for i,el in enumerate(scoreList[: -1]):
            scoreDoc.write( str( el ) + '\n' )
            strScore += str( i + 1 ) + '. ' + str(el) + '\n'
        scoreDoc.close()
        
        self.changeMessage(strScore)
        
        
        
        

