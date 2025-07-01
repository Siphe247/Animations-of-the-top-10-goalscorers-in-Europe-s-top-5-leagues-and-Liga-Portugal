import pandas as pd
import os
import numpy as np

#This code creates a DataFrame for La Liga's top 10 goalscoers and their goals scored in each gameweek
goals={
"Kylian Mbappé":[0,0,0,2,1,1,1,0,0,1,0,0,1,1,0,1,0,1,0,2,3,0,1,1,0,0,1,2,2,0,0,0,0,2,3,1,1,2],
"Robert Lewandowski":[2,1,0,1,0,2,1,0,3,2,2,0,0,1,0,0,1,0,0,0,1,1,1,1,0,1,1,1,2,0,0,0,0,0,0,0,0,2],
"Ante Budimir":[0,0,0,0,0,1,0,2,1,0,1,1,0,2,1,1,0,0,0,0,0,2,0,1,0,1,1,0,0,0,1,2,0,0,1,1,1,0],
"Alexander Sørloth":[1,0,0,0,0,0,0,0,0,2,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,1,0,1,0,4,0,0,3],
"Ayoze Pérez":[0,1,0,1,1,1,2,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,1,0,1,1,0,0,2,0,2,1,0],
"Raphinha":[0,0,0,3,0,2,0,0,0,0,1,1,0,1,1,2,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,2,0,1,2,0,0,0],
"Julián Álvarez":[0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,2,1,0,1,0,1,2,0,1,0,0,0,2,0],
"Oihan Sancet":[1,1,0,0,1,0,0,0,1,0,0,0,0,1,2,0,0,0,0,0,0,1,3,1,1,0,0,0,0,0,2,0,0,0,0,0,0,0],
"Kike García":[1,0,0,0,0,0,1,0,0,1,0,0,0,0,0,2,0,0,0,3,1,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0],
"Javi Puado":[0,0,0,0,3,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,1]
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
df_cumulative.to_csv('2024-25 La Liga cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/2024-25 La Liga cumulative goals.csv', index=True)

