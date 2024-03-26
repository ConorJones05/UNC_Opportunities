import pandas as pd

df = pd.read_csv('/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder/Class_AAAD.csv')

def nodes_builder(df):
    return df.iloc[:, 0]

# def connections(file):

# def layers(file):

print(nodes_builder(df))