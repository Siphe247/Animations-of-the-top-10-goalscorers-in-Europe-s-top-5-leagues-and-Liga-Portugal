import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La Liga/2024-25 La Liga cumulative goals.csv')

print(df)

#Want to create a cumulative sum of goals scored by each player
cumulative_goals = df.cumsum()
cumulative_goals.index.name = "Gameweek"
print(cumulative_goals)

from PIL import Image
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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
            imagebox = OffsetImage(badge_images[player], zoom=0.12)
            ab = AnnotationBbox(imagebox, (gameweek_data.min() - 4, y), 
                               frameon=False, box_alignment=(0.5, 0.5))
            ax.add_artist(ab)
        
        # Add player face to the right
        if player in face_images and gameweek_data[player] > 0:
            imagebox = OffsetImage(face_images[player], zoom=0.19)
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
    ax.set_title(f'La Liga 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
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
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/La_Liga_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 