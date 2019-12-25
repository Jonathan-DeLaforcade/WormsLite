from tkinter import *
from math import *
from time import sleep

class roquette(object):
    def __init__(self,fenetre,canonX2,canonY2,couleur):
        self.fenetre = fenetre
        self.x = canonX2
        self.y = canonY2
        self.rayon = 10
        self.couleur = couleur

        print (" x: "+ str(self.x) + " y: " + str(self.y))
    def tir(self,angle):

        vitesse = 60
        t = 0
        print("Angle: " + str(angle))
        
        while t< 50:
            self.y = self.y - (((-1/2)*9.81)*t**2)+sin(angle)
            self.x = self.x + cos(angle)*vitesse*t

            #self.y -= 5 #hauteur
            #self.x += 5 #largeur
            t =t + 1
            print (" angle: " + str(angle) + "  Largeur: "+ str(self.x) + " Hauteur: " + str(self.y))
            """self.fenetre.coords(self.obu,self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2)"""
            self.fenetre.create_oval(self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2, fill=self.couleur,width = self.rayon)
            self.fenetre.update()
            sleep(0.1)
        
        
       
    def CreateRoquette(self):
        self.obu = self.fenetre.create_oval(self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2, fill=self.couleur,width = self.rayon)
    def Destroy(self):
        self.fenetre.delete(self.obu)        

