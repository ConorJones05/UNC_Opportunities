import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Add nodes
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G'])

# Add edges
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('E', 'A')]  # Example of adding multiple edges
G.add_edges_from(edges)

# Draw the graph with layers
layers = [['A'], ['B', 'C'], ['D', 'E'], ['F', 'G']]  # Define layers
pos = {}
y = 3  # Initial y position for the first layer
for layer in layers:
    x = 0  # Initial x position for the nodes in the current layer
    for node in layer:
        pos[node] = (x, -y)  # Assign position to the node
        x += 1  # Increment x position for the next node in the layer
    y += 1  # Increment y position for the next layer

nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=15, arrows=True)
plt.show()

# Optionally, export to Graphviz DOT format
nx.nx_agraph.write_dot(G, 'sugiyama_graph.dot')
