import pandas as pd

df = pd.read_csv("income.csv")
df['Income'] = df['Income'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df['Traffic'] = (df['Density'] / 1000) - (df['Income'] / 1000000)
df.to_csv("income_cu_traffic.csv", index=False)

