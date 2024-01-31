from matplotlib import pyplot as plt
import pandas as pd

scatter_data = pd.read_csv('spotify_data_by_genres.csv')
plt.rcParams['figure.figsize'] = (5, 3)
plt.rcParams['figure.dpi'] = 75

plt.scatter(scatter_data.danceability, scatter_data.valence, alpha=.15, color='teal')

plt.title('Mood and Danceability correlation in Spotify genres')
plt.xlabel('Danceability')
plt.ylabel('Valence / Mood (sadder to happier)')
plt.show()

# Multiple scatter plots------------------------------------------------------------
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 75

plt.suptitle( 'Relationship between Popularity and ___')  # title above all the charts
plt.subplot(3, 4, 1)
plt.scatter(x=scatter_data.popularity, y=scatter_data.acousticness, alpha=.05)
plt.title('Acousticness')
plt.subplot(3, 4, 2)
plt.scatter(x=scatter_data.popularity, y=scatter_data.danceability, alpha=.05)
plt.title('danceability')
plt.subplot(3, 4, 3)
plt.scatter(x=scatter_data.popularity, y=scatter_data.duration_ms, alpha=.05)
plt.title('duration_ms')
plt.subplot(3, 4, 4)
plt.scatter(x=scatter_data.popularity, y=scatter_data.energy, alpha=.05)
plt.title('energy')
plt.subplot(3, 4, 5)
plt.scatter(x=scatter_data.popularity, y=scatter_data.instrumentalness, alpha=.05)
plt.title('instrumentalness')
plt.subplot(3, 4, 6)
plt.scatter(x=scatter_data.popularity, y=scatter_data.liveness, alpha=.05)
plt.title('liveness')
plt.subplot(3, 4, 7)
plt.scatter(x=scatter_data.popularity, y=scatter_data.loudness, alpha=.05)
plt.title('loudness')
plt.subplot(3, 4, 8)
plt.scatter(x=scatter_data.popularity, y=scatter_data.speechiness, alpha=.05)
plt.title('speechiness')
plt.subplot(3, 4, 9)
plt.scatter(x=scatter_data.popularity, y=scatter_data.tempo, alpha=.05)
plt.title('tempo')
plt.subplot(3, 4, 10)
plt.scatter(x=scatter_data.popularity, y=scatter_data.valence, alpha=.05)
plt.title('valence')
plt.subplot(3, 4, 11)
plt.scatter(x=scatter_data.popularity, y=scatter_data.key, alpha=.05)
plt.title('key')
plt.subplot(3, 4, 12)
plt.scatter(x=scatter_data.popularity, y=scatter_data.popularity, alpha=.05)
plt.title('popularity')

plt.subplots_adjust(hspace=0.5, wspace=0.3)
plt.show()