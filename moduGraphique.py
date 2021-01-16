# -*- coding: utf-8 -*-
"""
que fait : fichier classe graphique
qui : FOËX Vick / Nael Axel
quand : 17/12/2020
que reste a faire : 
lien git : https://github.com/armagoonGit/TP_space_invader
"""

from tkinter import Tk, Label, Canvas, Button, PhotoImage, messagebox


class fenetre():
    def __init__(self, gameRule):

        self.fen = Tk()
        
        self.fondim=PhotoImage(file = 'imagegif/fond.gif')
        
        self.width = 1000
        self.height = 700 

        
        
        self.quitBut = Button( self.fen, text = "quitter le jeu", command = self.fen.destroy)
        self.newGameBut = Button( self.fen, text = "nouveau jeu", command = gameRule.initialisationObj )
        
        self.message =Label( self.fen, text = "Le jeu est LOOOOOURD")

        
        self.score = Label( self.fen, text = "score : 0" )
        self.live = Label( self.fen, text = "lives : 1" )

        self.can = Canvas( self.fen, width = self.width, height = self.height )
        self.can.create_image(0, 0, image=self.fondim, anchor='nw')
        self.can.image=[self.fondim]
        
        self.idMessage =  self.can.create_text(self.width/2, 50, fill="darkblue",
                        font="systemfixed 20 italic bold", text="Niveau 0", anchor = "n")
        
        self.about = Button( self.fen, text = "a propos", command = self.aboutIt)

        
    def go(self): #mise en place au debut du programe
        """
        Setup toute la fenetre et ses composant
        """
        self.fen.title("Space invader")
        
        self.can.grid(row = 1, column = 1, rowspan= 5)
        
        self.live.grid(row = 1, column = 2)
        self.live.config( bg = "green")
        self.score.grid(row = 2, column = 2)
        
        self.newGameBut.grid(row = 3, column = 2)
        self.about.grid(row = 4, column = 2)
        self.quitBut.grid(row = 5, column = 2)

        self.cooldownMessage = 0

        self.fen.mainloop()
        
    def aboutIt(self):
        messagebox.showinfo('A propos','"Moi j\'aurai ete le prof je nous aurai mie une bonne note"')
        
#message
    def changeMessage(self, message):
        """
        Prend en parametre une str. Permet de changer le texte sur le canvas
        """
        self.can.itemconfig(self.idMessage, text = message )
        self.cooldownMessage = 50
  
    def manageMessage(self):
        """
        fait en sorte de que message ne reste pas indefiniment
        """
        if self.cooldownMessage > 0:
            self.cooldownMessage -= 1
        else:
            self.changeMessage("")

#life     
    def getLife(self):
        """
        donne le nombre de point de vie du joueur
        return un int
        """
        life = self.live.cget("text")
        life = life.split(" ")
        life = int( life[-1] ) 
        return( life )

    def lowLife(self):
        """
        Baisse la vie du joueur d'un point et l'affiche
        Change la couleur de l'affichage
        """
        life = self.getLife()
        life -= 1
        self.live.config(text = str( "lives : " + str( life ) ))
        if life >= 3:
            self.live.config( bg = "green")
        elif life == 2:
            self.live.config( bg = "coral")
        else:
            self.live.config( bg = "red")
    
    def resetLife(self):
        """
        remet les point de vie au max
        """
        self.live.config(text = "lives : 3")
        
#score    
    def getScore(self):
        """
        return un int correspondant au score du joueur
        """
        text = self.score.cget("text")
        text = text.split(":")
        return( int( text[1] ) )

    def scoreup(self,points):
        """
        Prend en parametre une str.
        augmente le score du nombre de point et l'affiche
        """
        score = self.getScore()
        score += points
        if score < 0: #peut arriver car la destruciton du vaiseau bassie le score
            score = 0
        self.score.config( text = str("score : " +str(score) ) )
        
    def resetScore(self):
        """
        remet le score a 0
        """
        self.score.config(text= "score : 0") 

    def manageScore(self):
        """
        gere la sauvegarde des meilleusr score dans un fichier
        creé une str qui pemret l'affichage des meilleur score avec celui 
        de la partie joué
        """
        scoreDoc = open('score.txt',"r")
        scoreList = []
        
        for el in scoreDoc :
            scoreList.append( el.rstrip('\n'))
            
        scoreDoc.close()

        score = self.getScore()

        scoreList.append(score)
        scoreList = [ int(x) for x in scoreList ]
        scoreList.sort()
        scoreList.reverse()
            
        scoreDoc = open('score.txt',"w")
        strScore = "Hight score :\n"

        for i,el in enumerate(scoreList[: -1]): 
            scoreDoc.write( str( el ) + '\n' )
            if el == score:
                strScore += "You" + '. ' + str(el) + '\n'
            else:
                strScore += str( i + 1 ) + '. ' + str(el) + '\n'
                
        scoreDoc.close()
        
        self.changeMessage(strScore)
