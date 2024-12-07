import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from geopy.geocoders import GoogleV3

df2 = pd.read_csv('data.csv')
geolocator = GoogleV3(api_key="AIzaSyBu8Jo9OrbW-7jjKUPFF38bsXoVZu-6tI4")

# Display the first few rows of the DataFrame
# Create an empty list to store the geocoded data
geocoded_data = []

# Geocode each address
for address in df2["Location"]:
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

for i, income in enumerate(df2['All Households']):
    geocoded_data[i]['Income'] = income

# Convert the list of dictionaries into a Pandas DataFrame
df2 = pd.DataFrame(geocoded_data)
# Save the DataFrame to a CSV file
df2.to_csv('district_and_location.csv', index=False)