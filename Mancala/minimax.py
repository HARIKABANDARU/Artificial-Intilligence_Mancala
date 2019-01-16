from itertools import count
from mancala import *
import math


def minimax(game, state, max_depth=None,ncount=0):
    """
    Run minimax search from the current game state up to a maximum search depth.
    Return the best utility found for the current player, the best next action,
    and the number of nodes encountered during the search.
    """
    #Player 0 as maximising player and player #1 as minimising player

    ####################################################################
    ##   Should Ask what do best next action means and number nodes   ##     
    ####################################################################
    ## Finish me! ##
    # Update the following code to return the correct node count
    # and the correct utility.
    
    

    if game.is_over(state) or max_depth == 0: return game.score(state), None, 1
    #print(state)
    actions = game.actions(state)
    #print(actions)
    utilities = []
    
    node_count = 0
    if game.player(state) == 0:
        value = -(math.inf)
        for action in actions:
            new_state = game.result(state,action)
            #node_count+=1
            m,_,nc = minimax(game,new_state,None if max_depth is None else max_depth - 1,ncount)
            #print(nc)
            '''if ncount == 0:
                ncount = 1'''
            if ncount < nc:
                ncount = nc+1
            else:
            
                ncount+=1
            #ncount+=(nc+1)
            #print("from Min")
            #print(ncount)
            value = max(value,m)#minimax(game,new_state,None))
            utilities.append(value)
        return value,actions[utilities.index(value)],ncount
    elif game.player(state) == 1:
        value = math.inf
        for action in actions:
            new_state = game.result(state,action)
            n,_,nc = minimax(game,new_state,None if max_depth is None else max_depth - 1,ncount)
            #print(nc)
            if(ncount < nc):
                ncount = nc+1
            else:
                ncount+=1
            
            value = min(value,n)#minimax(game,new_state,None))
            utilities.append(value)
        return value,actions[utilities.index(value)],ncount
        
                        
                        
    
  
def minimax_ab(game, state, alpha=-(math.inf), beta=math.inf, max_depth=None,ncount=0):
    """
    Run minimax search with alpha-beta pruning.
    """

    ## Finish me! [grad] ##
    # Update the following code to return the correct node count
    # and the correct utility.
    actions = game.actions(state)
    utilities = []
    nc = 0
    

    if game.is_over(state) or max_depth == 0: return game.score(state), None, 1
    if game.player(state) == 0:
        value = -(math.inf)
        for action in actions:
            new_state = game.result(state,action)
            
            m,_,nc = minimax_ab(game,new_state,alpha,beta,None if max_depth is None else max_depth - 1,ncount)
            if ncount < nc:
                ncount = nc+1
            else:
            
                ncount+=1
            
            
            value = max(value, m)#minimax_ab(game, new_state,alpha,beta,None))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        utilities.append(value)
        return value,actions[utilities.index(value)],ncount
    else:
        value = math.inf
        for action in actions:
            new_state = game.result(state,action)
            
            n,_,nc = minimax_ab(game,new_state,alpha,beta,None if max_depth is None else max_depth - 1,ncount)
            if ncount < nc:
                ncount = nc+1
            else:
            
                ncount+=1
            
            value = min(value, n)#minimax_ab(game, new_state,alpha,beta,None))
            beta = min(beta, value)
            if alpha >= beta:
                break
        utilities.append(value)
        return value,actions[utilities.index(value)],ncount

   
def play(game, alg, moves=None, verbose=False):

    state = game.initial()
    if verbose: print(game.string(state))

    player = game.player(state)
    turn = 0
    full_node_count = 0
    for move in count():

        if game.is_over(state): break
        if move == moves: break
    
        if player != game.player(state): turn += 1
        player = game.player(state)
        score = game.score(state)
        utility, action, node_count = alg(game, state)
        if move == 0: full_node_count = node_count

        if verbose: print("Move %d, turn %d: Player %d's move = %d, utility = %d, score = %d"%(
            move, turn, player, action, utility, score))
        if verbose: print("")

        state = game.result(state, action)
        if verbose: print(game.string(state))

    if verbose: print("Final score: %d, node count = %d" % (game.score(state), full_node_count))
    return game.score(state)

def play_minimax(game, max_depth=None, moves=None, verbose=False):
    alg = lambda game, state: minimax(game, state, max_depth=max_depth)
    final_score = play(game, alg, moves=moves, verbose=verbose)
    return final_score

#fuction written to play_minmax with pruinig usinf alpha and beta
def play_minimax_ab(game,max_depth=None,moves=None,verbose=False):
    alg = lambda game,state:minimax_ab(game,state,max_depth=max_depth)
    final_score = play(game,alg,moves=moves,verbose=verbose)
    return final_score
if __name__ == "__main__":

    """
    Scratch pad for informal tests
    """

    max_depth = 5
    moves = 100
    verbose=True
    mg = MancalaGame(size=5, count=2)

    fs = play_minimax(mg, max_depth=max_depth, moves=moves, verbose=verbose)

    # alg = lambda game, state: minimax_ab(game, state, max_depth=max_depth)
    # fs_ab = play(mg, alg, moves=moves, verbose=verbose)

    print("minimax: %f" % fs)
    # print("ab: %f" % fs_ab)

