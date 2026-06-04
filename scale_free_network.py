import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N = 10000
m = 3

G = nx.barabasi_albert_graph(N, m)

# plt.title("Scale-Free Network")
# nx.draw(G, node_size=10)
#
# plt.show()

avg_path = nx.average_shortest_path_length(G)
print("Shortest path length :", avg_path)

diameter = nx.diameter(G)
print("Diameter :", diameter)

clustering = nx.average_clustering(G)
print("Clustering coefficient :", clustering)

avg_degree = np.mean([d for n, d in G.degree()])
print("Average Degree:", avg_degree)

degree = [d for n, d in G.degree()]

plt.hist(degree)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")

plt.show()