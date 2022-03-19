# Miscellaneous

```python
# random seeds
random.seed(123)
numpy.random.seed(123) # networkx uses numpy


G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 1), (2, 3, 1), (3, 4, 1), (1, 3, 1), (2, 4, 1)])
nx.draw(G)

shortest path length
# doc: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html#networkx.algorithms.shortest_paths.generic.shortest_path_length
print("shortest path length:")
print(nx.shortest_path_length(G, 1, 4))

maximum flow
# doc: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.maximum_flow.html
print("maximum flow config from 1 to 4:")
print(nx.algorithms.maximum_flow(G, 1, 4, capacity="weight"))

all paths but sorted by length
# doc: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.simple_paths.shortest_simple_paths.html#networkx.algorithms.simple_paths.shortest_simple_paths
print("all paths sorted by length:")
paths = nx.algorithms.shortest_simple_paths(G, 1, 4)
for path in paths:
    print(path)

all shortest paths 
# doc: https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.all_shortest_paths.html#networkx.algorithms.shortest_paths.generic.all_shortest_paths
print("all shortest paths:")
paths = nx.all_shortest_paths(G, 1, 4)
for path in paths:
    print(path)
    
# random graph
G = nx.erdos_renyi_graph(10, 0.5)

# hashing
nx.algorithms.graph_hashing.weisfeiler_lehman_graph_hash(G)

# copy
# G.copy() gives a deep copy
# nx.Graph(G) gives a shallow copy (see ref [4])
```

## Reference

\[1] [https://networkx.org/documentation/stable/reference/randomness.html](https://networkx.org/documentation/stable/reference/randomness.html)

\[2] [https://networkx.org/documentation/stable/reference/generated/networkx.generators.random\_graphs.erdos\_renyi\_graph.html](https://networkx.org/documentation/stable/reference/generated/networkx.generators.random\_graphs.erdos\_renyi\_graph.html)

\[3] [https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.graph\_hashing.weisfeiler\_lehman\_graph\_hash.html#networkx.algorithms.graph\_hashing.weisfeiler\_lehman\_graph\_hash](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.graph\_hashing.weisfeiler\_lehman\_graph\_hash.html#networkx.algorithms.graph\_hashing.weisfeiler\_lehman\_graph\_hash)

\[4] [https://stackoverflow.com/questions/39555831/how-do-i-copy-but-not-deepcopy-a-networkx-graph](https://stackoverflow.com/questions/39555831/how-do-i-copy-but-not-deepcopy-a-networkx-graph)

\[5] [https://stackoverflow.com/questions/53583341/k-shortest-paths-using-networkx-package-in-python](https://stackoverflow.com/questions/53583341/k-shortest-paths-using-networkx-package-in-python)
