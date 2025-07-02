import os
import pandas as pd
import numpy as np  

goals = {
    "Mohamed Salah": [1,1,1,0,0,1,0,1,1,1,1,2,1,2,0,2,1,1,1,0,0,1,2,1,1,1,1,0,2,0,0,0,0,1,0,0,0,1],
    "Alexander Isak": [0,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,3,1,1,1,2,0,2,0,0,2,0,0,1,0,0,1,0,1,1,0,0,0],
    "Erling Haaland": [1,3,3,2,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,2,0,1,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1],
    "Chris Wood": [1,0,1,0,1,0,1,1,2,1,0,0,1,0,1,0,0,0,1,1,1,1,0,3,1,0,0,0,0,0,0,0,1,0,0,1,0,0],
    "Bryan Mbeumo": [1,0,2,0,1,1,1,0,2,0,0,0,0,0,1,1,0,0,1,2,0,0,1,0,0,1,0,0,0,1,0,0,2,0,0,0,1,1],
    "Yoane Wissa": [1,0,1,1,0,0,0,0,1,0,2,0,1,0,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0],  
    "Ollie Watkins": [0,0,0,2,1,1,0,1,0,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0],
    "Matheus Cunha": [0,1,0,0,1,0,1,0,1,0,1,2,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0,1,0,0,0,0],
    "Cole Palmer": [0,1,0,0,1,4,0,0,1,0,0,0,1,1,2,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
    "Jorgen Strand-Larsen": [0,1,0,0,0,0,1,1,0,1,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,1,1,1,0,1,0,0,1,0]
}

def cumulative_goals(goals_dict):
     cumulative = {}
     for player, goals_list in goals_dict.items():
        cum_sum = []
        total = 0
        for g in goals_list:
            total += g
            cum_sum.append(total)
        cumulative[player] = cum_sum
     return cumulative

cumulative_data=cumulative_goals(goals)
df_cumulative = pd.DataFrame(cumulative_data)
df_cumulative.index=range(1, len(df_cumulative) + 1)
df_cumulative.index.name = "Gameweek"
df_cumulative.to_csv('2024-25 Premier League cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/2024-25 Premier League cumulative goals.csv', index=True)