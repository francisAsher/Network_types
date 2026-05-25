import networkx as nx
import matplotlib.pyplot as plt

N = 1000
m = 3

G = nx.barabasi_albert_graph(N, m)
plt.title("Scale-Free Network")

nx.draw(G, node_size=10)

plt.show()

avg_path = nx.average_shortest_path_length(G)
print("Shortest path length :", avg_path)

diameter = nx.diameter(G)
print("Diameter :", diameter)

clustering = nx.average_clustering(G)
print("Clustering coefficient :", clustering)

degree = [d for n, d in G.degree()]

plt.hist(degree)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")

plt.show()