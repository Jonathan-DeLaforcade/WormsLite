from tkinter import *
from math import *
from time import sleep

class roquette(object):
    def __init__(self,fenetre,canonX2,canonY2,couleur):
        self.fenetre = fenetre
        self.x = canonX2
        self.y = canonY2
        self.rayon = 5
        self.couleur = couleur
    def tir(self,angle):
        angleRad = radians(angle)

        vitesse = 10
        t = 0
        """
        while t< 10:
            x = cos(angleRad)*vitesse*t
            y = (1/2)*10*t**2+sin(angleRad)+vitesse*t
            t =t + 1
            print ("x: "+ str(x) + " y: " + str(y))
            sleep(0.1)
        """
        self.fenetre.coords(self.obu, self.x, self.y, self.x, self.y)
        
       
    def CreateRoquette(self):
        self.obu = self.fenetre.create_oval(self.x-self.y,self.y-self.rayon, self.x+self.rayon, self.y+self.rayon, fill=self.couleur,width = self.rayon)
    def Destroy(self):
        self.fenetre.delete(self.obu)        

