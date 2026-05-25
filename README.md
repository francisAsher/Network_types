# Network Analysis Results

| Network Type | Average Shortest Path Length | Diameter | Clustering coefficient |
|---|--|---|------------------------|
| Random Network | 3.25 | 5 |         0.01               |
| Small-World Network |27.59 | 76 |    0.49                    |
| Scale-Free Network | 3.52 | 6 |      0.27                  |
| Exponential Network | N/A | N/A |     0.002                |

# Project Overview

This project explores four network structures:

- Random Networks: connections are formed randomly between nodes.

- Small-World Networks: nodes mostly connect locally, with a few long-range connections.

- Scale-Free Networks: most nodes have few connections, while a small number of hubs have many connections. New nodes join the network with new connections. 

- Exponential Networks: node connectivity follows an exponential degree distribution with many low-degree nodes.


# Random Network

Graph Generator: nx.erdos_renyi_graph(N, p)

Parameters:

* N = Number of nodes (population size)
* p = Probability that any two nodes become connected

Description:
The random network connects nodes with probability p. Most nodes tend to have similar connectivity levels.

# Small-World Networks

Graph generator: nx.watts_strogatz_graph(N, k, p)

Parameters:

* N = Number of nodes (population size)
* k = Number of nearest neighbors each node initially connects to
* p = Rewiring probability that creates random long-range shortcuts

Description:
The small-world network models realistic social systems where individuals mostly interact locally, but a few random long-distance connections exist.

# Scale-Free Network

Graph generator: nx.barabasi_albert_graph(N, m)

Parameters:

* N = Number of nodes (population size)
* m = Number of connections each new node creates when entering the network

Description:
The scale-free network grows over time and produces highly connected hub nodes through preferential attachment.

# Exponential Network

Graph generator: nx.configuration_model(degrees)

Parameters:

* N = Number of nodes (population size)
* scale = Controls the exponential degree distribution and average connectivity
* degrees = Degree sequence generated from the exponential distribution

Description:
The exponential network generates node connections using an exponential degree distribution, producing many low-degree nodes and fewer highly connected nodes.

