import os
import pandas as pd
import numpy as np  

# This code creates a DataFrame for Liga Portugal players and their goals scored in each gameweek.
goals={
    "Viktor Gyokeres":[1,2,3,1,1,2,0,1,1,4,0,0,1,1,0,0,3,1,0,0,0,0,1,2,2,1,2,1,0,3,4,0,0,1],
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

#Load the CSV
df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/2024-25 Liga Portugal cumulative goals.csv', index_col='Gameweek')
final_goals = df.iloc[-1].sort_values()

#Player colour mapping
player_colours={
    'Viktor Gyokeres': '#006E07',
    'Vangelis Pavlidis': '#DA0202',
    'Samuel Aghehowa': '#0B0BE4',
    'Clayton': '#00870B',
    'Kerem Akturkoglu': '#DA0202',
    'Yanis Begraoui': '#FFE500',
    'Alejandro Marques': '#FFE500',
    'Ricardo Horta': '#FF0800',
    'Rodrigo Mora': '#0B0BE4',
    'Cassiano': '#000000'
}

club_badges={
    'Viktor Gyokeres': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Sporting Lisbon_logo.png',
    'Vangelis Pavlidis': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/SL Benfica_logo.png',
    'Samuel Aghehowa': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/FC Porto_logo.png',
    'Clayton': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Rio Ave_logo.png',
    'Kerem Akturkoglu': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/SL Benfica_logo2.png',
    'Yanis Begraoui':'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Estoril_logo.png',
    'Alejandro Marques': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Estoril_logo2.png',
    'Ricardo Horta': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/SC Braga_logo.png',
    'Rodrigo Mora': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/FC Porto2_logo.png',
    'Cassiano': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Casa Pia_logo.png'
}

player_faces={
    'Viktor Gyokeres': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Viktor Gyokeres_lp.png',
    'Vangelis Pavlidis': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Vangelis Pavlidis_lp.png',
    'Samuel Aghehowa': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Samuel Aghehowa_lp.png',
    'Clayton': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Clayton_lp.png',
    'Kerem Akturkoglu': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Kerem Akturkoglu_lp.png',
    'Yanis Begraoui': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Yanis Begraoui_lp.png',
    'Alejandro Marques': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Alejandro Marques_lp.png',
    'Ricardo Horta': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Ricardo Horta_lp.png',
    'Rodrigo Mora': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Rodrigo Mora_lp.png',     
    'Cassiano': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Cassiano_lp.png'   
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
ax.set_title('Liga Portugal 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+7)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()

plt.show()