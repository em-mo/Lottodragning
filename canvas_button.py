#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  canvas_button.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from canvas_item import CanvasItem
from lotto_canvas import LottoCanvas
import Tkinter as tk

class CanvasButton(CanvasItem):	
	def __init__(self, parent, relx, rely, anchor, image, command):
		CanvasItem.__init__(self, parent)
		self.parent = parent
		self.image = image
		self.invoke = command
		self.relx = relx
		self.rely = rely
		
		self.anchor_x, self.anchor_y = anchor(self)
		
		width = self.parent.winfo_width()
		height = self.parent.winfo_height()
		
		self.x = relx * width + self.anchor_x + LottoCanvas.sidebar_offset
		self.y = rely * height + self.anchor_y
				
		self.image_item = parent.create_image(self.x, self.y, image=self.image, anchor=tk.NW)
		return
		
	def NW(self):
		return 0, 0
	
	def W(self):
		return 0, -self.image.height() / 2
		
	def S(self):
		return -self.image.width() / 2, -self.image.height()
		
	def set_image(self, new_image):
		self.parent.itemconfigure(self.image_item, image=new_image)
		
	def reposition(self, event):
		print 'repos'
		width = event.width
		height = event.height
		self.x = self.relx * width + self.anchor_x + LottoCanvas.sidebar_offset
		self.y = self.rely * height + self.anchor_y
		
		self.parent.coords(self.image_item, self.x, self.y)
		return
	
	def inside(self, x, y):
		top = self.y
		bottom = self.y + self.image.height()
		left = self.x
		right = self.x + self.image.width()
		
		return x >= left and x <= right and y >= top and y <= bottom
		
	def handle_event(self, event):
		if self.inside(event.x, event.y):
			self.invoke()
		return
		
		
	