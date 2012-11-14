#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lotto.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from Tkinter import *
from time import sleep, clock
from animated_number import AnimatedNumber

images = list()

def init_menu(master):
    menu = Menu(master)
    master.config(menu=menu)
    
    menu.add_command(lable="Nytt lotteri", command=new_raffle_callback)

def new_raffle_callback():
    pass
    
def init_images():
    number_images_paths = {0:'bilder/zero.gif', 1:'bilder/one.gif', 2:'bilder/two.gif'}
    images.append(PhotoImage(file=number_images_paths[0]))
    images.append(PhotoImage(file=number_images_paths[1]))
    images.append(PhotoImage(file=number_images_paths[2]))

def main():
    i = 0
    delta = clock()
    
    root = Tk()
    init_images()
    
    main_canvas = Canvas(root, width=500, height=200, bd=0, highlightthickness=0)
    
    anim = AnimatedNumber(main_canvas, 100, 100, 0.5, 0, images, 0, 2)
    
    main_canvas.pack()
    
    while True:
        delta = clock() - delta
        anim.update(delta)

        root.update()
        sleep(0.020)
        

if __name__ == '__main__':
    main()