#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lottery_number_display.py
#
#  Copyright 2012 Emil <emil@emil-luftbunt>
#

import Tkinter as tk
from canvas_item import CanvasItem
from composite_number import CompositeNumber

class LotterNumberDisplay(CanvasItem):
    def __init__(self, parent, relx, rely, anchor, image, number_images):
        CanvasItem.__init__(self, parent, relx, rely, anchor, image.width(), image.height())
        self.image = image
        self.number_images = number_images
        self.animation_started = False
        self.image_item = parent.create_image(self.x, self.y, image=self.image, anchor=tk.NW)
        self.lottery_number = None

        return

    def init_numbers(self, max_value, value):
        x = self.x - self.anchor_x
        y = self.y - self.anchor_y - (self.height * 4) / 5

        if self.lottery_number:
            self.lottery_number.destroy()

        self.lottery_number = CompositeNumber(self.parent, max_value, x, y, self.number_images)
        self.lottery_number.set_value(value)
        return

    def set_value(self, value):
        self.lottery_number.set_value(value)

    def set_image(self, new_image):
        self.parent.itemconfigure(self.image_item, image=new_image)
        return

    def start_animation(self):
        self.lottery_number.start_roll()
        return

    def stop_animation(self):
        self.lottery_number.stop_roll()
        return

    def update(self, delta):
        self.lottery_number.update(delta)
        return

    def update_position(self):
        self.parent.coords(self.image_item, self.x, self.y)

        x = self.x - self.anchor_x
        y = self.y - self.anchor_y - (self.height * 4) / 5

        self.lottery_number.move(x, y)
        return

    def handle_mouse_event_temp(self, event):
        if self.animation_started:
            self.stop_animation()
            self.animation_started = False
        else:
            self.start_animation()
            self.animation_started = True
        return

    def is_rolling(self):
        return self.lottery_number.run_animation
