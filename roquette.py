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

        vitesse = 17
        t = 0

        print("Angle: " + str(angle))
        position = []
        while self.y < 400 :
            self.y = self.y + (((-1/2)*(9.81)*t**2+sin(angle)*vitesse*t) * (-1))
            self.x = self.x + cos(angle)*vitesse*t
            t = t + 0.1
            
            print ("T: " + str(t) + "X: " + str(self.x) + " Y: " + str(self.y))
            pos = [self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2]
            position.append(pos)
            
        print("pos: " + str(position))

        for i in range (len(position)-1):
            self.fenetre.coords(self.obu,position[i][0],position[i][1],position[i][2],position[i][3])
            self.fenetre.update()
            sleep(0.1)

        self.Destroy()
        
    def CreateRoquette(self):
        self.obu = self.fenetre.create_oval(self.x-self.rayon/2,self.y-self.rayon/2, self.x+self.rayon/2, self.y+self.rayon/2, fill=self.couleur,width = self.rayon)
    def Destroy(self):
        self.fenetre.delete(self.obu)        

