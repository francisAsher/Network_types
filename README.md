# Network Analysis Results

| Network Type | Network Size | Average Degree | Clustering Coefficient | Diameter | Average Shortest Path Length |
|---|--------------|----------------|------------------------|-----|------------------------------|
| Random Network | 10000        | 100.04         | 0.01                   | 3   | 2.3                          |
| Small-World Network | 10000        | 4.0            | 0.49                   | 113 | 48.35                        |
| Scale-Free Network | 10000        | 6.0            | 0.01                   | 7   | 4.2                          |
| Exponential Network | 10000        | 2.3            | 7.7e-0.5               | 24  | 9.9                          |

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

