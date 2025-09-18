import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned metadata.csv file
df = pd.read_csv("metadata_cleaned.csv")

# 1. Number of publications per year
plt.figure(figsize=(12, 6))
sns.countplot(x='publish_year', data=df, palette='viridis')
plt.title('Number of Publications per Year')
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('publications_per_year.png')
plt.close()

# 2. Top 10 Journals by Publication Count
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='magma')
plt.title('Top 10 Journals by Publication Count')
plt.xlabel('Number of Publications')
plt.ylabel('Journal')
plt.tight_layout()
plt.savefig('top_journals.png')
plt.close()

# 3. Top 10 Authors by Publication Count (considering only the first author for simplicity)
top_authors = df['authors'].apply(lambda x: str(x).split(";")[0].strip()).value_counts().head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x=top_authors.values, y=top_authors.index, palette='plasma')
plt.title('Top 10 Authors by Publication Count (First Author)')
plt.xlabel('Number of Publications')
plt.ylabel('Author')
plt.tight_layout()
plt.savefig('top_authors.png')
plt.close()

print("Visualizations generated and saved as PNG files.")


