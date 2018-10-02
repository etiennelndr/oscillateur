# -*- coding: utf-8 -*-
from Tkinter import Canvas, Scale, Entry, Checkbutton, Frame, IntVar, Label
from observer import *

class Screen(Observer):
	def __init__(self,parent,model_x, model_y, bg="white"):
		self.canvas = Canvas(parent,bg=bg)
		self.model_x = model_x
		self.model_y = model_y
		print("parent", parent.cget("width"), parent.cget("height"))

		self.showX = True
		self.showY = True

		self.frame = Frame(parent)
		# Signal X
		self.magnitude_x = Scale(self.frame, length=250, orient="horizontal", name="m_x", label="Magnitude X", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)
		self.frequency_x = Scale(self.frame, length=250, orient="horizontal", name="f_x", label="Frequency X", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)
		self.phase_x     = Scale(self.frame, length=250, orient="horizontal", name="p_x", label="Phase X", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)
		# Signal Y
		self.magnitude_y = Scale(self.frame, length=250, orient="horizontal", name="m_y", label="Magnitude Y", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)
		self.frequency_y = Scale(self.frame, length=250, orient="horizontal", name="f_y", label="Frequency Y", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)
		self.phase_y     = Scale(self.frame, length=250, orient="horizontal", name="p_y", label="Phase Y", sliderlength=20, showvalue=0, from_=0, to=5, tickinterval=25)

		self.frame2 = Frame(parent,bg="black")
		self.varX = IntVar()
		self.varY = IntVar()
		self.varXY = IntVar()
		self.lbl = Label(self.frame2,text="Courbes",fg="black")
		# Boutons de sélection (X, Y ou X-Y)
		self.caseX = Checkbutton(self.frame2, text="X", variable=self.varX, command=self.getX)
		self.caseY = Checkbutton(self.frame2, text="Y", variable=self.varY, command=self.getY)
		self.caseXY = Checkbutton(self.frame2, text="XY", variable=self.varXY, command=self.getXY)

		self.caseXY.select()
		
		self.wi = self.canvas.cget("width")
		self.hi = self.canvas.cget("height")
		
		self.stepx = 0
		self.stepy = 0
		# Step x
		self.step_x = Entry(parent, name="x")
		# Step y
		self.step_y = Entry(parent, name="y")
                    
	def update(self, model):
		print("View update")
		if model.getId() == 0:
			signal = model.get_signal()
			self.plot_signal(signal)
		elif model.getId() == 1:
			signal = model.get_signal()
			self.plot_signal(signal, "blue")
		else:
			raise("Error")

	# Signal X
	def get_magnitude(self, whichOne):
		if whichOne == 0:
			return self.magnitude_x
		elif whichOne == 1:
			return self.magnitude_y
		else:
			raise("Error")

	def get_frequency(self, whichOne):
		if whichOne == 0:
			return self.frequency_x
		elif whichOne == 1:
			return self.frequency_y
		else:
			raise("Error")

	def get_phase(self, whichOne):
		if whichOne == 0:
			return self.phase_x
		elif whichOne == 1:
			return self.phase_y
		else:
			raise("Error")

	def get_step_x(self):
		return self.step_x

	def get_step_y(self):
		return self.step_y

	def getX(self):
		print("update_X(self,event)")
		self.caseY.deselect()
		self.caseXY.deselect()
		self.showX = True
		self.showY = False
		self.update(self.model_x)
		if self.canvas.find_withtag("signal_y") :
			self.canvas.delete("signal_y")
	
	def getY(self):
		print("update_Y(self,event)")
		self.caseX.deselect()
		self.caseXY.deselect()
		self.showX = False
		self.showY = True
		self.update(self.model_y)
		if self.canvas.find_withtag("signal_x") :
			self.canvas.delete("signal_x")
	        
	def getXY(self):
		print("update_XY(self,event)")
		self.caseX.deselect()
		self.caseY.deselect()
		self.showX = True
		self.showY = True
		self.update(self.model_x)
		self.update(self.model_y)

	def plot_signal(self, signal, color="red"):
		w, h = self.wi, self.hi
		width,height = int(w), int(h)
		if color == "red" and self.showX==True:
			if self.canvas.find_withtag("signal_x") :
				self.canvas.delete("signal_x")
			if signal and len(signal) > 1:
				plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
				signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal_x")		
		elif color == "blue" and self.showY == True:
			if self.canvas.find_withtag("signal_y") :
				self.canvas.delete("signal_y")
			if signal and len(signal) > 1:
				plot = [(x*width, height/2.0*(y+1)) for (x, y) in signal]
				signal_id = self.canvas.create_line(plot, fill=color, smooth=1, width=3,tags="signal_y")

	def grid(self, step_x, step_y):
		w, h = self.wi, self.hi
		width, height = int(w), int(h)
		self.stepx=(width-10)/step_x*1.
		self.stepy=(height-10)/step_y*1.
		for t in range(1,step_x+2):
			x = t*self.stepx
			self.canvas.create_line(x,0,x,height,tags="grid")
			#self.canvas.create_line(x,height/2-4,x,height/2+4)
		for t in range(1, step_y+2):
			y = t*self.stepy
			self.canvas.create_line(0,y,width,y,tags="grid")
			#self.canvas.create_line(width/2-4,y,width/2+4,y)

	def resize(self, event):
		if event:
			self.wi = event.width
			self.hi = event.height
                        
			self.canvas.delete("grid")
			self.plot_signal(self.model_x.get_signal())
			self.plot_signal(self.model_y.get_signal(), "blue")
			self.grid(25, 25)

	def packing(self) :
		self.canvas.pack(fill="both", expand=1)
		self.step_x.pack(expand=1, fill="both")
		self.step_y.pack(expand=1, fill="both")
		self.frame.pack(expand=1, fill="both")
		self.magnitude_x.grid(row=0, column=0)
		self.magnitude_y.grid(row=0, column=1)
		self.frequency_x.grid(row=1, column=0)
		self.frequency_y.grid(row=1, column=1)
		self.phase_x.grid(row=2, column=0)
		self.phase_y.grid(row=2, column=1)
		self.frame2.pack(side="bottom", expand=1)
		self.lbl.grid(row=0, column=0)
		self.caseX.grid(row=0, column=1)
		self.caseY.grid(row=0, column=2)
		self.caseXY.grid(row=0, column=3)

