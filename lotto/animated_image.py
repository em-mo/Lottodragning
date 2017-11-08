#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  animated_image.py
#
#  Copyright 2012 Emil <emil@emil-luftbunt>
#

import Tkinter as tk

class AnimatedImage:

    def __init__(self, canvas, x, y, update_time, images):
        self.images = images
        self.image = images[0]
        self.position = {'x':x, 'y':y}
        self.canvas = canvas
        self.update_time = update_time
        self.current_timer = update_time

        self.canvas_image = canvas.create_image(self.position['x'], self.position['y'], image=self.image, anchor=tk.NW)

    def set_position(self, x, y):
        self.canvas.coords(self.canvas_image, x, y)

    def update(self, time):
        pass