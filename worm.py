from tkinter import *
from math import pi, sin, cos

class Worm(object):
    def __init__(self,f,name,position):
        self.name = name
        self.position = position
        self.fenetre = f
        self.imgPath = PhotoImage(file ="Worm.png")
        self.wormHitBox = Canvas(self.fenetre,width=512, height=512)
        self.wormHitBox.create_image(512,512,image=self.imgPath)
        self.wormHitBox.pack()
        print ("Joueur " + str(self.name) + " en position " + str(self.position) + " a etait crée")