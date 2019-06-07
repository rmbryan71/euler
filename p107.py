import networkx as nx
import numpy as np

with open('p107_network.txt') as f:
    data = [[int(num) for num in line.split(',')] for line in f]
f.close()

a = np.matrix(data)
g = nx.from_numpy_matrix(a)
print(nx.info(g))
print(nx.is_weighted(g))
print(nx.density(g))
initial_weight = g.size(weight='weight')
print("initial weight", initial_weight)
minimum = nx.minimum_spanning_edges(g, weight='weight')

after = 0
for edge in minimum:
    after += (edge[2]['weight'])
print(initial_weight - after)