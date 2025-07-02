import os
import pandas as pd
import numpy as np

goals={
    "Ousmane Dembélé":[1,0,0,2,1,0,0,0,0,1,0,0,0,0,1,2,2,0,1,3,2,0,1,1,2,1,0,0,0,0,0,0,0,0],
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

df = pd.DataFrame(goals)
df.index.name = "Gameweek"
print(df)

# Load your CSV
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/2024-25 Ligue 1 cumulative goals.csv', index_col='Gameweek')
final_goals=df.iloc[-1].sort_values()

#Player colour mapping
player_colours={
    'Ousmane Dembélé': '#1300B9',
    'Mason Greenwood': '#36FFFC',
    'Arnaud Kalimuendo': '#FA1010',
    'Jonathan David': '#FE1515',
    'Alexandre Lacazette': '#E4EEF7',
    'Bradley Barcola': '#1300B9',
    'Emanuel Emegha': '#2EB2CC',
    'Amine Gouiri': '#36FFFC',
    'Ludovic Ajorque': '#FF0000',
    'Mika Biereth': '#E10808',
}

club_badges={
    'Ousmane Dembélé': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/PSG_logo.png',
    'Mason Greenwood': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/OM_logo.png',
    'Arnaud Kalimuendo': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/Rennes_logo.png',
    'Jonathan David': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/Lille_logo.png',
    'Alexandre Lacazette': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/OL_logo.png',
    'Bradley Barcola': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/PSG2_logo.png',
    'Emanuel Emegha': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/Strasbourg_logo.png',
    'Amine Gouiri': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/OM2_logo.png',
    'Ludovic Ajorque': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/Brest_logo.png',
    'Mika Biereth': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/Monaco_logo.png'
}

player_faces={
    'Ousmane Dembélé': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Dembele_l1.png',
    'Mason Greenwood': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Greenwood_l1.png',
    'Arnaud Kalimuendo': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Kalimuendo_l1.png',
    'Jonathan David': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/David_l1.png',
    'Alexandre Lacazette': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Lacazette_l1.png',
    'Bradley Barcola': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Barcola_l1.png',
    'Emanuel Emegha': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Emegha_l1.png',
    'Amine Gouiri': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Gouiri_l1.png',
    'Ludovic Ajorque': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Ajorque_l1.png',
    'Mika Biereth': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Biereth_l1.png'
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
            imagebox = OffsetImage(badge_img, zoom=0.04)
            ab = AnnotationBbox(imagebox, (final_goals.min() -5, y), frameon=False, box_alignment=(1,0.5))
            ax.add_artist(ab)
        except Exception as e:
            print(f"Could not load badge for {player}: {e}")
    # Player face to the right
    if player in player_faces:
        try:
            face_img = mpimg.imread(player_faces[player])
            imagebox = OffsetImage(face_img, zoom=0.07)
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
ax.set_title('Ligue 1 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+5)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()
