import networkx as nx
import matplotlib.pyplot as plt

# Creating a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 1)])

# Graph visualization
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
