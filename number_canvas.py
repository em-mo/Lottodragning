#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_canvas.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from Tkinter import Canvas

class NumberCanvas(Canvas):
	def __init__(self, parent, **kwargs):
		Canvas.__init__(self, parent, **kwargs)
		self.numbers = list()
	
	def add_number(self, number):
		self.numbers.append(number)
		
	def get_numbers(self):
		return self.numbers