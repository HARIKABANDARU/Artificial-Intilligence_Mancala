"""
A game state is represented by a tuple.  The leading elements of
the tuple are the number of stones in each position, from position 0
to the final position. The last element of the tuple is the current
player, either 0 or 1.
"""

class MancalaGame:

    def __init__(self, size=6, count=4):
        self.size = size
        self.count = count

    def initial(self):
        """
        Return the initial game state.
        """
        return ((self.count,)*self.size + (0,))*2 + (0,)

    def player(self, state):
        """
        Return the current player in the given game state.
        """
        return state[-1]
    
    def actions(self, state):
        """
        Return a list of all actions available in the current game state.
        Each action is the position number of a non-empty small position
        on the current player's half of the board.
        """
        actionsAvailable = []
        pos = 0
        if state[-1] == 0:
            for m in state[0:self.size]:
                if m != 0:
                    actionsAvailable.append(pos)
                pos+=1
        pos = self.size+1
        if state[-1] == 1:
                for m in state[self.size+1:-2]:
                    #print(m)
                    #print(pos)
                    if m != 0:
                        actionsAvailable.append(pos)
                    pos+=1
        return actionsAvailable
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))
    
    def result(self, state, action):
        """
        Return the new game state that results from playing the given
        action in the given state.  Be sure to account for the special
        cases where a player's last stone lands in one of their own small
        positions, and when a player's last stone lands in their own mancala.
        """
        actionsAvailable = []
        intialaction = action
        stateList = []
        actionsAvailable = (self.actions(state))
        #print(actionsAvailable)
        if action in actionsAvailable:
            stateList = list(state)
            countRem = stateList[action]
            stateList[action] = 0
            
            for m in range(0,countRem):
                if action <= (2*self.size):
                    #print(action)
                    if (stateList[-1] == 1) and action == self.size:
                        continue
                    if stateList[-1] == 0 and action == 2*self.size:
                        #print(action)
                        action = -1
                        #print(action)
                    
                    action+=1
                    #print(action)
                    stateList[action] = stateList[action] + 1
                        
                else:
                    action = 0
                    stateList[action] = stateList[action] + 1
            #print(action)
            #if landed on the empty space then u have to gather all the stones in opposite side to your own macala and placing zero on both sides of the cup
            if ((stateList[action] == 1) and ((action != self.size and action != 2*self.size+1))):
                if stateList[-1] == 0 and action < self.size:
                    stateList[self.size] += 1 + stateList[-(action+3)]
                    stateList[-(action+3)] = 0
                    stateList[action] = 0
                if stateList[-1] == 1 and action > self.size:
                    stateList[-2] += 1+stateList[-(action+3)]
                    stateList[-(action+3)] = 0
                    stateList[action] = 0
            if (((stateList[-1] == 0) and (intialaction+countRem == self.size)) or ((stateList[-1] == 1) and (intialaction+countRem == (2*self.size)+1))):
                return tuple(stateList)
        
            stateList[-1] = stateList[-1] ^ 1
            return tuple(stateList)
                        
            #print("Perform action")
        else:
            print("Action can not be performed")
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))

    def is_over(self, state):
        """
        Return True if the game is over in the given state, False otherwise.
        The game is over if either player has no stones left in their small positions.
        """
        #print(state)
        gameFlag = True;
        for ele in state[:self.size]:
            if ele != 0:
                gameFlag = False;
        if gameFlag:
            return gameFlag
        gameFlag = True
        for ele in state[self.size+1:-2]:
            if ele != 0:
                gameFlag = False
        return gameFlag
                
        
        
        ## Finish me! ##
        #raise(Exception("Not implemented yet."))

    def score(self, state):
        """
        Return the score in the current state, from player 0's perspective.
        If the game is over and one player still has stones on their side,
        those stones are added to that player's score.
        """
        
        ## Finish me! ##
        ## From explanation score = Stones in current player's macala - stones in opnents macala
        num = 0
        num2 = 0
        num = state[self.size];
        sum = 0
        if self.is_over(state):
            sum = 0;
            
            for m in state[0:self.size]:
                sum+=m
            
        
            #state[self.size] += sum
            num += sum;
            sum = 0
            for m in state[-3:self.size:-1]:
                sum += m
        num2 = state[-2]
        num2+=sum
        #print(num)
        #print(num2)
        if state[-1] == 0:
            return num-num2
        else:
            return num2-num 
        #if self.is_over(state):
        #   for 
        
        
        #raise(Exception("Not implemented yet."))

    def string(self, state):
        """
        Display current state as a game board.  The current player's mancala
        is marked with *.
        """
        z = self.size
        s = " ".join(["%2d"%m for m in state[-2:z:-1]] + [" *" if state[-1]==0 else "  "])
        s += "\n"
        s += " ".join(["  " if state[-1]==0 else " *"] + ["%2d"%m for m in state[:(z+1)]])
        return s

if __name__ == "__main__":

    """
    Scratch pad for informal tests
    """

    mg = MancalaGame(size=3, count=2)

    s = mg.initial()
    print(mg.is_over(s));
    print(s);
    print(mg.string(s))
    #Private Test Case #1
    s = (2,2,2,4,0,0,0,2,0)
    print(mg.score(s))

    #Own Test Cases
    mg = MancalaGame(size  = 6, count = 4)
    s = (0, 0, 2, 0, 2, 8, 3, 6, 1, 1, 5, 0, 0, 8, 1)
    s2 =  (0, 0, 2, 0, 2, 8, 3, 6, 0, 2, 5, 0, 0, 8, 0)
    print(mg.result(s,8))
    print(s2)
    exit(0);
    a = mg.actions(s)
    print(mg.string(s))
    print(s)
    print(a)
    print("Is over: %s"%mg.is_over(s))
    print("Utility = %d"%mg.score(s))
    print("")

    s = mg.result(s, 2)
    a = mg.actions(s)
    print(mg.string(s))
    print(s)
    print(a)
    print("Is over: %s"%mg.is_over(s))
    print("Utility = %d"%mg.score(s))
    print("")

