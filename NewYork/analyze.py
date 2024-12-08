import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from geopy.distance import geodesic
from scipy.spatial.distance import pdist, squareform

df = pd.read_csv('convenience_enhanced.csv')
df2 = pd.read_csv('datasets/district_and_location.csv')

print(df['Name'].value_counts())

# for lat, long in zip(df2['Latitude'], df2['Longitude']):
    
