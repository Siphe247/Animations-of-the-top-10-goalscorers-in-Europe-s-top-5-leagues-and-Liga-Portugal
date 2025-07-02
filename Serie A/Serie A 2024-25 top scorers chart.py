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

df = pd.DataFrame(goals)
df.index.name = "Gameweek"
print(df)

# Load your CSV
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/2024-25 Serie A cumulative goals.csv', index_col='Gameweek')
final_goals=df.iloc[-1].sort_values()

#Player colour mapping
player_colours={
    "Mateo Retegui": "#0429AFFF",
    "Moise Kean": "#9604C3E8",
    "Ademola Lookman": "#0429AFFF",
    "Riccardo Orsolini": "#030367FF",
    "Marcus Thuram":"#043AFFFF",
    "Romelu Lukaku":"#00B0F0FF",
    "Lautaro Martinez":"#043AFFFF",
    "Scott McTominay":"#00B0F0FF",
    "Lorenzo Lucca":"#747B91EC",
    "Artem Dovbyk":"#3E1A1AFF",
    }

club_badges={
    "Mateo Retegui":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Atalanta.png',
    "Moise Kean": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Fiorentina.png',
    "Ademola Lookman": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Atalanta2.png',
    "Riccardo Orsolini": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Bologna.png',
    "Marcus Thuram":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Inter.png',
    "Romelu Lukaku":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Napoli.png',
    "Lautaro Martinez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Inter2.png',
    "Scott McTominay":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Napoli2.png',
    "Lorenzo Lucca":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Udinese.png',
    "Artem Dovbyk":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A club badges/Roma.png',
}

player_faces={
    "Mateo Retegui":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Retegui.png',
    "Moise Kean": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Kean.png',
    "Ademola Lookman": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Lookman.png',
    "Riccardo Orsolini": '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Orsolini.png',
    "Marcus Thuram":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Thuram.png',
    "Romelu Lukaku":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Lukaku.png',
    "Lautaro Martinez":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Martinez.png',
    "Scott McTominay":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/McTominay.png',
    "Lorenzo Lucca":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Lucca.png',
    "Artem Dovbyk":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/Serie A top scorer images/Dovbyk.png' 
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
badge_x = final_goals.min() - 13  # Adjust this value as needed for spacing

# Aesthetics
ax.set_xlabel('Total Goals', fontsize=14)
ax.set_ylabel('Player', fontsize=14)
ax.set_title('Serie A 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+5)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)
plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()