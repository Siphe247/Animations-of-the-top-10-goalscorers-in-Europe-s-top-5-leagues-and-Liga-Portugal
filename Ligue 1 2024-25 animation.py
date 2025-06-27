import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/2024-25 Ligue 1 cumulative goals.csv')

print(df)

#Want to create a cumulative sum of goals scored by each player
cumulative_goals = df.cumsum()
cumulative_goals.index.name = "Gameweek"
print(cumulative_goals)

from PIL import Image
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

#Player colour mapping
player_colours={
    'Ousmane Dembele': '#1300B9',
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
    'Ousmane Dembele': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 club badges/PSG_logo.png',
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
    'Ousmane Dembele': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue 1/Ligue 1 top scorers/Dembele_l1.png',
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

#Load badge and image faces
badge_images={}
face_images={}

for player in player_colours.keys():
   if player in club_badges:
      try:
        badge_images[player] = mpimg.imread(club_badges[player])
      except Exception as e:
        print(f"Error loading badge for {player}: {e}")
      try:
        face_images[player] = mpimg.imread(player_faces[player])
      except Exception as e:
        print(f"Error loading face for {player}: {e}")

fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(left=0.26)

#Get all players
players=[col for col in df.columns if col != 'Gameweek']
max_goals = df[players].max().max()

# Function to create the plot for each frame
def update(frame):
    ax.clear()
    
    # Get data for the current gameweek
    gameweek_data = df.iloc[frame][players].sort_values()
    
    # Create horizontal bars
    bars = ax.barh(gameweek_data.index, gameweek_data.values, 
                  color=[player_colours.get(p, 'gray') for p in gameweek_data.index])
    
    # Add club badge and player face
    for i, player in enumerate(gameweek_data.index):
        y = i
        
        # Club badge to the left
        if player in badge_images:
            imagebox = OffsetImage(badge_images[player], zoom=0.05)
            ab = AnnotationBbox(imagebox, (gameweek_data.min() - 4, y), 
                               frameon=False, box_alignment=(0.5, 0.5))
            ax.add_artist(ab)
        
        # Add player face to the right
        if player in face_images and gameweek_data[player] > 0:
            imagebox = OffsetImage(face_images[player], zoom=0.08)
            ab = AnnotationBbox(imagebox, (gameweek_data[player] + 1, y), 
                               frameon=False, box_alignment=(0.5, 0.5))
            ax.add_artist(ab)
        
        # Add text label for the goal count
        if gameweek_data[player] > 0:
            ax.text(gameweek_data[player] + 2.3, y, f"{int(gameweek_data[player])}", 
                   va='center', fontsize=12, fontweight='bold')
    
    # Aesthetics
    ax.set_xlabel('Total Goals', fontsize=14)
    ax.set_ylabel('Player', fontsize=14)
    ax.set_title(f'Ligue 1 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
                fontsize=14, weight='bold')
    
    # Set consistent x-axis limits for all frames
    ax.set_xlim(0, max_goals + 7)
    ax.set_yticks(range(len(gameweek_data.index)))
    ax.set_yticklabels(gameweek_data.index, fontsize=13)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    return bars

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=500, blit=False)

# Save as GIF video
writer = animation.FFMpegWriter(fps=2, metadata=dict(artist='Me'), bitrate=1800)
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Ligue_1_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 
