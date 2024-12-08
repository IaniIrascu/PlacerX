import googlemaps
import pandas as pd
import numpy as np
import time

# Initialize Google Maps client
gmaps = googlemaps.Client(key='AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4')

# Define the bounding box for the area (min_lat, max_lat, min_lng, max_lng)
min_lat, max_lat = 40.5, 41
min_lng, max_lng = -74.2, -73.6

# Generate grid points (adjust step size for finer grids)
lat_points = np.arange(min_lat, max_lat, 0.05)  # Approx. 5 km steps
lng_points = np.arange(min_lng, max_lng, 0.05)
centers = [(lat, lng) for lat in lat_points for lng in lng_points]

radius = 5000  # Smaller radius for detailed searches
place_type = "supermarket"

# Data storage
data = []
unique_place_ids = set()

# Query the Google Maps API for each grid center
for center in centers:
    try:
        # Fetch initial results
        places_result = gmaps.places_nearby(location=center, radius=radius, type=place_type)

        # Process results and handle pagination
        while True:
            for place in places_result.get('results', []):
                if place['place_id'] not in unique_place_ids:
                    unique_place_ids.add(place['place_id'])
                    data.append({
                        'Name': place['name'],
                        'Address': place.get('vicinity', ''),
                        'Latitude': place['geometry']['location']['lat'],
                        'Longitude': place['geometry']['location']['lng'],
                    })

            # Check for next page
            next_page_token = places_result.get('next_page_token')
            if not next_page_token:
                break

            # Wait for the next page token to activate
            time.sleep(2)
            places_result = gmaps.places_nearby(page_token=next_page_token)

    except Exception as e:
        # Handle errors (e.g., API limits, network issues)
        continue

# Save final results to CSV
df = pd.DataFrame(data)
df.to_csv("supermarket_initial.csv", index=False)
