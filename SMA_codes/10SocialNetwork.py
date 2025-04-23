import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.community import girvan_newman
from sklearn.cluster import KMeans
import numpy as np

df = pd.read_csv(r"SMA_codes\sma_ques10_dataset.csv")
G = nx.Graph()
G.add_edges_from(zip(df["source"], df["target"]))

communities = girvan_newman(G)
top_level_communities = next(communities)

colors = ['red', 'blue', 'green', 'yellow', 'purple']
color_map = {}

for i, community in enumerate(top_level_communities):
    for node in community:
        color_map[node] = colors[i%len(colors)]

node_colors = [color_map.get(node, 'gray') for node in G.nodes()]
plt.figure(figsize=(10, 6))
nx.draw(G, with_labels = True, node_color=node_colors, node_size=500)
plt.title("Social Network Graph with Communities")
plt.show()

### Kmeans Clustering on Centrality Features

degree_contrality = nx.degree_centrality(G)
betweeness_centrality = nx.betweenness_centrality(G)

features = []
nodes = list(G.nodes())
for node in nodes:
    features.append([degree_contrality[node],betweeness_centrality[node]])

features = np.array(features)

kmeans = KMeans(n_clusters=3, random_state=0)
labels = kmeans.fit_predict(features)

# Plot KMeans clustering
plt.figure(figsize=(8, 5))
plt.scatter(features[:, 0], features[:, 1], c=labels, s=100)
# for i, node in enumerate(nodes):
#     plt.text(features[i, 0], features[i, 1], node, fontsize=9, ha="right")
plt.xlabel("Degree Centrality")
plt.ylabel("Betweenness Centrality")
plt.title("KMeans Clustering of Nodes Based on Centrality")
plt.show()

sorted_nodes = sorted(betweeness_centrality.items(), key=lambda x: x[1], reverse=True)
print("\nTop Influential Nodes (by Betweenness Centrality):")
for node, score in sorted_nodes[:5]:
    print(f"{node}: {score:.4f}")
