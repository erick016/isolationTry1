#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:51:46 2017

@author: gLestrade
"""

from game_agent import *
from isolation import *

#isoPlayer = IsolationPlayer
mmPlayer = MinimaxPlayer()
abPlayer = AlphaBetaPlayer()
myBoard = isolation.Board(mmPlayer, abPlayer)
print(str(mmPlayer.get_move(myBoard,myBoard.time_left)))
print(str(abPlayer.get_move(myBoard,myBoard.time_left)))
