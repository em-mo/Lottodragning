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
        CanvasItem.__init__(self, parent, relx, rely, anchor, image.width(), image.height())
        self.image = image
        self.invoke = command

        self.image_item = parent.create_image(self.x, self.y, image=self.image, anchor=tk.NW)

        return

    def set_image(self, new_image):
        self.parent.itemconfigure(self.image_item, image=new_image)

    def update_position(self):
        self.parent.coords(self.image_item, self.x, self.y)

    def handle_event(self, event):
        if self.inside(event.x, event.y):
            self.invoke()
        return


