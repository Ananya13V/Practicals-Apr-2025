import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"SMA_codes\SMA 1-3 Dataset.csv")

location_count = df['Location'].value_counts()
print(location_count)

top_locations = location_count.head(10)

plt.figure(figsize=(10,6))
top_locations.plot(kind = 'bar', color = 'skyblue')
plt.title('Top 10 locations')
plt.xlabel('Location')
plt.ylabel('Frequency')
plt.show()