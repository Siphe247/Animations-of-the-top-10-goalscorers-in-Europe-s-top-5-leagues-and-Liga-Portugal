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
    "Jørgen Strand-Larsen": [0,1,0,0,0,0,1,1,0,1,0,0,2,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,2,1,1,1,0,1,0,0,1,0]
}

df = pd.DataFrame(goals)
df.index.name = "Gameweek"
print(df)

# Load your CSV
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/2024-25 Premier League cumulative goals.csv', index_col='Gameweek')
final_goals=df.iloc[-1].sort_values()

# Player color mapping
player_colours = {
    'Ollie Watkins': '#670e36',
    'Bryan Mbeumo': '#e30613',
    'Yoane Wissa': '#e30613',
    'Cole Palmer': '#034694',
    'Mohamed Salah': '#c8102e',
    'Erling Haaland': '#6cabdd',
    'Alexander Isak': '#241f20',
    'Chris Wood': '#e53233',
    'Matheus Cunha': '#fdb913',
    'Jørgen Strand-Larsen': '#fdb913',
}

club_badges = {
    'Ollie Watkins': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/aston villa_logo.png',
    'Bryan Mbeumo': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/brentford_logo.png',
    'Yoane Wissa': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/brentford2_logo.png',
    'Cole Palmer': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/chelsea_logo.png',
    'Mohamed Salah': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/liverpool_logo.png',
    'Erling Haaland': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/manchester city_logo.png',
    'Alexander Isak': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/newcastle utd_logo.png',
    'Chris Wood': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/nottingham forest_logo.png',
    'Matheus Cunha': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/wolves_logo.png',
    'Jørgen Strand-Larsen': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/wolves2_logo.png'
}

player_faces = {
    'Matheus Cunha': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Cunha_pl.png',
    'Erling Haaland': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Haaland_pl.png',
    'Alexander Isak': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Isak_pl.png',
    'Bryan Mbeumo': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Mbeumo_pl.png',
    'Cole Palmer': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Palmer_pl.png',
    'Mohamed Salah': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Salah_pl.png',
    'Jørgen Strand-Larsen': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Strand Larsen_pl.png',
    'Ollie Watkins': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Watkins_pl.png',
    'Yoane Wissa': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Wissa_pl.png',
    'Chris Wood': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Wood_pl.png'
}

import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

fig, ax = plt.subplots(figsize=(14, 8))
bars = ax.barh(final_goals.index, final_goals.values, color=[player_colours.get(p, 'gray') for p in final_goals.index])

# Add club badge and player face
for i, player in enumerate(final_goals.index):
    y = i
    # Club badge to the left
    if player in club_badges:
        try:
            badge_img = mpimg.imread(club_badges[player])
            imagebox = OffsetImage(badge_img, zoom=0.07)
            ab = AnnotationBbox(imagebox, (final_goals.min() -5, y), frameon=False, box_alignment=(1,0.5))
            ax.add_artist(ab)
        except Exception as e:
            print(f"Could not load badge for {player}: {e}")
    # Player face to the right
    if player in player_faces:
        try:
            face_img = mpimg.imread(player_faces[player])
            imagebox = OffsetImage(face_img, zoom=0.08)
            ab = AnnotationBbox(imagebox, (final_goals[player]+0.7, y), frameon=False, box_alignment=(0.5,0.5))
            ax.add_artist(ab)
        except Exception as e:
            print(f"Could not load face for {player}: {e}")
    # Add text label for the goal count
    ax.text(final_goals[player]+2.3, y, f"{int(final_goals[player])}", va='center', fontsize=12, fontweight='bold')

# Set y-ticks and y-tick labels as usual
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)

# Find the minimum x-limit to position badges just left of the labels
badge_x = final_goals.min() - 5  # Adjust this value as needed for spacing

# Aesthetics
ax.set_xlabel('Total Goals', fontsize=14)
ax.set_ylabel('Player', fontsize=14)
ax.set_title('Premier League 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+7)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()

