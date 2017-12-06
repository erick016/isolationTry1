#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:51:46 2017

@author: gLestrade
"""

from game_agent import *
from isolation import *
import timeit

def time_left(): 
    time_millis = lambda: 1000 * timeit.default_timer()
    move_start = time_millis()
    return(150 - (time_millis() - move_start))

#isoPlayer = IsolationPlayer
mmPlayer = MinimaxPlayer()
abPlayer = AlphaBetaPlayer()
myBoard = isolation.Board(mmPlayer, abPlayer)
best_move = mmPlayer.get_move(myBoard, time_left)
best_move2 = abPlayer.get_move(myBoard, time_left)
