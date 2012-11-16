#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lotto.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

import Tkinter as tk
from time import sleep, clock
from animated_number import AnimatedNumber
from lotto_canvas import LottoCanvas
from canvas_button import CanvasButton
from canvas_item import CanvasItem
from lottery_number_display import LotterNumberDisplay
from number_bar import NumberBar

class LotteryLayout:
    def __init__(self):
        
        self.run = True
        
        self.root = tk.Tk()
        self.init_images()
        self.init_menu(self.root)
        self.root.title("Lotto!")
    
        self.root.protocol('WM_DELETE_WINDOW', self.destroy_callback)
        self.root.minsize(1024, 600)
        
        self.init_main_canvas()
        
        self.root.update()
        
        self.init_buttons()
        
        self.init_bar_and_display()

        self.main_canvas.focus_set()
        return

    def init_menu(self, parent):
        self.menu = tk.Menu(parent)
        parent.config(menu=self.menu)
        self.menu.add_command(label="Nytt lotteri", command=self.new_raffle_callback)
        return
        
    def init_main_canvas(self):
        self.main_canvas = LottoCanvas(self.root, bd=0, highlightthickness=0, relief='ridge')
        self.main_canvas.bind('<Configure>', self.main_canvas.resize)
        self.main_canvas.bind('<Button-1>', self.main_canvas.handle_event)
        
        self.set_background()
        self.main_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        return

    def init_buttons(self):
        self.red_button = CanvasButton(self.main_canvas, 0, 0.15, CanvasItem.W, self.red_button_full_image, self.red_button_callback)
        self.white_button = CanvasButton(self.main_canvas, 0, 0.375, CanvasItem.W, self.white_button_half_image, self.white_button_callback)
        self.yellow_button = CanvasButton(self.main_canvas, 0, 0.625, CanvasItem.W, self.yellow_button_half_image, self.yellow_button_callback)
        self.green_button = CanvasButton(self.main_canvas, 0, 0.85, CanvasItem.W, self.green_button_half_image, self.green_button_callback)
        return
    
    def init_bar_and_display(self):
        self.main_display = LotterNumberDisplay(self.main_canvas, 0.5, 1, CanvasItem.S, self.main_red_image, self.number_images)
        self.main_display.init_numbers(1000, 323)
        
        self.side_number_bar = NumberBar(self.main_canvas, 1, 0, CanvasItem.NE, self.small_number_images, 1000)
        self.side_number_bar.add_number(111)        
        self.side_number_bar.add_number(112)        
        self.side_number_bar.add_number(113)        
        self.side_number_bar.add_number(114)        
        self.side_number_bar.add_number(115)        
        self.side_number_bar.add_number(116)        
        self.side_number_bar.add_number(117)        
        self.side_number_bar.add_number(118)        
        self.side_number_bar.add_number(119)        
        self.side_number_bar.add_number(110)        
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
        self.side_thing = tk.PhotoImage(file='bilder/sidsak.gif')
        
        self.small_number_images = list()
        self.number_images = list()
        for i in range(10):
            self.small_number_images.append(tk.PhotoImage(file=self.number_path(i)).subsample(2))
            self.number_images.append(tk.PhotoImage(file=self.number_path(i)))
            
        
        return
        
    def number_path(self, num):
        return 'bilder/nr/' + str(num) + 's.gif'
        
    def destroy_callback(self):
        self.run = False
        return
    
    def red_button_callback(self):
        self.set_buttons_to_half()
        self.red_button.set_image(self.red_button_full_image)
    
    def white_button_callback(self):
        self.set_buttons_to_half()
        self.white_button.set_image(self.white_button_full_image)

    def yellow_button_callback(self):
        self.set_buttons_to_half()
        self.yellow_button.set_image(self.yellow_button_full_image)

    def green_button_callback(self):
        self.set_buttons_to_half()
        self.green_button.set_image(self.green_button_full_image)
    
    def new_raffle_callback(self):
        pass

    def roll_callback(self):
        pass
        
    def configure_callback(self, event):
        pass
        
    def set_buttons_to_half(self):
        self.red_button.set_image(self.red_button_half_image)
        self.white_button.set_image(self.white_button_half_image)
        self.yellow_button.set_image(self.yellow_button_half_image)
        self.green_button.set_image(self.green_button_half_image)
        
        

    def start(self):
        self.prevClock = clock()
    
        while self.run:
            self.curClock = clock()
            delta = self.curClock - self.prevClock
            self.prevClock = self.curClock
            self.main_display.update(delta)

            self.root.update()
            sleep(0.020)
        
        self.root.destroy()

def main():
    lottery = LotteryLayout()
    lottery.start()
        

if __name__ == '__main__':
    main()