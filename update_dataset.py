
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

# plt.scatter(df['Latitude'], df['Longitude'])
# plt.xlabel('Latitude')
# plt.ylabel('Longitude')
# plt.xlim(40.55, 40.9)  # Set the limits for the x-axis (latitude)
# plt.ylim(-74.2, -73.65)  # Set the limits for the y-axis (longitude)
# print(df['Name'].value_counts())
# print(df['Random_Score'].describe())
# plt.show()