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
from number_canvas import NumberCanvas

images = list()
anims = list()  
run = True

def roll_text():
    return 'Nytt nummer!'

def init_menu(root):
    menu = Menu(root)
    root.config(menu=menu)
    
    menu.add_command(label="Nytt lotteri", command=new_raffle_callback)

def destroy_callback():
    global run
    run = False

def new_raffle_callback():
    pass

def roll_callback():
    pass
    
def configure_callback(event):
    pass
    
def init_images():
    number_images_paths = {0:'bilder/zero.gif', 1:'bilder/one.gif', 2:'bilder/two.gif'}
    images.append(PhotoImage(file=number_images_paths[0]))
    images.append(PhotoImage(file=number_images_paths[1]))
    images.append(PhotoImage(file=number_images_paths[2]))

def main():
    global run
    i = 0
    delta = clock()
    
    root = Tk()
    init_images()
    init_menu(root)
    root.title("Lotto!")
    
    root.protocol('WM_DELETE_WINDOW', destroy_callback)
    root.config(width=500, height=500)
    
    left_bar = Frame(root)
    roll_button = Button(left_bar, text=roll_text(), command=roll_callback)
    roll_button.pack(side=TOP, padx=2, pady=10)
    left_bar.pack(side=LEFT, fill=Y)
    
    main_canvas = NumberCanvas(root)
    main_canvas.bind('<Configure>', configure_callback)
    
    main_canvas.add_number(AnimatedNumber(main_canvas, 100, 100, 0.5, 0, images, 0, 2))
    
    main_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    
    while run:
        delta = clock() - delta
        main_canvas.get_numbers()[0].update(delta)
        
        root.update()
        sleep(0.020)
        
    root.destroy()
        

if __name__ == '__main__':
    main()