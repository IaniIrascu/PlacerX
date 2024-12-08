import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic

# Load the data
df = pd.read_csv('bucuresti_principal.csv')
df2 = pd.read_csv('sectoare_cu_densitate.csv')

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
        K = range(2, min(10, len(coordinates) + 1))
        for k in K:
            kmeans = KMeans(n_clusters=k, random_state=0).fit(coordinates)
            inertia.append(kmeans.inertia_)
            if k > 1 and len(coordinates) > k:
                silhouette_scores.append(silhouette_score(coordinates, kmeans.labels_))
            else:
                silhouette_scores.append(-1)
        
        best_k = K[np.argmax(silhouette_scores[1:]) + 1]  # Find best k based on silhouette score

        # Fit the model with the best k value
        kmeans = KMeans(n_clusters=best_k, random_state=0).fit(coordinates)
        cluster_center = kmeans.cluster_centers_[0]  # Use the first cluster center for now

        midpoints.append({
            'Name': 'Potential Store',
            'Address': 'Potential Address',
            'Latitude': cluster_center[0],
            'Longitude': cluster_center[1],
        })

# Convert the list of midpoints to a DataFrame
midpoints_df = pd.DataFrame(midpoints, columns=['Name', 'Address', 'Latitude', 'Longitude'])

# Print the midpoints for the potential store locations
print(midpoints_df)

# Append the potential store locations to the original dataframe
df3 = pd.concat([df, midpoints_df], ignore_index=True)

# Save the midpoints DataFrame to a CSV file
midpoints_df.to_csv("midpoints.csv", index=False)
