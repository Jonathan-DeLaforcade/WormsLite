from tkinter import *
from bazooka import *
from roquette import *



class Game(object):
    def __init__(self,fenetre):
        self.fenetrePrincipal = fenetre
        self.fenetreDeJeu = Canvas(self.fenetrePrincipal,width=1000, height=200, bg ='ivory',bd=0)
        self.fenetreDeJeu.pack(side=TOP, padx =10, pady =1)

        self.terrainDeJeu = Canvas(self.fenetreDeJeu,width=1000, height=190, bg ='cyan',bd=0)
        self.terrainDeJeu.pack(side=TOP, padx =10, pady =1)

        ground = Canvas(self.fenetreDeJeu,width=1000, height=10, bg ='green')
        ground.pack(side=BOTTOM)

        armeJoueur1 = Bazooka(self.terrainDeJeu, 50, 175)
        armeJoueur2 = Bazooka(self.terrainDeJeu, 800, 175)


        sliderReglageAngleJ1 =Scale(self.fenetrePrincipal, label='hausse', from_=90, to=0, length = 100 , command=armeJoueur1.orienter)
        sliderReglageAngleJ1.pack(side=LEFT, pady =0, padx =10)
        sliderReglageAngleJ1.set(45)

        sliderReglageAngleJ2 =Scale(self.fenetrePrincipal, label='hausse', from_=90, to=180, length = 100 , command=armeJoueur2.orienter)
        sliderReglageAngleJ2.pack(side=RIGHT, pady =0, padx =10)
        sliderReglageAngleJ2.set(125)

        buttonFireJ1 = Button(self.fenetrePrincipal, text="FEUUUUUUUU !!!", command=armeJoueur1.tir,padx = 0, pady = 40, height=1, width= 20)
        buttonFireJ1.pack(side=LEFT, pady =20, padx =10)

        buttonDeleteJ1 = Button(self.fenetrePrincipal, text="Delete", command=armeJoueur1.Destroy,padx = 0, pady = 40, height=1, width= 20)
        buttonDeleteJ1.pack(side=LEFT, pady =20, padx =10)

        buttonFireJ2 = Button(self.fenetrePrincipal, text="FEUUUUUUUU !!!", command=armeJoueur2.tir,padx = 0, pady = 40, height=1, width= 20)
        buttonFireJ2.pack(side=RIGHT, pady =20, padx =10)

        buttonDeleteJ2 = Button(self.fenetrePrincipal, text="Delete", command=armeJoueur2.Destroy,padx = 0, pady = 40, height=1, width= 20)
        buttonDeleteJ2.pack(side=LEFT, pady =20, padx =10)