import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

N = 1000
p = 0.01

G = nx.erdos_renyi_graph(N, p)

beta =  14/8 #infection rate
gamma = 1/8 #recovery rate

status = {} # Dictionary to store disease state of each person
for node in G.nodes():
    status[node] = 'S' # Initially everyone is susceptible

# Randomly choose one person to start the outbreak
initial_patient = np.random.choice(list(G.nodes()))

status[initial_patient] = 'I' # Infect the first individual

S_history = []   #List for storing  susceptible population over time
I_history = []   #List for storing  infected population over time
R_history = []   #List for storing  recovered population over time

# SIR SIMULATION
days = 100   # Number of simulation days
for t in range(days):
    # Create a copy so today's changes do not affect today's calculations
    new_status = status.copy()

    for node in G.nodes():     # Check every person in the network

        if status[node] == 'I': # Only infected people can spread disease

            for neighbor in G.neighbors(node):  # Check all nodes connected to the infected node

                if status[neighbor] == 'S':     # Only susceptible nodes can become infected

                    # Infection occurs with probability beta
                    if np.random.random() < beta:
                        new_status[neighbor] = 'I'

            # Recovery occurs with probability gamma
            if np.random.random() < gamma:
                new_status[node] = 'R'

    # End of the day: update population with new infections and recoveries
    status = new_status

    # Count number of susceptible, infected, and recovered individuals
    S_count = list(status.values()).count('S')
    I_count = list(status.values()).count('I')
    R_count = list(status.values()).count('R')

    # Save results for plotting
    S_history.append(S_count)
    I_history.append(I_count)
    R_history.append(R_count)

#testing if results were saved and working with first ten values for each
print(S_history[:10])
print(I_history[:10])
print(R_history[:10])

avg_degree = np.mean([d for n, d in G.degree()])
print("Average Degree:", avg_degree)

clustering = nx.average_clustering(G)
print("Clustering coefficient: ", clustering)

avg_path = nx.average_shortest_path_length(G)
print("Average Path Length:", avg_path)

diameter = nx.diameter(G)
print("Diameter:", diameter)

R0 = (beta / gamma) * avg_degree
print("Estimated R0:", R0)

#plot curve
plt.figure(figsize=(10,6))
plt.plot(S_history, label='Susceptible')
plt.plot(I_history, label='Infected')
plt.plot(R_history, label='Recovered')
plt.title('Random Network SIR Model')
plt.xlabel('Time in days')
plt.ylabel('Population')
plt.legend()
plt.grid()
plt.show()

