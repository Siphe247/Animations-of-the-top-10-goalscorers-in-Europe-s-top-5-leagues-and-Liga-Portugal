import os
import pandas as pd
import numpy as np

#This code creates a DataFrame for Ligue 1 and their goals scored in each gameweek.
goals={
    "Ousmane Dembele":[1,0,0,2,1,0,0,0,0,1,0,0,0,0,1,2,2,0,1,3,2,0,1,1,2,1,0,0,0,0,0,0,0,0],
    "Mason Greenwood":[2,1,2,0,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,2,0,0,1,2],
    "Arnaud Kalimuendo":[0,0,0,1,1,1,0,0,0,0,0,0,3,0,0,1,1,0,0,0,1,0,1,1,0,0,2,0,1,0,0,1,2,0],
    "Jonathan David":[1,0,0,0,1,3,0,0,1,1,0,0,2,2,0,0,0,0,0,1,0,0,0,1,1,0,0,0,0,2,0,0,0,0],
    "Alexandre Lacazette":[0,0,0,0,0,0,0,1,0,0,1,0,3,0,0,0,0,0,0,1,0,1,0,2,0,1,0,1,1,0,1,0,0,2],
    "Bradley Barcola":[1,2,1,0,0,2,0,1,1,0,2,0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,0],
    "Emanuel Emegha":[0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,2,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,0,0],
    "Amine Gouiri":[1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,2,0,1,0,1,0,0,0,0,3,1,2,0],
    "Ludovic Ajorque":[0,0,1,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0,2,0,0,0,1,0],
    "Mika Biereth":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,3,0,3,0,3,0,1,1,0,0,0,1,0,0,0],
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
df_cumulative.to_csv('2024-25 Ligue 1 cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/2024-25 Ligue 1 cumulative goals.csv', index=True)
