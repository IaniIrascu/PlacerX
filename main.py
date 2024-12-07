import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

# Load the df
df = pd.read_csv('dataset.csv')
df2 = pd.read_csv('district_and_location.csv')

def within_radius(row, center, radius):
        store_point = (row['Latitude'], row['Longitude'])
        return geodesic(center, store_point).km <= radius

midpoints = []

for lat, long in zip(df2['Latitude'], df2['Longitude']):
    center = (lat, long)  # Center point coordinates
    radius = 5  # Radius in kilometers

    stores_within_radius = df[df.apply(within_radius, center=center, radius=radius, axis=1)]

    # Calculate the midpoint coordinates of all stores within the radius
    coordinates = stores_within_radius[['Latitude', 'Longitude']]
    if not coordinates.empty:
        # Determine the best number of clusters using the Elbow Method
        inertia = []
        silhouette_scores = []
        K = range(2, min(10, len(coordinates)))
        for k in K:
            kmeans = KMeans(n_clusters=k, random_state=0).fit(coordinates)
            inertia.append(kmeans.inertia_)
            if k > 1 and len(coordinates) > k:
                silhouette_scores.append(silhouette_score(coordinates, kmeans.labels_))
            else:
                silhouette_scores.append(-1)
        best_k = K[np.argmax(silhouette_scores[1:]) + 1]

        kmeans = KMeans(n_clusters=best_k, random_state=0).fit(coordinates)
        cluster_center = kmeans.cluster_centers_[0]

        midpoints.append({
            'Name': 'Potential Store',
            'Address': 'Potential Address',
            'Latitude': cluster_center[0],
            'Longitude': cluster_center[1],
            'Rating': 0,
            'User Ratings Total': 0  # Replace with actual column names and default values
        })

midpoints_df = pd.DataFrame(midpoints, columns=['Name', 'Adresss', 'Latitude', 'Longitude', 'Rating', 'User Ratings Total'])

print(midpoints_df)

df3 = pd.concat([df, midpoints_df], ignore_index=True)
midpoints_df.to_csv("midpoints.csv", index=False)