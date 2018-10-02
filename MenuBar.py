# -*- coding: utf-8 -*-
import Tkinter
from Tkinter import *
from tkMessageBox import *
from Tkinter import Tk,Toplevel,Canvas,Frame,Menu,Menubutton
import tkFileDialog
import tkMessageBox
class MenuBar(Frame):
  def __init__(self, parent, model_x, model_y, bg="white"):
    Tkinter.Frame.__init__(self)
    self.model_x = model_x
    self.model_y = model_y
    self.parent  = parent
    #Barre Menu
    self.MenuBarre = Tkinter.Menu(self.master)
    
    #button_file
    self.button_file = Menu(self.MenuBarre, tearoff=0)
    self.MenuBarre.add_cascade(label="File", underline=0, menu=self.button_file)
    self.button_file.add_command(label="Open", underline=0, command = self.open)
    self.button_file.add_command(label="Save", underline=0, command = self.save)
    self.button_file.add_command(label="Exit", underline=0, command = self.exit)
    
    #button_Aide
    self.button_Aide = Menu(self.MenuBarre,tearoff=0)
    self.MenuBarre.add_cascade(label="Aide", underline=0, menu=self.button_Aide);
    self.button_Aide.add_command(label="Aide", underline=0, command=self.aide)
    
    self.master.config(menu=self.MenuBarre)
    
  
  def packing(self):
	  self.button_file.pack(side="top")
	  
	

  def save(self):
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt",initialfile = "SAVE FILE")
    text2save = "Amplitude_x : "+ str(self.model_x.get_magnitude())+" Frequence_x : "+str(self.model_x.get_frequency())+" Phase_x : "+str(self.model_x.get_phase()); # starts from `1.0`, not `0.0`
    f.write(text2save)
    text2save = " Amplitude_y : "+ str(self.model_y.get_magnitude())+" Frequence_y : "+str(self.model_y.get_frequency())+" Phase_y : "+str(self.model_y.get_phase());
    f.write(text2save)
    f.close()

  def exit(self):
      res = tkMessageBox.askquestion("Quitter", "Voulez-vous quitter ?", icon='warning')
      if res == "yes" :
        exit()
      else :
        return False

  def open(self):
    f = tkFileDialog.askopenfilename(initialdir="./", title="Select file", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    reading = open(f, "r").read()
    infos = reading.split(" ")
    amp_x, freq_x, phase_x = float(infos[2]), float(infos[5]), float(infos[8])
    self.model_x.set_magnitude(amp_x)
    self.model_x.set_frequency(freq_x)
    self.model_x.set_phase(phase_x)
    amp_y, freq_y, phase_y = float(infos[11]), float(infos[14]), float(infos[17])
    self.model_y.set_magnitude(amp_y)
    self.model_y.set_frequency(freq_y)
    self.model_y.set_phase(phase_y)


  def aide(self):
    showinfo('Aide','Concepteur de l\'application\n\tLANDURE Etienne \nEmail :\n\te4landure@enib.fr')
 	      
