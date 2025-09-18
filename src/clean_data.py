import pandas as pd

# Load the metadata.csv file, specifying dtype for 'arxiv_id' to avoid DtypeWarning
df = pd.read_csv('metadata.csv', dtype={'arxiv_id': str}, low_memory=False)

# Drop columns that are not relevant for this basic analysis or have too many missing values
# Based on the previous df.info() output, 'sha', 'pmcid', 'pubmed_id', 'Microsoft Academic Paper ID', 'WHO #Covidence', 'arxiv_id', 'full_text_file', 'url' have many missing values or are less relevant for basic analysis.
df.drop(columns=['sha', 'pmcid', 'pubmed_id', 'Microsoft Academic Paper ID', 'WHO #Covidence', 'arxiv_id', 'full_text_file', 'url'], inplace=True)

# Handle missing values in 'title', 'abstract', 'authors', 'journal', 'publish_time'
# For 'title' and 'abstract', fill missing values with 'No Title' and 'No Abstract' respectively
df['title'].fillna('No Title', inplace=True)
df['abstract'].fillna('No Abstract', inplace=True)

# For 'authors' and 'journal', fill missing values with 'Unknown'
df['authors'].fillna('Unknown', inplace=True)
df['journal'].fillna('Unknown', inplace=True)

# For 'publish_time', drop rows with missing values as it's important for time-series analysis
df.dropna(subset=['publish_time'], inplace=True)

# Convert 'publish_time' to datetime objects
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Drop rows where 'publish_time' conversion failed (NaT values)
df.dropna(subset=['publish_time'], inplace=True)

# Extract year from 'publish_time' for potential analysis
df['publish_year'] = df['publish_time'].dt.year

# Display the first 5 rows of the cleaned DataFrame
print('First 5 rows of the cleaned DataFrame:')
print(df.head())

# Display the column names and their data types after cleaning
print('\nColumn names and their data types after cleaning:')
print(df.info())

# Save the cleaned data to a new CSV file
df.to_csv('metadata_cleaned.csv', index=False)
print('\nCleaned data saved to metadata_cleaned.csv')


