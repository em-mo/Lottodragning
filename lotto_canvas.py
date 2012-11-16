#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lotto_canvas.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from Tkinter import Canvas

class LottoCanvas(Canvas):
	sidebar_offset = 54
	def __init__(self, parent, **kwargs):
		Canvas.__init__(self, parent, **kwargs)
		self.numbers = list()
		self.items = list()
	
	def add_number(self, number):
		self.numbers.append(number)
		
	def get_numbers(self):
		return self.numbers
		
	def register_item(self, item):
		self.items.append(item)
		
	def reposition_items(self):
		for item in self.items:
			item.reposition()
	
	def handle_event(self, event):
		for item in self.items:
			item.handle_event(event)
			
	def resize(self, event):
		print 'resize'
		for item in self.items:
			item.reposition(event)