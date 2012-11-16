#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  composite_number.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

import Tkinter as tk
from math import pow, floor
from animated_number import AnimatedNumber

class CompositeNumber(tk.Canvas):
	def __init__(self, canvas, no_numbers, x, y, images):
		self.current_stopper = 0
		update_time = 0.1
		self.value = 0
		self.number_margin = 3
		self.no_numbers = no_numbers

		self.number_images = images
		self.numbers = list()

		self.number_width = self.number_images[0].width() + self.number_margin
		
		centered_x = self.center_x(x)
		centered_y = self.center_y(y)

		for i in range(self.no_numbers):
			offset = self.number_width * i
			self.numbers.append(AnimatedNumber(canvas, centered_x + offset, centered_y, update_time, self.value, self.number_images))
		return

	def center_x(self, x):
		return x - (self.no_numbers * self.number_width - self.number_margin) / 2
		
	def center_y(self, y):
		return y - self.number_images[0].height() / 2

	def number_path(self, num):
		return 'bilder/nr/' + str(num) + 's.gif'
	
	def set_value(self, value):
		chars = self.divide_into_singles(value)
		i = 0
		for num in self.numbers:
			num.set_value(chars[i])
			i += 1

	def divide_into_singles(self, value):
		no_chars = 1
		while pow(10, no_chars) < value:
			no_chars += 1
		
		chars = list()
		
		last_char = 0
		rest = 0
		for i in reversed(range(no_chars)):
			chars.append(int(floor((value - rest) / pow(10, i))))
			rest += (chars[no_chars - i - 1] * pow(10, i))
		if len(chars) < self.no_numbers:
			for i in range(self.no_numbers - len(chars)):
				chars.insert(0, 0)
		return chars
		
	def start_roll(self):
		for n in self.numbers:
			n.animate(True)
			
	def stop_roll(self):
		for n in self.numbers:
			n.animate(False)
			
	def stop_next(self):
		self.numbers[self.current_stopper].animate(False)
		self.current_stopper = (self.current_stopper + 1) % len(self.numbers)
		
	def update(self, delta):
		for n in self.numbers:
			n.update(delta)
			
	def move(self, x, y):
		centered_x = self.center_x(x)
		centered_y = self.center_y(y)
		
		for i in range(self.no_numbers):
			offset = self.number_width * i
			self.numbers[i].set_position(centered_x + offset, centered_y)
		