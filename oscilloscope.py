# -*- coding: utf-8 -*-
from Tkinter import Tk,Toplevel,Canvas,Scale,Frame,IntVar
from observer import *
from generator import *
from view import *
from controller import *
from MenuBar import *


#class Oscilloscope(object):
#    def __init__(self,parent):
#        self.model=Generator()
#        self.model1=Generator(d=1)

        

if  __name__ == "__main__" : 
    root=Tk()
    root.option_readfile('config.txt')
    # Signal X
    model_x = Generator()
    # Signal Y
    model_y = Generator(id=1)
    # Création de la barre pour le menu
    menubar = MenuBar(root, model_x, model_y)

    view = Screen(root, model_x, model_y)
    view.grid(25, 25)
    view.update(model_x)
    view.update(model_y)

    model_x.attach(view)
    model_y.attach(view)

    # Contrôleur pour le signal X
    ctrl_x = Controller(model_x, view)
    # Contrôleur pour le signal Y
    ctrl_y = Controller(model_y, view)

    view.packing()

    root.mainloop()
    
     
