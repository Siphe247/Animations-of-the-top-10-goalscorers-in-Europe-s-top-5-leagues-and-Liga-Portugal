import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie A/2024-25 Serie A cumulative goals.csv')

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
            imagebox = OffsetImage(badge_images[player], zoom=0.08)
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
    ax.set_title(f'Serie A 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
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
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Serie_A_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 
