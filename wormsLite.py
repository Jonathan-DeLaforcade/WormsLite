from tkinter import *
from bazooka import *
from roquette import *

"""                 INTERFACE                 """
fenetre  = Tk()
fenetre.geometry("1024x480")


fenetreDeJeu = Canvas(fenetre,width=1000, height=200, bg ='ivory',bd=0)
fenetreDeJeu.pack(side=TOP, padx =10, pady =1)

terrainDeJeu = Canvas(fenetreDeJeu,width=1000, height=190, bg ='cyan',bd=0)
terrainDeJeu.pack(side=TOP, padx =10, pady =1)

ground = Canvas(fenetreDeJeu,width=1000, height=10, bg ='green')
ground.pack(side=BOTTOM)

armeJoueur1 = Bazooka(terrainDeJeu, 50, 175)
armeJoueur2 = Bazooka(terrainDeJeu, 800, 175)


sliderReglageAngleJ1 =Scale(fenetre, label='hausse', from_=90, to=0, length = 100 , command=armeJoueur1.orienter)
sliderReglageAngleJ1.pack(side=LEFT, pady =0, padx =10)
sliderReglageAngleJ1.set(45)

sliderReglageAngleJ2 =Scale(fenetre, label='hausse', from_=90, to=180, length = 100 , command=armeJoueur2.orienter)
sliderReglageAngleJ2.pack(side=RIGHT, pady =0, padx =10)
sliderReglageAngleJ2.set(125)

buttonFireJ1 = Button(fenetre, text="FEUUUUUUUU !!!", command=armeJoueur1.tir,padx = 0, pady = 40, height=1, width= 20)
buttonFireJ1.pack(side=LEFT, pady =20, padx =10)

buttonDeleteJ1 = Button(fenetre, text="Delete", command=armeJoueur1.Destroy,padx = 0, pady = 40, height=1, width= 20)
buttonDeleteJ1.pack(side=LEFT, pady =20, padx =10)

buttonFireJ2 = Button(fenetre, text="FEUUUUUUUU !!!", command=armeJoueur2.tir,padx = 0, pady = 40, height=1, width= 20)
buttonFireJ2.pack(side=RIGHT, pady =20, padx =10)

buttonDeleteJ2 = Button(fenetre, text="Delete", command=armeJoueur2.Destroy,padx = 0, pady = 40, height=1, width= 20)
buttonDeleteJ2.pack(side=LEFT, pady =20, padx =10)

fenetre.mainloop()