#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  composite_number.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from Tkinter import Canvas
from math import pow, floor
from animated_number import AnimatedNumber

class CompositeNumber(Canvas):
	def __init__(self, canvas, no_numbers, x, y):
        update_time = 0.05
        self.value = 0
        self.number_margin = 3
        
        self.number_images = list()
        self.numbers = list()
        for i in range(10):
            self.number_images.append(tk.PhotoImage(file=self.number_path(i)))
        
    	self.number_width = self.number_images[0].width() + self.number_margin
            
        centered_x = x - (no_numbers * self.number_width - self.number_margin) / 2
        centered_y = y - self.number_images[0].height() / 2
        
        for i in range(no_numbers):
        	offset = number_width * i
        	self.numbers.append(AnimatedNumber(canvas, x + offset, y, update_time, value, number_images))
        	
    def width(self):
    	return len(self.numbers) * self.number_width - self.number_margin
		
    def number_path(self, num):
        return 'bilder/nr/' + str(num) + 's.gif'
		
	def set_value(self, value):
		chars = self.divide_into_singles(value)
		
		i = 0
		for num in self.numbers:
			num.set_value(chars[i])
			i += 1

	def divide_into_singles(value):
		no_chars = 1
		while pow(10, no_chars) < value:
			no_chars += 1
		
		chars = list()
		
		last_char = 0
		rest = 0
		for i in reversed(range(no_chars)):
			chars.append(int(floor((value - rest) / pow(10, i))))
			rest += (chars[no_chars - i - 1] * pow(10, i))
			print rest
		
		return chars
		
	def start_roll():
		for n in self.numbers:
			n.animate(True)
			
	def stop_next():
		numbers[self.current_stopper].animate(False)
		
