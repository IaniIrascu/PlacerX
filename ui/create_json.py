import csv
import json
import os

# List of input directories to process
input_dirs = ['../Bucharest', '../NewYork']  # Add your directories here

# Base output directory
base_output_dir = 'geojson_files'

# Create base output directory if it doesn't exist
os.makedirs(base_output_dir, exist_ok=True)

for input_dir in input_dirs:
    if not os.path.isdir(input_dir):
        print(f"Directory '{input_dir}' does not exist. Skipping.")
        continue
    
    # Extract city name from input_dir (e.g., '../Bucuresti' -> 'Bucuresti')
    city_name = os.path.basename(os.path.normpath(input_dir))
    
    # Define output directory for the current input directory
    output_dir = os.path.join(base_output_dir, city_name)
    os.makedirs(output_dir, exist_ok=True)
    
    # Iterate over all CSV files in the current input directory
    for filename in os.listdir(input_dir):
        if filename.endswith('.csv'):
            csv_path = os.path.join(input_dir, filename)
            features = []
            with open(csv_path, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    try:
                        latitude = float(row['Latitude'])
                        longitude = float(row['Longitude'])
                        store_name = row.get('Name', 'No Name')
                        address = row.get('Address', 'No Address')
                        # Extract store type from filename (e.g., 'grocery.csv' -> 'grocery')
                        store_type = os.path.splitext(filename)[0].replace(' ', '_')
                        
                        feature = {
                            "type": "Feature",
                            "properties": {
                                "Name": store_name,
                                "Address": address,
                                "StoreType": store_type.replace('_', ' ').title()
                                # Add other properties if needed
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [longitude, latitude]
                            }
                        }
                        features.append(feature)
                    except (ValueError, KeyError) as e:
                        # Skip rows with invalid or missing data
                        print(f"Skipping row due to error: {e}")
                        continue

            geojson = {
                "type": "FeatureCollection",
                "features": features
            }

            # Create JavaScript variable name based on city and store type
            variable_city = city_name.replace(' ', '').replace('-', '')
            variable_store = os.path.splitext(filename)[0].replace(' ', '_').replace('-', '').lower()
            variable_name = f"json_{variable_city}_{variable_store}"
            
            js_content = f"var {variable_name} = {json.dumps(geojson, indent=4)};"

            # Write to .js file in the output directory
            output_filename = f"{store_type}.js"
            output_path = os.path.join(output_dir, output_filename)
            with open(output_path, 'w', encoding='utf-8') as jsfile:
                jsfile.write(js_content)

            print(f"Created {output_path} with variable '{variable_name}'")