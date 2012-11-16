#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lottery_number_display.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

import Tkinter as tk
from canvas_item import CanvasItem
from composite_number import CompositeNumber

class LotterNumberDisplay(CanvasItem):
	def __init__(self, parent, relx, rely, anchor, image, number_images):
		CanvasItem.__init__(self, parent, relx, rely, anchor, image.width(), image.height())
		self.image = image
		self.number_images = number_images
		
		self.image_item = parent.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

		return
		
	def init_numbers(self, max_value, value):
		no_numbers = 1
		while pow(10, no_numbers) < max_value:
			no_numbers += 1
		
		
		x = self.x - self.anchor_x
		y = self.y - self.anchor_y - (self.height * 4) / 5
		self.lottery_number = CompositeNumber(self.parent, no_numbers, x, y, self.number_images)
		self.lottery_number.set_value(value)
		return
		
	def start_animation(self):
		self.lottery_number.start_roll()
		
	def update(self, delta):
		self.lottery_number.update(delta)