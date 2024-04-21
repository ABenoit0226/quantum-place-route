import pandas as pd
import os

def process_csvs(source_dir, target_dir):
    # Ensure the source and target directories exist
    if not os.path.exists(source_dir) or not os.path.exists(target_dir):
        print("One or both specified directories do not exist.")
        return
    
    # Iterate over all files in the source directory
    for file_name in os.listdir(source_dir):
        if file_name.endswith('.csv'):
            source_file_path = os.path.join(source_dir, file_name)
            target_file_path = os.path.join(target_dir, file_name)
            
            # Check if the corresponding file exists in the target directory
            if os.path.exists(target_file_path):
                # Read source and target CSV files
                source_df = pd.read_csv(source_file_path)
                target_df = pd.read_csv(target_file_path)
                
                # Extract columns 2-4 from the source CSV
                selected_columns = source_df.iloc[:, 1:4]  # Adjust columns as necessary
                
                # Check if target dataframe already has 5 or more columns
                if len(target_df.columns) >= 5:
                    print(f"Target file {file_name} already has 5 or more columns. Skipping insertion.")
                    continue
                
                # Check if there's room to insert the columns before the 2nd column
                if len(target_df.columns) < 2:
                    print(f"Target file {file_name} does not have enough columns to insert data before the 2nd column.")
                    continue
                
                # Insert extracted columns into the target DataFrame before the 2nd column (index 1)
                left_part = target_df.iloc[:, :1]
                right_part = target_df.iloc[:, 1:]
                target_df_modified = pd.concat([left_part, selected_columns, right_part], axis=1)
                
                # Save the modified DataFrame back to the target file
                target_df_modified.to_csv(target_file_path, index=False)
                print(f"Processed and updated {file_name}")
            else:
                print(f"No corresponding file found in target directory for {file_name}")
        else:
            print(f"Skipping non-CSV file {file_name}")


# Example usage
source_dir = 'tests'
target_dir = 'mod/tests'
process_csvs(source_dir, target_dir)

source_dir = 'gateTests'
target_dir = 'mod/gateTests'
process_csvs(source_dir, target_dir)

