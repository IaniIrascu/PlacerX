import pandas as pd
df = pd.read_csv('department_initial.csv')
print(df['Name'].value_counts())


