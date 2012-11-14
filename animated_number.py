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
		AnimatedImage.__init__(self, canvas, x, y, update_time, value, images)
		self.min = min
		self.max = max
		
	def update(self, time):
		self.current_timer -= time
		if self.current_timer < 0:
			self.set_value(randint(self.min, self.max))
			self.current_timer = self.update_time