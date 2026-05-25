import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = 1000 #number of node(total number of people)

#generating exponential degree sequence
degrees =  np.random.exponential(scale =  2, size=n) #scale is 2;more people are less connected
degrees = degrees.astype(int) #want only integers and not decimals

if sum(degrees) % 2 != 0:   #sum of degrees to be even cuz every degrees have two nodes
    degrees[0] += 1        #add one to it incase the random number generated is odd

#we don't have a built network generator for exponential networks
#expoential network usually refers to the degree distribution (exponential network means, the degree follows an exponential distribution)
#we can build one by generating exponential degrees
#Build the network
G = nx.configuration_model(degrees)
plt.title("Exponential Degree Distribution")

G = nx.Graph(G) #removes duplicate connections
G.remove_edges_from(nx.selfloop_edges(G))  #removes cases like nodes connected to itself

nx.draw(G, node_size = 50)

plt.show()

if nx.is_connected(G):

    avg_path = nx.average_shortest_path_length(G)
    print("Shortest path length:", avg_path)

    diameter = nx.diameter(G)
    print("Diameter:", diameter)

else:
    print("Graph is not connected")

clustering = nx.average_clustering(G)
print("Clustering coefficient:", clustering)

degree = [d for n, d in G.degree()]

plt.hist(degree)
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Number of Nodes")

plt.show()

