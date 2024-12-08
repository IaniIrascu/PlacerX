from geopy.geocoders import GoogleV3
import pandas as pd

# Initialize the geolocator
geolocator = GoogleV3(api_key="AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4")  # Replace with your API key

# List of Paris arrondissements
arrondissements = [f"Arrondissement {i}, Paris, France" for i in range(1, 21)]

# Store the results
arrondissement_coordinates = []

# Geocode each arrondissement
for arrondissement in arrondissements:
    try:
        location = geolocator.geocode(arrondissement)
        if location:
            arrondissement_coordinates.append({
                'Arrondissement': arrondissement.split(',')[0],
                'Latitude': location.latitude,
                'Longitude': location.longitude
            })
        else:
            arrondissement_coordinates.append({
                'Arrondissement': arrondissement.split(',')[0],
                'Latitude': None,
                'Longitude': None
            })
    except Exception as e:
        print(f"Error geocoding {arrondissement}: {e}")
        arrondissement_coordinates.append({
            'Arrondissement': arrondissement.split(',')[0],
            'Latitude': None,
            'Longitude': None
        })

# Convert results to DataFrame
df = pd.DataFrame(arrondissement_coordinates)

# Save to a CSV
df.to_csv("paris_arrondissement_coordinates.csv", index=False)

# Print the DataFrame
print(df)
