import pandas as pd
df = pd.read_csv('sectoare_cu_densitate.csv')
del df['Densitate']
del df['Venituri']
del df['Trafic']
df.to_csv('sectoare.csv', index  = False)