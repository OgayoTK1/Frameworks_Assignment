import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud

# Part 1: Data Loading and Exploration
# Load the metadata.csv file (download from Kaggle: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
df = pd.read_csv('metadata.csv', low_memory=False)

# Display first few rows
print("First 5 rows of the dataset:")
print(df.head())

# Check dimensions, data types, and missing values
print("\nDimensions (rows, columns):", df.shape)
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe())

# Part 2: Data Cleaning and Preparation
# Calculate percentage of missing values
print("\nPercentage of missing values:")
print(df.isnull().mean() * 100)

# Drop rows where critical columns (title, publish_time) are missing
df_cleaned = df.dropna(subset=['title', 'publish_time'])

# Fill missing abstracts with a placeholder
df_cleaned['abstract'] = df_cleaned['abstract'].fillna("No abstract available")

# Convert publish_time to datetime and extract year
df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
df_cleaned['year'] = df_cleaned['publish_time'].dt.year

# Create a column for abstract word count
df_cleaned['abstract_word_count'] = df_cleaned['abstract'].apply(lambda x: len(str(x).split()) if x else 0)

# Save cleaned dataset
df_cleaned.to_csv('cleaned_metadata.csv', index=False)
print("\nCleaned dataset saved as 'cleaned_metadata.csv'")

# Part 3: Data Analysis
# Count papers by publication year
year_counts = df_cleaned['year'].value_counts().sort_index()

# Identify top journals
top_journals = df_cleaned['journal'].value_counts().head(10)

# Word frequency in titles
titles = df_cleaned['title'].dropna().str.lower()
words = ' '.join(titles).split()
word_freq = Counter(words)
common_words = dict(word_freq.most_common(20))
print("\nMost common words in titles:", common_words)

# Part 3: Visualizations
# Plot publications by year
plt.figure(figsize=(10, 6))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title('Number of Publications by Year')
plt.xlabel('Year')
plt.ylabel('Number of Papers')
plt.savefig('publications_by_year.png')
plt.close()

# Bar chart of top journals
plt.figure(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis')
plt.title('Top 10 Journals Publishing COVID-19 Research')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.savefig('top_journals.png')
plt.close()

# Word cloud of titles
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(titles))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
plt.savefig('title_wordcloud.png')
plt.close()

# Distribution of paper counts by source
source_counts = df_cleaned['source_x'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index, palette='magma')
plt.title('Paper Counts by Source')
plt.xlabel('Number of Papers')
plt.ylabel('Source')
plt.savefig('source_counts.png')
plt.close()

print("\nVisualizations saved as PNG files.")
