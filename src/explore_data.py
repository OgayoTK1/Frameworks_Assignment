import pandas as pd

# Load the metadata.csv file
df = pd.read_csv('metadata.csv')

# Display the first 5 rows of the DataFrame
print('First 5 rows of the DataFrame:')
print(df.head())

# Display the column names and their data types
print('\nColumn names and their data types:')
print(df.info())

# Display basic statistical summary of numerical columns
print('\nBasic statistical summary of numerical columns:')
print(df.describe())

# Display the number of rows and columns
print(f'\nNumber of rows: {df.shape[0]}')
print(f'Number of columns: {df.shape[1]}')


