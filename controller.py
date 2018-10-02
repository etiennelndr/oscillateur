class Controller :
	def __init__(self, model, view):
		self.model = model
		self.view = view
		self.view.canvas.bind("<Configure>", self.view.resize)
		self.view.get_magnitude(model.getId()).bind("<B2-Motion>", self.update_magnitude)
		self.view.get_frequency(model.getId()).bind("<B2-Motion>", self.update_frequency)
		self.view.get_phase(model.getId()).bind("<B2-Motion>", self.update_phase)
		self.view.get_step_x().bind("<Return>", self.update_step_x)
		self.view.get_step_y().bind("<Return>", self.update_step_y)
        
	def update_magnitude(self, event):
		print("update_magnitude")
		x = int(event.widget.get())
		self.model.set_magnitude(x)
		self.model.generate_signal()
	
	def update_frequency(self, event):
		print("update_frequency")
		x = int(event.widget.get())
		self.model.set_frequency(x)
		self.model.generate_signal()
		
	def update_phase(self, event):
		print("update_phase")
		x = int(event.widget.get())
		self.model.set_phase(x)
		self.model.generate_signal()
		
	def update_step_x(self, event):
		print("update step x")
		self.view.canvas.delete("grid")
		self.view.grid(int(self.view.get_step_x().get()), int(self.view.stepy))
		
	def update_step_y(self, event):
		print("update step y")
		self.view.canvas.delete("grid")
		self.view.grid(int(self.view.stepx), int(self.view.get_step_y().get()))
