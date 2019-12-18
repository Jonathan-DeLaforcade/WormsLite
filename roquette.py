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

        print (" x: "+ str(self.x) + " y: " + str(self.y))
    def tir(self,angle):
        angleRad = radians(angle)

        vitesse = 10
        t = 0
        
        
        while t< 50:
            self.x = self.x + (200 - (cos(angleRad)*vitesse*t))
            self.y = self.y + (200 -((1/2)*10*t**2+sin(angleRad)+vitesse*t))
            t =t + 1
            print ("angleRad: " + str(angleRad) + "           x: "+ str(self.x) + " y: " + str(self.y))
            sleep(0.1)
        
        self.fenetre.coords(self.obu,self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2)
        
        
       
    def CreateRoquette(self):
        self.obu = self.fenetre.create_oval(self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2, fill=self.couleur,width = self.rayon)
    def Destroy(self):
        self.fenetre.delete(self.obu)        

