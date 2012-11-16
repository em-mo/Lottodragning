#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  raffle.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  
from random import randint


class Raffle:
	def __init__(self, size):
		self.size = size
		self.numbers = range(1, size)
		self.remaining_numbers = range(1, size)
		self.drawn_numbers = list()

	def draw(amount):
		result = list()
		for i in range amount:
			if remaining_numbers:
				result.append(self.remaining_numbers.pop(randint(0, len(remaining_numbers) - 1)))

		return result

	def draw_one():
		return draw(1)[0]