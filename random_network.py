import networkx as nx
import matplotlib.pyplot as plt

N = 1000
p = 0.01 #p is probability of people connecting = 1% (small probability because in real life people ain't connected to everyone)

G = nx.erdos_renyi_graph(N, p) #create the random graph with 1%p

plt.title("Random Network")
nx.draw(G, node_size=10)

plt.show()

avg_path = nx.average_shortest_path_length(G) #on the average how many steps to travel between two nodes
print("Shortest Path Length: ", avg_path)

diameter = nx.diameter(G) #distance between two furthest nodes
print("Diameter: ", diameter)

clustering = nx.average_clustering(G) #how much friend groups exist, how the network is linked
print("Clustering coefficient: ", clustering)

degree = [d for n, d in G.degree()] #degree distribution

plt.hist(degree)
plt.title("Degree Distribution of Random Network")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")

plt.show()

