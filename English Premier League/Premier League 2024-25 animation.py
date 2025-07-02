import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation    

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/2024-25 Premier League cumulative goals.csv')

print(df)

#Want to create a cumulative sum of goals scored by each player
cumulative_goals = df.cumsum()
cumulative_goals.index.name = "Gameweek"
print(cumulative_goals)

from PIL import Image
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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
    'Jorgen Strand-Larsen': '#fdb913',
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
    'Jorgen Strand-Larsen': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League club badges/wolves2_logo.png'
}

player_faces = {
    'Matheus Cunha': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Cunha_pl.png',
    'Erling Haaland': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Haaland_pl.png',
    'Alexander Isak': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Isak_pl.png',
    'Bryan Mbeumo': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Mbeumo_pl.png',
    'Cole Palmer': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Palmer_pl.png',
    'Mohamed Salah': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Salah_pl.png',
    'Jorgen Strand-Larsen': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Strand Larsen_pl.png',
    'Ollie Watkins': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Watkins_pl.png',
    'Yoane Wissa': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Wissa_pl.png',
    'Chris Wood': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier League/Premier League top scorer images/Wood_pl.png'
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

      

#Create figure and axis
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
            imagebox = OffsetImage(badge_images[player], zoom=0.07)
            ab = AnnotationBbox(imagebox, (gameweek_data.min() - 4, y), 
                               frameon=False, box_alignment=(0.5, 0.5))
            ax.add_artist(ab)
        
        # Add player face to the right
        if player in face_images and gameweek_data[player] > 0:
            imagebox = OffsetImage(face_images[player], zoom=0.08)
            ab = AnnotationBbox(imagebox, (gameweek_data[player] + 0.7, y), 
                               frameon=False, box_alignment=(0.5, 0.5))
            ax.add_artist(ab)
        
        # Add text label for the goal count
        if gameweek_data[player] > 0:
            ax.text(gameweek_data[player] + 2.3, y, f"{int(gameweek_data[player])}", 
                   va='center', fontsize=12, fontweight='bold')
    
    # Aesthetics
    ax.set_xlabel('Total Goals', fontsize=14)
    ax.set_ylabel('Player', fontsize=14)
    ax.set_title(f'Premier League 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
                fontsize=14, weight='bold')
    
    # Set consistent x-axis limits for all frames
    ax.set_xlim(0, max_goals + 7)
    ax.set_yticks(range(len(gameweek_data.index)))
    ax.set_yticklabels(gameweek_data.index, fontsize=13)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    return bars

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=500, blit=False)

# Save as GIF
writer = animation.FFMpegWriter(fps=2, metadata=dict(artist='Me'), bitrate=1800)
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Premier_League_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 
