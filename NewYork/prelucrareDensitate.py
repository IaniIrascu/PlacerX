import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("datasets/density.csv")

del df['CD Number']
del df['1970 Population']
del df['1980 Population']
del df['1990 Population']
del df['2000 Population']

dimensiune_cartier = {
    'Bronx': 42.2,
    'Brooklyn': 69.4,
    'Manhattan': 22.7,
    'Queens': 108.7,
    'Staten Island': 57.5
}

df['Populatie'] = df['2010 Population']

df['Area'] = df['Borough'].map(dimensiune_cartier)

df['Population Density'] = df['Populatie'] / df['Area'] * 6

df.to_csv('datasets/nyc_population_density_with_area.csv', index=False)
