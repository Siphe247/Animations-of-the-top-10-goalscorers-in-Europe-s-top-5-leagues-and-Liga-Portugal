import pandas as pd
import os
import numpy as np

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

df=pd.DataFrame(goals)
df.index.name = "Gameweek"
print(df)

# Load your CSV
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/2024-25 La Liga cumulative goals.csv', index_col='Gameweek')
final_goals=df.iloc[-1].sort_values()

#Player colour mapping
player_colours={
"Kylian Mbappé": "#DCDCE3E6",
"Robert Lewandowski":"#150080",
"Ante Budimir": "#DB0808E6",
"Alexander Sørloth":"#EF0808",
"Ayoze Pérez": "#FFF204",
"Raphinha": "#150080",
"Julián Álvarez": "#EF0808",
"Oihan Sancet": "#B30707",
"Kike García": "#004EEA",
"Javi Puado": "#1936DB"
}

club_badges={
    "Kylian Mbappé":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Real Madrid_liga.png',
    "Robert Lewandowski":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Barcelona_liga.png',
    "Ante Budimir":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Osasuna_liga.png',
    "Alexander Sørloth":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Atletico_liga.png',
    "Ayoze Pérez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Villarreal_liga.png',
    "Raphinha":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Barcelona2_liga.png',
    "Julián Álvarez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Atletico2_liga.png',
    "Oihan Sancet":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Athletic_liga.png',
    "Kike García":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Alaves_liga.png',
    "Javi Puado":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga club badges/Espanyol_liga.png'
}

player_faces={
    "Kylian Mbappé":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Mbappe.png',
    "Robert Lewandowski":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Lewandowski.png',
    "Ante Budimir":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Budimir.png',
    "Alexander Sørloth":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Sørloth.png',
    "Ayoze Pérez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Pérez.png',
    "Raphinha":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Raphinha.png',
    "Julián Álvarez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Alvarez.png',
    "Oihan Sancet":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Sancet.png',
    "Kike García":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/García.png',
    "Javi Puado":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/La Liga top scorer images/Puado.png'
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
            imagebox = OffsetImage(badge_img, zoom=0.12)
            ab = AnnotationBbox(imagebox, (final_goals.min() -5, y), frameon=False, box_alignment=(1,0.5))
            ax.add_artist(ab)
        except Exception as e:
            print(f"Could not load badge for {player}: {e}")
    # Player face to the right
    if player in player_faces:
        try:
            face_img = mpimg.imread(player_faces[player])
            imagebox = OffsetImage(face_img, zoom=0.19)
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
badge_x = final_goals.min() - 13  # Adjust this value as needed for spacing

# Aesthetics
ax.set_xlabel('Total Goals', fontsize=14)
ax.set_ylabel('Player', fontsize=14)
ax.set_title('La Liga 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+5)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()
