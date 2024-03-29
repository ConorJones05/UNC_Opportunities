import pickle
import pandas as pd
from classes_tree import build_tree


with open('my_dict.pkl', 'rb') as f:
    classes = pickle.load(f)


Nodes = []
exit_flag = 0
while exit_flag < 1:
    search = input("What class would you like to search for: ")
    if search.upper() in classes:
        print(f"{search} has been found.")
    else:
        print(f"{search} is not in records.")

    Nodes.append(search)
    exit_input = input("Would you like to enter another class Y/N: ")
    if exit_input.upper() == "N":
        exit_flag += 1

additional_nodes = []
key_index = 0
iteration = 0

while iteration < 50 and key_index < len(Nodes):
    key = Nodes[key_index]
    if classes[key] is not None:
        for i in classes[key]:
            additional_nodes.append(i)
    key_index += 1
    iteration += 1
    Nodes.extend(additional_nodes)
    unique_items = set(Nodes)
    Nodes = list(unique_items)

biggest = 0
output = {"Nodes": Nodes}

biggest = 0
for j in Nodes:
    if classes[j] is not None:
        if len(classes[j]) > biggest:
            biggest = len(classes[j])

for column in range(biggest):
    output[f"Prereq{column+1}"] = []

for key in Nodes:
    if classes[key] is not None:
        for column, value in enumerate(classes[key]):
            output[f"Prereq{column+1}"].append(value)
    else:
        for column in range(biggest):
            output[f"Prereq{column+1}"].append(None)


df = pd.DataFrame(output)

build_tree(df)