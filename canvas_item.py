#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  canvas_item.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

class CanvasItem:
	def __init__(self, parent):
		parent.register_item(self)
		return
		
	def reposition(self):
		pass
		
	def handle_event(self, event):
		pass