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
	
		self.x = relx * self.parent.winfo_width() + self.anchor_x + LottoCanvas.sidebar_offset
		self.y = rely * self.parent.winfo_height() + self.anchor_y
		return
		
	def NW(self):
		return 0, 0
	
	def W(self):
		return 0, -self.height / 2
		
	def S(self):
		return -self.width / 2, -self.height
		
	def NE(self):
		return self.width, 0
		
	def set_height(self, height):
		self.height =  height
		self.anchor_x, self.anchor_Y = anchor(self)
	
	def set_width(self, width):
		self.width =  width
		self.anchor_x, self.anchor_Y = anchor(self)
	
	def inside(self, x, y):
		top = self.y
		bottom = self.y + self.height
		left = self.x
		right = self.x + self.width
		
		return x >= left and x <= right and y >= top and y <= bottom
		
	def reposition(self, event):
		width = event.width
		height = event.height
		self.x = self.relx * width + self.anchor_x + LottoCanvas.sidebar_offset
		self.y = self.rely * height + self.anchor_y
		
		self.update_position()
		return
		
	def update_position(self):
		pass
		
	def handle_event(self, event):
		pass