import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga/2024-25 Bundesliga cumulative goals.csv')

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
    ax.set_title(f'Bundesliga 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
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
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Bundesliga_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 