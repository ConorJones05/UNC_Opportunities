import pickle
import pandas as pd

df = pd.read_csv('/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/combined_data.csv')



classes_dictionary = {}

for index, row in df.iterrows():
    pre_list = []
    for key in row.keys():
        if key.startswith('Prereq_') and pd.notna(row[key]):
            pre_list.append(row[key])
    classes_dictionary[row['Course Code']] = pre_list

for key in classes_dictionary:
    if classes_dictionary[key] == []:
        classes_dictionary[key] = None




with open('my_dict.pkl', 'wb') as f:
    pickle.dump(classes_dictionary, f)