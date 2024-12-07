import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from geopy.geocoders import GoogleV3

# Load the df
df = pd.read_csv('dataset.csv')

initial_count = sum(1 for entry in df['Name'] if entry == 'bp')
print(f"Initial count of 'bp': {initial_count}")

# Get the indices of all 'bp' entries
bp_indices = df[df['Name'] == 'bp'].index

# Calculate the number of entries to delete (half of the initial count)
num_to_delete = initial_count // 2

# Drop the calculated number of 'bp' entries
df = df.drop(bp_indices[:num_to_delete])

df['Random_Score'] = np.where(df['Name'] == 'Key Food Supermarkets', np.random.randint(-50, 150, len(df)), np.nan)
df.to_csv("stores.csv", index=False)


plt.scatter(df['Latitude'], df['Longitude'])
plt.xlabel('Latitude')
plt.ylabel('Longitude')
plt.xlim(40.55, 40.9)  # Set the limits for the x-axis (latitude)
plt.ylim(-74.2, -73.65)  # Set the limits for the y-axis (longitude)
# print(df['Name'].value_counts())
print(df['Random_Score'].describe())
plt.show()

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

