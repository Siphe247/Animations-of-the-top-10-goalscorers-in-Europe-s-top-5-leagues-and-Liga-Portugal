import os 
import pandas as pd
import numpy as np

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

df = pd.DataFrame(goals)
df.index.name = "Gameweek"
print(df)

# Load your CSV
df = pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/2024-25 Bundesliga cumulative goals.csv', index_col='Gameweek')
final_goals=df.iloc[-1].sort_values()

player_colours={
    "Harry Kane": "#FF0000",
    "Patrik Schick": "#FF0A0A",
    "Serhou Guirassy": "#FFFB00",
    "Jonathan Burkardt": "#00FF00",
    "Tim Kleindienst": "#047D2A",
    "Ermedin Demirovic": "#FF0800",
    "Hugo Ekitike": "#000000A2",
    "Omar Marmoush": "#000000A2",
    "Benjamin Sesko": "#FF1212",
    "Jamal Musiala": "#FF0000"
}

club_badges={
    "Harry Kane":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Bayern_bu.png',
    "Patrik Schick":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Leverkusen_bu.png',
    "Serhou Guirassy":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/BVB_bu.png',
    "Jonathan Burkardt":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Mainz_bu.png',
    "Tim Kleindienst":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Gladbach_bu.png',
    "Ermedin Demirovic":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Stuttgart_bu.png',
    "Hugo Ekitike":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Frankfurt_bu.png',
    "Omar Marmoush":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Frankfurt2_bu.png',
    "Benjamin Sesko":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Leipzig_bu.png',
    "Jamal Musiala":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga club badges/Bayern2_bu.png'
}

player_faces={
    "Harry Kane":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Kane_bu.png',
    "Patrik Schick":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Schick_bu.png',
    "Serhou Guirassy":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Guirassy_bu.png',
    "Jonathan Burkardt":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Burkardt_bu.png',
    "Tim Kleindienst":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Kleindienst_bu.png',
    "Ermedin Demirovic":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Demirovic_bu.png',
    "Hugo Ekitike":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Ekitike_bu.png',
    "Omar Marmoush":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Marmoush_bu.png',
    "Benjamin Sesko":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Sesko_bu.png',
    "Jamal Musiala":'/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/Bundesliga top scorer images/Musiala_bu.png'
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
            imagebox = OffsetImage(face_img, zoom=0.1)
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
ax.set_title('Bundesliga 2024/25 Top Scorers', fontsize=14, weight='bold')
ax.set_xlim(final_goals.min()-5, final_goals.max()+5)
ax.set_yticks(range(len(final_goals.index)))
ax.set_yticklabels(final_goals.index, fontsize=13)
ax.tick_params(axis='y', which='both', direction='out', pad=28)
ax.grid(axis='x', linestyle='--', alpha=0.5)
plt.subplots_adjust(left=0.5, right=0.95, top=0.9, bottom=0.15)

#Add credits 
CREDIT_1="Data: World Fantasy Soccer" 
CREDIT_2="Viz: Siphe247"

plt.figtext(
    0.99, 0.01, f"{CREDIT_1}\n{CREDIT_2}", fontsize=9,
    color="#000000",
    ha="right"
)

plt.savefig('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga 2024-25 Top Scorers.png', dpi=300, bbox_inches='tight')
plt.tight_layout()
plt.show()
