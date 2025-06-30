import os
import pandas as pd
import numpy as np

#This code creates a DataFrame for Bundesliga's top 10 goalscorers and their goals scored in each gameweek.
goals={
"Harry Kane":[0,1,3,1,0,0,3,1,2,0,3,0,0,0,0,1,1,0,1,2,2,0,0,0,0,0,1,1,0,1,0,0,1,1],
"Patrik Schick":[0,0,0,0,0,0,0,0,0,1,3,1,0,0,4,2,0,1,1,1,0,0,1,1,0,1,0,0,0,1,1,0,0,2],
"Serhou Guirassy":[0,0,0,1,2,0,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,0,4,1,0,0,0,1,0,1,1,2,1,1],
"Jonathan Burkardt":[0,1,0,2,0,2,0,0,0,1,1,2,1,0,0,2,0,0,0,0,0,1,0,1,0,1,0,0,0,0,0,1,1,1],
"Tim Kleindienst":[1,1,0,0,0,1,2,1,0,0,1,1,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,0,0,0,0,1,0,0],
"Ermedin Demirovic":[1,0,2,1,0,1,0,0,0,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,1,1,0,3,0,0,0,0,1,1],
"Hugo Ekitike":[0,1,0,0,0,1,0,0,2,1,0,1,1,0,0,0,1,1,2,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0],
"Omar Marmoush":[0,1,2,1,2,2,1,0,1,1,0,2,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"Benjamin Sesko":[0,0,0,0,2,0,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0],
"Jamal Musiala":[1,0,1,1,0,0,0,1,0,1,0,1,2,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
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
df_cumulative.to_csv('2024-25 Bundesliga cumulative goals.csv')

data=pd.DataFrame(df_cumulative)

print(data)

data=df_cumulative.to_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/2024-25 Bundesliga cumulative goals.csv', index=True)