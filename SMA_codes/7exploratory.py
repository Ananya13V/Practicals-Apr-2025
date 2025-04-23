import pandas as pd 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

df = pd.read_csv(r"SMA_codes/SMA 1-3 Dataset.csv")

plt.figure(figsize=(10,5))
sns.barplot(data = df, x = 'Content_Type', y = 'Likes', estimator = 'sum', hue = 'Content_Type')
plt.title("Total Likes by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Total Likes")
plt.show()

plt.figure(figsize=(10,5))
sns.scatterplot(data = df, x = 'Comments', y = 'Likes', hue = 'Content_Type', s = 100)
plt.title("Likes vs Comments by Content Type")
plt.xlabel("Comments")
plt.ylabel("Likes")
plt.legend(title = 'Content Type')
plt.show()

plt.figure(figsize=(10,5))
plt.scatter(df['Shares'], df['Likes'], s = df['Followers']/10, alpha = 0.6, c = 'teal', edgecolors = 'w')
plt.title("Likes vs Shares by Followers")
plt.xlabel("Shares")
plt.ylabel("Likes")
plt.show()

plt.figure(figsize=(10,5))
sns.heatmap(df[['Likes', 'Comments', 'Shares', 'Followers']].corr(), annot = True, cmap = 'coolwarm')
plt.title("Correlation Heatmap")
plt.show()

#### Network Graph: Hashtag using Co-occurence
df['Hashtags'] = df['Hashtags'].astype(str)
df['HashtagsList'] = df['Hashtags'].apply(lambda x: [h.strip() for h in x.split()])

edges = []
for tags in df['HashtagsList']:
    for i in range(len(tags)):
        for j in range(i+1, len(tags)):
            edges.append((tags[i], tags[j]))

G = nx.Graph()
G.add_edges_from(edges)
plt.figure(figsize=(12, 8))
nx.draw(G, with_labels=True, node_color = 'lightcoral', edge_color = 'gray', node_size=1000, font_size=10)
plt.title('Hashtag Co-Occurence Network')
plt.show()

### WordCloud ###
hashtags = ' '.join(df['Hashtags'].astype(str).tolist())

wordcloud = WordCloud(width = 800, height = 400, background_color = 'white', colormap = 'viridis').generate(hashtags)


plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Hashtag WordCloud')
plt.show()
