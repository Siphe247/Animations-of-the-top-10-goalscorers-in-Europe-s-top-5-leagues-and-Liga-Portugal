import os
import pandas as pd
import numpy as np  

# This code creates a DataFrame for Liga Portugal players and their goals scored in each gameweek.
goals={
    "Viktor Gyökeres":[1,2,3,1,1,2,0,1,1,4,0,0,1,1,0,0,3,1,0,0,0,0,1,2,2,1,2,1,0,3,4,0,0,1],
    "Vangelis Pavlidis":[0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,1,2,0,1,1,1,0,1,3,1,2,1,0,0,1],
    "Samuel Aghehowa":[0,0,0,0,1,2,1,0,3,0,1,1,1,0,1,2,0,0,0,0,0,0,0,1,0,0,1,1,0,0,0,2,0,1],
    "Clayton":[1,0,0,1,0,1,0,0,0,1,1,1,0,1,0,2,0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0],
    "Kerem Akturkoglu":[0,0,0,0,1,0,1,3,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,2,0,0,0,1,0,1,0],
    "Yanis Begraoui":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,2,0,1,0,0,0,1,0,0,0,1,0,0,3],
    "Alejandro Marques":[1,0,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,1,0],
    "Ricardo Horta":[0,0,0,0,0,0,1,0,0,0,2,0,0,2,0,0,0,0,1,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0],
    "Rodrigo Mora":[0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,2,0,0,1,1],
    "Cassiano":[0,0,0,0,0,1,1,0,0,1,1,0,0,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0,1,0,0,0]
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
df_cumulative.to_csv('2024-25 Liga Portugal cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/2024-25 Liga Portugal cumulative goals.csv', index=True)