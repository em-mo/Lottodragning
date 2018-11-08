#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lotto.py
#
#  Copyright 2012 Emil <emil@emil-luftbunt>
#

import Tkinter as tk
from time import sleep, time
from animated_number import AnimatedNumber
from lotto_canvas import LottoCanvas
from canvas_button import CanvasButton
from canvas_item import CanvasItem
from lottery_number_display import LotterNumberDisplay
from number_bar import NumberBar
from raffle import Raffle
from dialog import Dialog

SIDE_NUMBER_SIZE = 1.0 / 4

class LotteryLayout:
    def __init__(self):
        self.run = True

        self.root = tk.Tk()
        self.init_images()
        self.init_menu(self.root)
        self.root.title("Lotto!")

        self.root.protocol('WM_DELETE_WINDOW', self.destroy_callback)
        self.root.minsize(800, 500)
        self.root.geometry('1024x600')

        self.init_raffles()

        self.init_main_canvas()

        self.init_buttons()

        self.init_bar_and_display()

        self.main_canvas.focus_set()
        return

    def init_menu(self, parent):
        self.menu = tk.Menu(parent)
        parent.config(menu=self.menu)
        self.menu.add_command(label="Nytt lotteri", command=self.configure_callback)
        return

    def init_main_canvas(self):
        self.main_canvas = LottoCanvas(self.root, bd=0, highlightthickness=0, relief='ridge')
        self.main_canvas.bind('<Configure>', self.main_canvas.resize)
        self.main_canvas.bind('<Button-1>', self.main_canvas.handle_event)
        self.main_canvas.bind('<Button-3>', self.roll_callback)
        self.set_background()
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.root.update()

        return

    def init_buttons(self):
        self.red_button = CanvasButton(self.main_canvas, 0, 0.15, CanvasItem.W, self.red_button_full_image, self.red_button_callback)
        self.white_button = CanvasButton(self.main_canvas, 0, 0.383, CanvasItem.W, self.white_button_half_image, self.white_button_callback)
        self.yellow_button = CanvasButton(self.main_canvas, 0, 0.616, CanvasItem.W, self.yellow_button_half_image, self.yellow_button_callback)
        self.green_button = CanvasButton(self.main_canvas, 0, 0.85, CanvasItem.W, self.green_button_half_image, self.green_button_callback)
        return

    def init_bar_and_display(self):
        self.main_display = LotterNumberDisplay(self.main_canvas, 0.5, 1, CanvasItem.S, self.main_red_image, self.number_images)
        self.main_display.init_numbers(self.active_raffle.size, 000)
        self.side_number_bar = NumberBar(self.main_canvas, 1, 0, CanvasItem.NE, self.small_number_images, self.active_raffle.size)
        return

    def set_background(self):
        self.background_image = self.main_canvas.create_image(0, 0, image=self.background_photo_image, anchor=tk.NW)
        self.side_image = self.main_canvas.create_image(0, 0, image=self.side_thing, anchor=tk.NW)
        return

    def init_images(self):
        self.red_button_half_image = tk.PhotoImage(file='bilder/Liten_halv_rod2.gif')
        self.red_button_full_image = tk.PhotoImage(file='bilder/Liten_rod2.gif')
        self.main_red_image = tk.PhotoImage(file='bilder/Main_rod2.gif')

        self.yellow_button_half_image = tk.PhotoImage(file='bilder/Liten_halv_gul2.gif')
        self.yellow_button_full_image = tk.PhotoImage(file='bilder/Liten_gul2.gif')
        self.main_yellow_image = tk.PhotoImage(file='bilder/Main_gul2.gif')

        self.green_button_half_image = tk.PhotoImage(file='bilder/Liten_halv_gron2.gif')
        self.green_button_full_image = tk.PhotoImage(file='bilder/Liten_gron2.gif')
        self.main_green_image = tk.PhotoImage(file='bilder/Main_gron2.gif')

        self.white_button_half_image = tk.PhotoImage(file='bilder/Liten_halv_vit2.gif')
        self.white_button_full_image = tk.PhotoImage(file='bilder/Liten_vit2.gif')
        self.main_white_image = tk.PhotoImage(file='bilder/Main_vit2.gif')

        self.background_photo_image = tk.PhotoImage(file='bilder/BG.gif')
        self.side_thing = tk.PhotoImage(file='bilder/Sidsak.gif')

        self.small_number_images = list()
        self.number_images = list()
        for i in range(10):
            self.small_number_images.append(tk.PhotoImage(file=self.number_path(i)).subsample(int(round(1 / SIDE_NUMBER_SIZE))))
            self.number_images.append(tk.PhotoImage(file=self.number_path(i)))
        return

    def init_raffles(self):
        self.red_raffle = Raffle()
        self.white_raffle = Raffle()
        self.yellow_raffle = Raffle()
        self.green_raffle = Raffle()
        self.active_raffle = self.red_raffle

    def number_path(self, num):
        return 'bilder/nr/' + str(num) + 's.gif'

    def destroy_callback(self):
        self.run = False
        return

    def red_button_callback(self):
        self.set_buttons_to_half()
        self.red_button.set_image(self.red_button_full_image)
        self.main_display.set_image(self.main_red_image)
        self.switch_raffle(self.red_raffle)

    def white_button_callback(self):
        self.set_buttons_to_half()
        self.white_button.set_image(self.white_button_full_image)
        self.main_display.set_image(self.main_white_image)
        self.switch_raffle(self.white_raffle)

    def yellow_button_callback(self):
        self.set_buttons_to_half()
        self.yellow_button.set_image(self.yellow_button_full_image)
        self.main_display.set_image(self.main_yellow_image)
        self.switch_raffle(self.yellow_raffle)

    def green_button_callback(self):
        self.set_buttons_to_half()
        self.green_button.set_image(self.green_button_full_image)
        self.main_display.set_image(self.main_green_image)
        self.switch_raffle(self.green_raffle)

    def switch_raffle(self, raffle):
        self.active_raffle = raffle
        self.reset_displays()
        return

    def reset_displays(self):
        self.main_display.init_numbers(self.active_raffle.size, 0)
        self.side_number_bar.reset(self.active_raffle.size)
        for n in self.active_raffle.drawn_numbers:
            self.side_number_bar.add_number(n)

    def roll_callback(self, event):
        if not self.main_display.is_rolling():
            self.main_display.start_animation()

            if self.active_raffle.drawn_numbers:
                old_number = self.active_raffle.get_latest()
            else:
                old_number = 0

            new_number = self.active_raffle.draw_one()
            if new_number:
                self.main_display.set_value(new_number)

            if self.active_raffle.drawn_numbers and self.side_number_bar.latest_drawn_number != old_number and old_number != 0:
                self.side_number_bar.add_number(old_number)

        return

    def configure_callback(self, event = None):
        d = Dialog(self.root, 'Konfigurera', self.red_raffle.size, self.white_raffle.size, self.yellow_raffle.size, self.green_raffle.size)
        if d.result:
            self.set_raffles(d.result)

            self.set_buttons_to_half()
            self.set_buttons_to_half()
            self.red_button.set_image(self.red_button_full_image)
            self.main_display.set_image(self.main_red_image)
            self.switch_raffle(self.red_raffle)
        return


    def set_raffles(self, raffle_values):
        red, white, yellow, green = raffle_values

        self.red_raffle = Raffle(red)
        self.white_raffle = Raffle(white)
        self.yellow_raffle = Raffle(yellow)
        self.green_raffle = Raffle(green)
        self.active_raffle = self.red_raffle
        return



    def set_buttons_to_half(self):
        self.red_button.set_image(self.red_button_half_image)
        self.white_button.set_image(self.white_button_half_image)
        self.yellow_button.set_image(self.yellow_button_half_image)
        self.green_button.set_image(self.green_button_half_image)

    def start(self):
        self.prevClock = time()

        while self.run:
            self.curClock = time()
            delta = self.curClock - self.prevClock
            self.prevClock = self.curClock
            self.main_display.update(delta)

            self.root.update()
            sleep(0.020)

        self.root.destroy()
