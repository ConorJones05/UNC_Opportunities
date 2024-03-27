import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from cleaning_raw_massive import nodes_builder, connections, layers 

df = pd.read_csv('/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder/Class_BIOL.csv')

def make_tree(df):
    G = nx.DiGraph()

    # Add nodes
    G.add_nodes_from(nodes_builder(df))

    # Add edges
    edges = connections(df) #connections
    G.add_edges_from(edges)

    # Draw the graph with layers
    layers = layers(df)  # layers
    pos = {}
    y = 3  # Initial y position for the first layer
    for layer in layers:
        x = 0  # Initial x position for the nodes in the current layer
        for node in layer:
            pos[node] = (x, -y)  # Assign position to the node
            x += 1  # Increment x position for the next node in the layer
        y += 1  # Increment y position for the next layer

    nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=3, arrows=True)  # Decrease font_size to make labels smaller
    plt.show()
