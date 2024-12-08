import pandas as pd
df = pd.read_csv('bucuresti_convenience.csv')
#Mega Image
df['Name'] = df['Name'].str.replace(r'.*Mega image.*', 'Mega Image', case=False, regex=True)
df['Name'] = df['Name'].str.replace(r'.*Shop and.*', 'Mega Image', case=False, regex = True)
df['Name'] = df['Name'].str.replace(r'.*Shop &.*', 'Mega Image', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Carrefour.*', 'Carrefour', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Kaufland.*', 'Kaufland', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Penny.*', 'Penny', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Profi.*', 'Profi', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Domino.*', 'Domino', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*KFC.*', 'KFC', case=False, regex = True)
df['Name'] =  df['Name'].str.replace(r'.*Auchan.*', 'Auchan', case=False, regex = True)
df.to_csv('bucuresti_principal.csv', index=False)