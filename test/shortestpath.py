import networkx as nx

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (1, 3)])

# Finding the shortest path
shortest_path = nx.shortest_path(G, source=1, target=4)

print("Shortest path:", shortest_path)
