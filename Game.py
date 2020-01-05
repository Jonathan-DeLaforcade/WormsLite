from tkinter import *
from bazooka import *
from roquette import *



class Game(object):
    def __init__(self,fenetre):


        self.fenetrePrincipal = fenetre

        self.fenetreDeJeu = Frame(self.fenetrePrincipal,width=1000, height=500, bg ='ivory',bd=0)
        self.fenetreDeJeu.pack(side=TOP, padx =10, pady =1)

        self.terrainDeJeu = Canvas(self.fenetreDeJeu,width=1000, height=400, bg ='cyan',bd=0)
        self.terrainDeJeu.pack(side=TOP, padx =10, pady =1)

        ground = Canvas(self.fenetreDeJeu,width=1000, height=10, bg ='green')
        ground.pack(side=BOTTOM)

        armeJoueur1 = Bazooka(self.terrainDeJeu, 50, 375)
        armeJoueur2 = Bazooka(self.terrainDeJeu, 800, 375)


        self.controlsJ1 = Frame(self.fenetrePrincipal,width=200, height=300, bg ='blue',bd=1)
        self.controlsJ1.pack(side=LEFT,padx=10,pady=10)

        sliderReglageAngleJ1 =Scale(self.controlsJ1, label='hausse', from_=90, to=0, length = 100 , command=armeJoueur1.orienter)
        sliderReglageAngleJ1.pack(side=LEFT, pady =0, padx =10)
        sliderReglageAngleJ1.set(45)

        buttonFireJ1 = Button(self.controlsJ1, text="FEUUUUUUUU !!!", command=armeJoueur1.tir,padx = 0, pady = 40, height=1, width= 20)
        buttonFireJ1.pack(side=LEFT, pady =20, padx =10)

        buttonDeleteJ1 = Button(self.controlsJ1, text="Delete", command=armeJoueur1.Destroy,padx = 0, pady = 40, height=1, width= 20)
        buttonDeleteJ1.pack(side=LEFT, pady =20, padx =10)


        self.controlsJ2 = Frame(self.fenetrePrincipal,width=200, height=300, bg ='red',bd=1)
        self.controlsJ2.pack(side=RIGHT,padx=10,pady=10)

        sliderReglageAngleJ2 =Scale(self.controlsJ2, label='hausse', from_=90, to=180, length = 100 , command=armeJoueur2.orienter)
        sliderReglageAngleJ2.pack(side=RIGHT, pady =0, padx =10)
        sliderReglageAngleJ2.set(125)

        buttonFireJ2 = Button(self.controlsJ2, text="FEUUUUUUUU !!!", command=armeJoueur2.tir,padx = 0, pady = 40, height=1, width= 20)
        buttonFireJ2.pack(side=RIGHT, pady =20, padx =10)

        buttonDeleteJ2 = Button(self.controlsJ2, text="Delete", command=armeJoueur2.Destroy,padx = 0, pady = 40, height=1, width= 20)
        buttonDeleteJ2.pack(side=LEFT, pady =20, padx =10) 