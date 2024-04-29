import networkx as nx
import matplotlib.pyplot as plt

# Create a sample graph
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (1, 4),(1, 5)])

# Compute the degree of each node
node_degrees = dict(G.degree())

# Set node sizes based on their degrees
node_sizes = [v * 100 for v in node_degrees.values()]  # Adjust multiplier for suitable scaling

# Draw the graph
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=node_sizes)

# Show the plot
plt.show()
print(node_degrees)