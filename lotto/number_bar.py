#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  number_bar.py
#
#  Copyright 2012 Emil <emil@emil-luftbunt>
#

from canvas_item import CanvasItem
from composite_number import CompositeNumber

PADDING_FACTOR = 1.05

class NumberBar(CanvasItem):
    def __init__(self, parent, relx, rely, anchor, images, max_value):
        CanvasItem.__init__(self, parent, relx, rely, anchor, images[0].width() * 4, parent.winfo_height())

        self.number_images = images
        self.drawn_numbers_list = list()
        self.latest_drawn_number = 0
        self.max_value = max_value

        self.calculate_next_coordinates()
        return

    def reset(self, max_value):
        for n in self.drawn_numbers_list:
            n.destroy()

        self.max_value = max_value
        self.calculate_next_coordinates()
        self.drawn_numbers_list = list()

    def add_number(self, number):
        self.latest_drawn_number = number
        lottery_number = CompositeNumber(self.parent, self.max_value, self.next_number_x, self.next_number_y, self.number_images)
        lottery_number.set_value(number)
        self.drawn_numbers_list.append(lottery_number)

        self.next_number_y += self.number_images[0].height() * PADDING_FACTOR

    def reposition(self, event):
        width = event.width
        height = event.height

        self.set_height(height)
        self.calculate_coordinates(width, height)

        self.update_position()
        return

    def update_position(self):
        self.calculate_next_coordinates()

        for n in self.drawn_numbers_list:
            n.move(self.next_number_x, self.next_number_y)
            self.next_number_y += self.number_images[0].height() * PADDING_FACTOR

    def calculate_next_coordinates(self):
        self.next_number_y = self.number_images[0].height() / 2
        self.next_number_x = self.x + self.width / 2
