# This script can be used to convert a Parquet dataset into a CSV or Excel file to easily view and interact with large datasets.

# Remove the hashtags from lines 5, 6, and 7 the first time you run this script to install the required packages

#pip install pandas
#pip install pyarrow
#pip install openpyxl

import pandas as pd

# Update the paths below to where your files are located in your Windows Downloads folder
input_parquet_path = r'c:\Users\username\Downloads\FILENAME.parquet'  # Update this to your file's path
output_excel_path = r'c:\Users\username\Downloads\output.xlsx'  # Update this to your desired output path

# NOW YOU CAN RUN THE SCRIPT

# THE OUTPUT FILE WILL BE LOCATED IN YOUR WINDOWS DOWNLOADS FOLDER BY DEFAULT

# Reading the Parquet file
df = pd.read_parquet(input_parquet_path)

# Writing to an Excel file
df.to_excel(output_excel_path, index=False)

print(f"Successfully converted {input_parquet_path} to {output_excel_path}")
