#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dialog.py

from Tkinter import *
import os

class Dialog(Toplevel):

    def __init__(self, parent, title, red_old, white_old, yellow_old, green_old):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        self.red_old = red_old
        self.white_old = white_old
        self.yellow_old = yellow_old
        self.green_old = green_old

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        body = Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=5, pady=5)

        self.buttonbox()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx()+50,
                                  parent.winfo_rooty()+50))

        self.initial_focus.focus_set()

        self.wait_window(self)

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden
        Label(master, text="Mata in maxvärden, mindre än 1000").grid(row=0, columnspan=2)
        red_label = Label(master, text="Röd:")
        white_label = Label(master, text="Vit:")
        yellow_label = Label(master, text="Gul:")
        green_label = Label(master, text="Grön:")

        red_label.grid(row=1)
        white_label.grid(row=2)
        yellow_label.grid(row=3)
        green_label.grid(row=4)

        self.red_entry = Entry(master)
        self.white_entry = Entry(master)
        self.yellow_entry = Entry(master)
        self.green_entry = Entry(master)

        self.red_entry.insert(0, str(self.red_old))
        self.white_entry.insert(0, str(self.white_old))
        self.yellow_entry.insert(0, str(self.yellow_old))
        self.green_entry.insert(0, str(self.green_old))

        self.red_entry.grid(row=1, column=1)
        self.white_entry.grid(row=2, column=1)
        self.yellow_entry.grid(row=3, column=1)
        self.green_entry.grid(row=4, column=1)
        return self.red_entry # initial focus

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default=ACTIVE)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):
        try:
            a = int(self.red_entry.get())
            b = int(self.white_entry.get())
            c = int(self.yellow_entry.get())
            d = int(self.green_entry.get())
            if a > 999 or b > 999 or c > 999 or d > 999 or a < 1 or b < 1 or c < 1 or d < 1:
                return 0
        except ValueError:
            return 0
        return 1 # override

    def apply(self):
        a = int(self.red_entry.get())
        b = int(self.white_entry.get())
        c = int(self.yellow_entry.get())
        d = int(self.green_entry.get())

        self.result = a, b, c, d