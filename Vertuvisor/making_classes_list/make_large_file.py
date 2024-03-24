import os
import pandas as pd

def combine_csv_files(directory):
    # Initialize variables to store data and column names
    all_data = {}
    longest_file = None
    max_columns = 0

    # Read data from all CSV files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            try:
                df = pd.read_csv(file_path)
                num_columns = len(df.columns)
                if num_columns > max_columns:
                    max_columns = num_columns
                    longest_file = filename
                all_data[filename] = df
            except pd.errors.EmptyDataError:
                print(f"Skipping empty file: {filename}")

    if not all_data:
        print("No valid CSV files found in the directory.")
        return

    # Remove header (column names) from CSV files except the one with the longest header
    for filename, df in all_data.items():
        if filename != longest_file:
            if len(df) > 0:  # Check if DataFrame is not empty
                all_data[filename] = df.iloc[1:, :].reset_index(drop=True)  # Exclude the first row (header)

    # Concatenate data from all CSV files into a single DataFrame
    combined_df = pd.concat(all_data.values(), ignore_index=True)

    # Write the combined data to a new CSV file
    combined_file_path = os.path.join(directory, 'combined_data.csv')
    combined_df.to_csv(combined_file_path, index=False)

    print(f"Combined data written to '{combined_file_path}'.")

# Example usage:

# Example usage:
combine_csv_files('/Users/conor/conorjones-github/ConorJonesProjects/Vertuvisor/making_classes_list/classes_folder')
