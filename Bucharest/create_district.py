from geopy.geocoders import GoogleV3
import pandas as pd

# Initialize the geolocator
geolocator = GoogleV3(api_key="AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4")  # Replace with your API key

# List of Bucharest sectors
sectors = [
    "Sector 1, Bucharest, Romania",
    "Sector 2, Bucharest, Romania",
    "Sector 3, Bucharest, Romania",
    "Sector 4, Bucharest, Romania",
    "Sector 5, Bucharest, Romania",
    "Sector 6, Bucharest, Romania"
]

# Store the results
sector_coordinates = []

# Geocode each sector
for sector in sectors:
    try:
        location = geolocator.geocode(sector)
        if location:
            sector_coordinates.append({
                'Sector': sector.split(',')[0],
                'Latitude': location.latitude,
                'Longitude': location.longitude
            })
        else:
            sector_coordinates.append({
                'Sector': sector.split(',')[0],
                'Latitude': None,
                'Longitude': None
            })
    except Exception as e:
        print(f"Error geocoding {sector}: {e}")
        sector_coordinates.append({
            'Sector': sector.split(',')[0],
            'Latitude': None,
            'Longitude': None
        })

# Convert results to DataFrame
df = pd.DataFrame(sector_coordinates)

# Save to a CSV
df.to_csv("bucharest_sector_coordinates.csv", index=False)

# Print the DataFrame
print(df)
