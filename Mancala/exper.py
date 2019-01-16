from minimax import *
from mancala import *
import pandas as pd
import numpy as np


def testMinimaxGame():
    max_depth = 5
    moves = 100
    verbose=True
    size_board = [(2,1), (3,1), (3,2), (4,2), (5,3), (6,4)]
    list_depth = []
    list_size = []
    list_count = []
    list_finalScore = []
    max_depth = [1,2,3,4,5,6,7,8]
    f = open('output4.txt','w')
    for i in max_depth:
        f.write(f'Depth is {i}\n')
        for size,count in size_board:
            mg = MancalaGame(size, count)
            list_depth.append(i)
            
            fs = play_minimax(mg, max_depth=i, moves=moves, verbose=False)
            df = pd.DataFrame({'Size': [fs] })
            list_size.append(size)
            list_count.append(count)
            list_finalScore.append(fs)
            
            f.write(f'Size of board Size: {size} Count: {count}\n')
            f.write(f'Final Score is: {fs}\n')
    pdData = pd.DataFrame(np.column_stack([list_depth, list_size, list_count,list_finalScore]), 
                               columns=['Depth', 'Size', 'Count','FinalScore'])
    writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')
    pdData.to_excel(writer, 'Sheet1')
    writer.save()
    
            

testMinimaxGame()




