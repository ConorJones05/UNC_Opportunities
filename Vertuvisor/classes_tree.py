import csv
import networkx as nx
import matplotlib.pyplot as plt

def create_course_graph(csv_file):
    course_graph = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            course = row[0]
            prerequisites = row[1:]
            course_graph[course] = prerequisites
    return course_graph

def visualize_course_graph(course_graph):
    G = nx.DiGraph()
    for course, prerequisites in course_graph.items():
        for prerequisite in prerequisites:
            G.add_edge(prerequisite, course)

    # Use nx_agraph.graphviz_layout for hierarchical layout
    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog="dot")

    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")
    plt.title("Course Prerequisite Sugiyama Diagram")
    plt.show()

if __name__ == "__main__":
    csv_file = "ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder/Class_RELI.csv"  # Replace with your CSV file path
    course_graph = create_course_graph(csv_file)
    visualize_course_graph(course_graph)
