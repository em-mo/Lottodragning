#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  animated_image.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from animated_image import AnimatedImage
from random import randint

class AnimatedNumber(AnimatedImage):
	def __init__(self, canvas, x, y, update_time, value, images, min = 0, max = 9):
		AnimatedImage.__init__(self, canvas, x, y, update_time, images)
		self.min = min
		self.max = max
		self.value = value;
		self.run_animation = False
		self.image_value = value
		
	def update(self, time):
		if self.run_animation:
			self.current_timer -= time
			if self.current_timer < 0:
				new_value = randint(self.min, self.max)
				while self.image_value == new_value:
					new_value = randint(self.min, self.max)
				
				self.image_value = new_value
				
				self.set_image(self.image_value)
				self.current_timer = self.update_time
	
	def set_image(self, value):
		self.image = self.images[value]
		self.canvas.itemconfig(self.canvas_image, image=self.image)
	
	def set_value(self, value):
		self.value = value
		if not self.run_animation:
			self.image_value = value
			self.set_image(self.image_value)
	
	def animate(self, bool):
		self.run_animation = bool
		if not bool:
			self.image = self.images[value]
			self.canvas.itemconfig(self.canvas_image, image=self.image)