#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:51:46 2017

@author: gLestrade
"""

from game_agent_test_b import *
from isolation import *

#isoPlayer = IsolationPlayer
mmPlayer = MinimaxPlayer()
abPlayer = AlphaBetaPlayer()
myBoard = isolation.Board(mmPlayer, abPlayer)
best_move = mmPlayer.get_move(myBoard, mmPlayer.myTimeoutFn)
best_move2 = abPlayer.get_move(myBoard,abPlayer.myTimeoutFn)
