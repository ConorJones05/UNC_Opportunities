import pandas as pd
import re

def nodes_builder(file):
    data_list = []
    for i in range(len(file.columns)):
        data = file.iloc[:, i].values
        data_list.append(data)
    clean_row = [prereq for sublist in data_list for prereq in sublist if pd.notna(prereq)]
    return clean_row


def connections(file):
    file_without_nan = file.fillna('')
    arrays = []
    for index, row in file_without_nan.iterrows():
        array = [value for value in row if value != '']
        arrays.append(array)
    final_array = []
    for i in range(len(arrays)):
        for j in range(1, len(arrays[i])):
            # Append tuples with elements reversed
            final_array.append((arrays[i][j], arrays[i][0]))
    return final_array

def layers(file):
    level_0 = []
    level_100 = []
    level_200 = []
    level_300 = []
    level_400 = []
    level_500 = []
    level_600 = []
    level_700 = []
    level_800 = []
    level_900 = []

    for i in nodes_builder(file):
        numeric_values = re.findall(r'\d+', i)
        numeric_string = int(''.join(numeric_values))

        # Append to the appropriate level list based on numeric value
        if numeric_string < 100:
            level_0.append(i)
        elif numeric_string < 200:
            level_100.append(i)
        elif numeric_string < 300:
            level_200.append(i)
        elif numeric_string < 400:
            level_300.append(i)
        elif numeric_string < 500:
            level_400.append(i)
        elif numeric_string < 600:
            level_500.append(i)
        elif numeric_string < 700:
            level_600.append(i)
        elif numeric_string < 800:
            level_700.append(i)
        elif numeric_string < 900:
            level_800.append(i)
        else:
            level_900.append(i)
            
    # Return all level lists
    return level_0, level_100, level_200, level_300, level_400, level_500, level_600, level_700, level_800, level_900