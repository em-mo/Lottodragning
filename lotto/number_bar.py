#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_bar.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from canvas_item import CanvasItem
from composite_number import CompositeNumber

class NumberBar(CanvasItem):
	MAX_NUMBER_OF_NUMBERS = 10
	def __init__(self, parent, relx, rely, anchor, images, max_value):
		CanvasItem.__init__(self, parent, relx, rely, anchor, images[0].width() * 4, parent.winfo_height())
		self.no_numbers = 1
		while pow(10, self.no_numbers) < max_value:
			self.no_numbers += 1
		
		self.number_images = images
		self.drawn_numbers_list = list()
		
		self.next_number_y = self.height / (NumberBar.MAX_NUMBER_OF_NUMBERS * 2)
		self.next_number_x = self.x + self.width / 2
		return
	
	def add_number(self, number):
		lottery_number = CompositeNumber(self.parent, self.no_numbers, self.next_number_x, self.next_number_y, self.number_images)
		lottery_number.set_value(number)
		self.drawn_numbers_list.append(lottery_number)
		
		self.next_number_y += self.height / NumberBar.MAX_NUMBER_OF_NUMBERS
		
	def reposition(self, event):
		width = event.width
		height = event.height
		
		self.set_height(height)
		self.calculate_coordinates(width, height)
		
		self.update_position()
		return
		
	def update_position(self):
		self.next_number_y = self.height / (NumberBar.MAX_NUMBER_OF_NUMBERS * 2)
		self.next_number_x = self.x + self.width / 2
		
		for n in self.drawn_numbers_list:
			n.move(self.next_number_x, self.next_number_y)
			self.next_number_y += self.height / NumberBar.MAX_NUMBER_OF_NUMBERS
