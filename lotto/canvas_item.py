#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  canvas_item.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from lotto_canvas import LottoCanvas

class CanvasItem:
	def __init__(self, parent, relx, rely, anchor, width, height):
		parent.register_item(self)
		self.anchor = anchor
		self.width = width
		self.height = height
		self.parent = parent
		
		self.relx = relx
		self.rely = rely
		
		self.anchor_x, self.anchor_y = anchor(self)
	
		self.calculate_coordinates(self.parent.winfo_width(), self.parent.winfo_height())

		return
	
	def calculate_coordinates(self, width, height):
		self.x = self.relx * (width - LottoCanvas.sidebar_offset) + self.anchor_x + LottoCanvas.sidebar_offset
		self.y = self.rely * height + self.anchor_y
	
	def NW(self):
		return 0, 0
	
	def W(self):
		return 0, -self.height / 2
		
	def S(self):
		return -self.width / 2, -self.height
		
	def NE(self):
		return -self.width, 0
		
	def set_height(self, height):
		self.height =  height
		self.anchor_x, self.anchor_Y = self.anchor(self)
	
	def set_width(self, width):
		self.width =  width
		self.anchor_x, self.anchor_Y = self.anchor(self)
	
	def inside(self, x, y):
		top = self.y
		bottom = self.y + self.height
		left = self.x
		right = self.x + self.width
		
		return x >= left and x <= right and y >= top and y <= bottom
		
	def reposition(self, event):
		width = event.width
		height = event.height
		self.calculate_coordinates(width, height)
		
		self.update_position()
		return
		
	def update_position(self):
		pass
		
	def handle_event(self, event):
		pass