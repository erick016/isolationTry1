class AlphaBetaPlayer(IsolationPlayer):

        self.time_left = time_left
 
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)
        self.search_depth = 1
        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            while (True):
                move = self.alphabeta(game, self.search_depth)
                #print(best_move)
                if move is not (-1,-1):
                    best_move = move
                self.search_depth += 1
               
                #return self.minimax(game, self.search_depth)
                if self.time_left() < self.TIMER_THRESHOLD:
                    raise SearchTimeout()  # @ was returning score                  
 
        except SearchTimeout:
            return best_move  # Handle any actions required after timeout as needed
           
        # Return the best move from the last completed search iteration
        return best_move
 
    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
 
        #result = alphabeta_decision(self,game,depth,True,alpha,beta,(-1,-1))
        #return(result[1])
 
        movesList = game.get_legal_moves()
       
            #@if not movesList:
            #@return (-1,-1)

        bestMoveSoFar = (-1,-1)            
 
        movesListLen = len(movesList) 
       
        if (movesListLen == 0):
            myScore = (self.score(game))
            return myScore
       
        if (depth == 0):
             myScore = (self.score(game))
             return myScore    
           
        #@examinedScore = float('-inf')
       #@self.bestMoveSoFar = movesList[0]
 
           
        for m in movesList:
 
            examinedState = game.forecast_move(m)
            examinedScore = alphabeta_decision(self,examinedState,depth - 1,False,alpha,beta)
 
            if examinedScore > alpha:
                alpha = examinedScore
                bestMoveSoFar = m #@ this was only being assigned if beta was greater than alpha
           
            if beta <= alpha:
                break
               
        return bestMoveSoFar
 
def alphabeta_decision(caller,game,depth,maximizingPlayer,alpha,beta):
   
    if caller.time_left() < caller.TIMER_THRESHOLD:
        raise SearchTimeout()
   
    movesList = game.get_legal_moves()
 
    movesListLen = len(movesList)
 
    #scoredMovesList = list()
       
    #returnTuple = (0,(-1,-1))
 
    #scoredMovesList.append(returnTuple)
   
    """if (depth == 0) or (movesListLen == 0):
        returnTuple = (caller.score(game,caller),(-1,-1))
        return returnTuple"""
 
       
    if (depth == 0):
       
        myScore = (caller.score(game,caller))
        return myScore
       
    if (maximizingPlayer):
 
        if (movesListLen == 0):
            return -1
 
        myScore = float('-inf')
        #myScore = bestSoFar        
 
        for m in movesList:
           
            timeLeftResult = caller.time_left()
            if timeLeftResult < caller.TIMER_THRESHOLD:
                raise SearchTimeout()
           
            myScore = max(myScore,alphabeta_decision(caller,game.forecast_move(m),depth - 1,False,alpha, beta))
 
            if myScore >= beta:
                return myScore
           
            alpha = max(alpha,myScore)
 
        #scoredMovesList.sort(key = lambda x: x[0]) #sorts the list and returns None
        #returnTuple = scoredMovesList[0]    
        return myScore
 
    else:
 
        if (movesListLen == 0):
            return 1
       
        myScore = float('inf')
        #myScore = bestSoFar
        for m in movesList:
           
            timeLeftResult = caller.time_left()
            if timeLeftResult < caller.TIMER_THRESHOLD:
                raise SearchTimeout()
                       
            myScore = min(myScore,alphabeta_decision(caller,game.forecast_move(m),depth - 1,True,alpha, beta))
 
            if myScore <= alpha:
                return myScore
           
            beta = min(beta,myScore)            
       
        #scoredMovesList.sort(key = lambda x: x[0])
        #returnTuple = scoredMovesList[0]  
        return myScore
