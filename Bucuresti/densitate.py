import pandas as pd

Area = [68, 38, 34, 34, 32, 30]
Population = [385.439, 367.760, 345.370, 287.828, 271.575, 225.454]
Densitate = [p / a for p, a in zip(Population, Area)]

Venituri = [3500, 2800, 3000, 2500, 2700, 2400]

df = pd.read_csv('sectoare.csv')
df['Densitate'] = Densitate
df['Venituri'] = Venituri
df['Trafic'] = ((df['Densitate'] / 100) - (df['Venituri'] / 100000))
df.to_csv("sectoare_cu_densitate.csv", index = False)