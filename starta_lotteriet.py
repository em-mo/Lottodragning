#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  starta_lotteriet.py
#  
#  Copyright 2012 Emil <emil@emil-luftbunt>
#  

from lotto.lotto import LotteryLayout

def main():
    lottery = LotteryLayout()
    lottery.start()
        

if __name__ == '__main__':
    main()