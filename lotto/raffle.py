#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  raffle.py
#
#  Copyright 2012 Emil <emil@emil-luftbunt>
#

from random import randint

class Raffle:
    def __init__(self, size = 500):
        self.size = size
        self.numbers = range(1, size + 1)
        self.remaining_numbers = range(1, size + 1)
        self.drawn_numbers = list()

    def draw(self, amount):
        result = list()
        for i in range(amount):
            if self.remaining_numbers:
                result.append(self.remaining_numbers.pop(randint(0, len(self.remaining_numbers) - 1)))

        return result

    def draw_one(self):
        result = None
        if self.remaining_numbers:
            result = self.remaining_numbers.pop(randint(0, len(self.remaining_numbers) - 1))
            self.drawn_numbers.append(result)
        return result

    def get_latest(self):
        return self.drawn_numbers[-1]