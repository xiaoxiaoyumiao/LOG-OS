# Basics

```python
import networkx as nx
G = nx.Graph() # undirected graph
G = nx.DiGraph() # directed graph
G = nx.MultiGraph() # graph that allows multiple undirected edges between a node pair
G = nx.MultiDiGraph() # graph that allows multiple directed edges between a node pair

# A node of a graph can be any hashable object (with __hash__() and __eq__() implemented properly).
#   In fact, the graph object itself can be a node of other graphs.
# An edge of a graph can have arbitrary attributes.
# Graph is maintained as an adjacency list, that is, { node: {adjacent_node: edge} }

# Some special graphs
nx.complete_graph(10) # complete graph with 10 nodes.
nx.cycle_graph(10) # a cycle with 10 nodes. A chain with two ends joined.
nx.path_graph(10) # a chain structure with 10 nodes.
nx.trivial_graph() # a graph with one node.
nx.null_graph() # an empty graph

# Construct graph from edge list
# Edges will be introduced in detail below
edgelist = [(0, 1), (1, 2), (2, 3)]
H = nx.Graph(edgelist)
```

## Nodes

```python
G = nx.Graph() # undirected graph

# Adding nodes
G.add_node(1)

# Adding multiple nodes from iterable object
# The parameter can also be a graph, since graph is iterable
G.add_nodes_from([2, 3])
for node in G:
    print(node)

# Get node count
print(G.number_of_nodes())

# Adding nodes with attributes
G.add_nodes_from([
    (4, {"color": "red"}),
    (5, {"color": "green"}),
])

# Remove node
G.remove_node(4)
# Remove multiple nodes
G.remove_nodes_from([2, 3, 5])

G.nodes[1] # access node attribute by its ID (after nx 2.4)
```

## Edges

```python
G = nx.Graph() # undirected graph

# Adding edges
G.add_edge(1, 2) # add an edge between node 1 and 2; default edge data=1
G.add_edge(2, 3, weight=0.9) # specify edge data
for edge in G.edges:
    print(edge)

# Get edge count
print(G.number_of_edges())

# Adding multiple edges. Existing edges will be overwritten
elist = [(1, 2), (2, 3), (1, 4), (4, 2)]
G.add_edges_from(elist)

elist = [('a', 'b', 5.0), ('b', 'c', 3.0), ('a', 'c', 1.0), ('c', 'd', 7.3)]
G.add_weighted_edges_from(elist)

# Remove edge
G.remove_edge(1, 2)
# Remove multiple edges. (Seems like there's no error report when deleting non-existent edge)
G.remove_edges_from([(2, 3), (1, 4), (1, 'w')])

# Access adjacency list
G = nx.path_graph(3)
for node in G: 
    print(G.adj[node])
    print(G.degree[node])
print(list(G.adjacency()))
print(G.adj.items())

# Manipulate edge data by indexing
G[1][2]["data"] = "hello world"
print(G[1][2])
print(G.edges[1, 2])

# set attribute for all edges
nx.set_edge_attributes(G, 1, "weights")
```

## Drawing

```python
# Drawing

G = nx.complete_graph(5)
nx.draw(G)
```

## Reference

\[1] [https://stackoverflow.com/questions/13698352/storing-and-accessing-node-attributes-python-networkx](https://stackoverflow.com/questions/13698352/storing-and-accessing-node-attributes-python-networkx)

\[2] [https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.set\_edge\_attributes.html](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.set\_edge\_attributes.html)

\[3] [https://stackoverflow.com/questions/26691442/how-do-i-add-a-new-attribute-to-an-edge-in-networkx](https://stackoverflow.com/questions/26691442/how-do-i-add-a-new-attribute-to-an-edge-in-networkx)
