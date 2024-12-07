import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from geopy.geocoders import GoogleV3

df = pd.read_csv('data.csv')
geolocator = GoogleV3(api_key="AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4")

# Display the first few rows of the DataFrame
# Create an empty list to store the geocoded data
geocoded_data = []

# Geocode each address
for address in df["Location"]:
    address = address[:-5]
    aux_address = address + ", New York City"
    location = geolocator.geocode(aux_address)
    if location:
        # Append the data to the list
        geocoded_data.append({
            'Address': address,
            'Latitude': location.latitude,
            'Longitude': location.longitude
        })
    else:
        # Append the data with None if the address is not found
        geocoded_data.append({
            'Address': address,
            'Latitude': None,
            'Longitude': None
        })

for i, income in enumerate(df['All Households']):
    geocoded_data[i]['Income'] = income

print(df["All Households"])
# Convert the list of dictionaries into a Pandas DataFrame
df = pd.DataFrame(geocoded_data)

# Save the DataFrame to a CSV file
df.to_csv('district_and_location.csv', index=False)

# Print the DataFrame to verify
print(df)


