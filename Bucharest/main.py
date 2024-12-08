import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from geopy.geocoders import GoogleV3
from geopy.distance import geodesic
from scipy.spatial.distance import pdist, squareform

df = pd.read_csv('datasetaux.csv')

df2 = pd.read_csv('sectoare_cu_densitate.csv')
df3 = pd.read_csv('bucuresti_convenience.csv')

def within_radius(row, center, radius):
    store_point = (row['Latitude'], row['Longitude'])
    return geodesic(center, store_point).km <= radius
    

geolocator = GoogleV3(api_key="AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4")

midpoints = []

for lat, long in zip(df2['Latitude'], df2['Longitude']):
    center = (lat, long)
    radius = 5  # To be made variable

    df['Venituri'] = df['Venituri'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    stores_within_radius = df[df.apply(within_radius, center=center, radius=radius, axis=1)].copy()
    stores_within_radius['Income_norm'] = (df['Venituri'] - df['Venituri'].min()) / (df['Venituri'].max() - df['Venituri'].min())
    stores_within_radius['Density_norm'] = (df['Density'] - df['Density'].min()) / (df['Density'].max() - df['Density'].min())
    stores_within_radius['Traffic_norm'] = (df['Trafic'] - df['Trafic'].min()) / (df['Trafic'].max() - df['Trafic'].min())

    coord = stores_within_radius[['Latitude', 'Longitude']].values
    distance_matrix = squareform(pdist(coord, metric='euclidean'))
    mean_distances = distance_matrix.mean(axis=1)
    stores_within_radius['Distance_norm'] = (mean_distances - mean_distances.min()) / (mean_distances.max() - mean_distances.min())
    # Invert distance normalization

    # Calculate weighted score
    stores_within_radius['Weighted'] = (
        0.2 * stores_within_radius['Income_norm'] +
        0.3 * stores_within_radius['Density_norm'] +
        0.3 * stores_within_radius['Distance_norm'] +
        0.2 * stores_within_radius['Traffic_norm']
    )

    # Normalize Weighted_Score to sum to 1
    stores_within_radius['Weighted'] = stores_within_radius['Weighted'] / stores_within_radius['Weighted'].sum()

    # Check for non-zero weights
    non_zero_weights = stores_within_radius[stores_within_radius['Weighted'] > 0]
    if non_zero_weights.empty:
        continue

    # Adjust sample size if necessary
    sample_size = len(non_zero_weights)

    selected_store = non_zero_weights.sample(weights=non_zero_weights['Weighted'], n=sample_size, replace=True)
    
    # Select stores based on weights
    coordinates = selected_store[['Latitude', 'Longitude']]

    if not coordinates.empty:
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
        valid_scores = [score for score in silhouette_scores if score != -1]
        if valid_scores:
            best_k = K[np.argmax(valid_scores)]
        else:
            best_k = 2

        kmeans = KMeans(n_clusters=best_k, random_state=0).fit(coordinates)
        cluster_center = kmeans.cluster_centers_[0]
        
        same_stores_within_radius = df[(df['Name'].str.contains('La doi paşi')) & df.apply(within_radius, center=cluster_center, radius=0.5, axis=1)]
        # if is_on_water(cluster_center[0], cluster_center[1]) or not same_stores_within_radius.empty:
        #     continue
        if same_stores_within_radius.empty:
            location = geolocator.reverse((cluster_center[0], cluster_center[1]))
            address = location.address if location else 'Unknown Address'
            address_parts = address.split(", ")
            address = address_parts[0]
        
            df.add({
                'Name': 'La doi paşi',
                'Address': address,
                'Latitude': cluster_center[0],
                'Longitude': cluster_center[1],
                'Venituri': 0,
                'Density': 0,
                'Trafic': 0
            })
            midpoints.append(['La doi paşi', address, cluster_center[0], cluster_center[1]])

midpoints_df = pd.DataFrame(midpoints, columns=['Name', 'Address', 'Latitude', 'Longitude'])
midpoints_df.to_csv("midpoints3_convenience.csv", index=False)

df4 = pd.concat([df3, midpoints_df], ignore_index=True)
df4.to_csv("convenience_final.csv", index=False)