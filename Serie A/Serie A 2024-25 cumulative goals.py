import numpy as np
import os
import pandas as pd

#This code creates a DataFrame for Serie A's top 10 goalscorers and their goals scored in each gameweek.
goals={
    "Mateo Retegui":[2,1,0,1,0,0,3,1,2,0,1,0,1,0,0,0,0,0,0,1,1,2,0,4,0,1,0,1,0,0,0,1,0,1,0,0,1,0],
    "Moise Kean":[0,0,1,1,0,0,0,0,2,0,1,3,1,0,0,1,1,0,0,1,0,1,2,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1],
    "Ademola Lookman":[0,0,0,1,1,0,0,0,2,0,2,0,1,0,1,0,1,0,0,0,1,0,0,0,0,2,0,1,0,0,0,0,0,0,1,1,0,0],
    "Riccardo Orsolini":[1,0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,2,0,1,1,0,0,1,0,0,1,1,1],
    "Marcus Thuram":[2,0,2,0,0,0,3,0,0,0,0,0,2,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
    "Romelu Lukaku":[0,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1],
    "Lautaro Martinez":[0,0,0,0,0,2,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0],
    "Scott McTominay":[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,2,1,2,0,0,0,1],
    "Lorenzo Lucca":[0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    "Artem Dovbyk":[0,0,0,1,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,1,1,0,0,0,0,1,0,1,1,0,0,0,0,1,0,0,0]
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
df_cumulative.to_csv('2024-25 Serie A cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/2024-25 Serie A cumulative goals.csv', index=True)
