import googlemaps
import pandas as pd
import time

# Initialize Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4')

# Define a list of origin-destination pairs for traffic analysis
zones = [
    ("Times Square, New York", "Central Park, New York"),
    ("Brooklyn, NY", "Manhattan, NY"),
    ("Queens, NY", "Bronx, NY"),
    ("Chinatown, NY", "Harlem, NY")
]

# Data storage for results
traffic_data = []

# Loop through each pair and get traffic data
for origin, destination in zones:
    # Request traffic data using Google Maps Directions API
    directions_result = gmaps.directions(
        origin,
        destination,
        departure_time='now',  # Get real-time traffic data
        traffic_model='best_guess'  # Model for traffic estimation
    )
    
    # Extract relevant data from the response
    for leg in directions_result[0]['legs']:
        traffic_data.append({
            'origin': origin,
            'destination': destination,
            'duration_in_traffic': leg['duration_in_traffic']['text'],
            'distance': leg['distance']['text']
        })
    
    # Adding a sleep to avoid exceeding API rate limits
    time.sleep(1)

# Convert the traffic data to a DataFrame
traffic_df = pd.DataFrame(traffic_data)

# Save the traffic data to a CSV file
traffic_df.to_csv('nyc_multiple_zones_traffic.csv', index=False)

print("Traffic data for multiple zones saved to 'nyc_multiple_zones_traffic.csv'")
