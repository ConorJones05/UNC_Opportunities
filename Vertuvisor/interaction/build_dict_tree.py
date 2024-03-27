import pickle
import pandas as pd

df = pd.read_csv('/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder/Class_AAAD.csv')



classes_dictionary = {}

for index, row in df.iterrows():
    pre_list = []
    for key in row.keys():
        if key.startswith('Prereq_') and pd.notna(row[key]):
            pre_list.append(row[key])
    classes_dictionary[row['Course Code']] = pre_list
     


print(classes_dictionary)




#serialized_object = pickle.dumps(my_object)