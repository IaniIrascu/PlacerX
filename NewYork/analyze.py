import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic
from scipy.spatial.distance import pdist, squareform

df = pd.read_csv('supermarket_enhanced.csv')
df2 = pd.read_csv('district_and_location.csv')

for lat, long in zip(df2['Latitude'], df2['Longitude']):
    center = (lat, long)
    coord = df[['Latitude', 'Longitude']].values
    distance_matrix = squareform(pdist(coord, metric='euclidean'))
    print(distance_matrix)
    mean_distances = distance_matrix.mean(axis=1)
    # print(mean_distances)
    #df['Distance_norm'] = (mean_distances - mean_distances.min()) / (mean_distances.max() - mean_distances.min())

# print(df['Distance_norm'].sort_values(ascending=True))

