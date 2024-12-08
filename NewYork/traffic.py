import pandas as pd

df = pd.read_csv("./datasets/income.csv")
df['Income'] = df['Income'].replace({'\$': '', ',': ''}, regex=True).astype(float)
df['Traffic'] = 0.05 * df['Density'] * df['Income']
df.to_csv("./datasets/income_cu_traffic.csv", index=False)

