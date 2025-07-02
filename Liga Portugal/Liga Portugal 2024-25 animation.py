import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation    

df=pd.read_csv('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/2024-25 Liga Portugal cumulative goals.csv')

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
    'Viktor Gyökeres': '#006E07',
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
    'Viktor Gyökeres': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal club badges/Sporting Lisbon_logo.png',
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
    'Viktor Gyökeres': '/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga Portugal/Liga Portugal Top scorer images/Viktor Gyokeres_lp.png',
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
    ax.set_title(f'Liga Portugal 2024/25 Top Scorers - Gameweek {df.iloc[frame]["Gameweek"]}', 
                fontsize=14, weight='bold')
    
    # Set consistent x-axis limits for all frames
    ax.set_xlim(0, max_goals + 7)
    ax.set_yticks(range(len(gameweek_data.index)))
    ax.set_yticklabels(gameweek_data.index, fontsize=13)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    return bars

# Create animation
ani = animation.FuncAnimation(fig, update, frames=len(df), interval=500, blit=False)

# Save as MP4 video
writer = animation.FFMpegWriter(fps=2, metadata=dict(artist='Me'), bitrate=1800)
ani.save('/Users/siphuvuyomngxunyeni/Downloads/Football Analytics/Liga_Portugal_2024-25_Top_Scorers.gif',
         writer='pillow')

plt.closefig() 