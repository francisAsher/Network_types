import networkx as nx
import matplotlib.pyplot as plt

N = 1000
k = 4
p = 0.01

G = nx.watts_strogatz_graph(N, k, p)
plt.title("Small World Network")
nx.draw(G, node_size=10)

plt.show()

avg_path = nx.average_shortest_path_length(G)
print("Shortest path length: " , avg_path)

diameter = nx.diameter(G)
print("Diameter: " , diameter)

clustering = nx.average_clustering(G)
print("Clustering coefficient: " , clustering)

degree = [d for n, d in G.degree()]

plt.hist(degree)
plt.title("Degree Distribution of Small World Network")
plt.xlabel("Degree")
plt.ylabel("number of nodes")

plt.show()
