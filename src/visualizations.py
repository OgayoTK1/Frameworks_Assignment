import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("images", exist_ok=True)
df = pd.read_csv("data/metadata_cleaned.csv")
df.columns = df.columns.str.strip()
df['publish_year'] = df['publish_year'].astype(int)
df['authors'] = df['authors'].fillna("Unknown")
df['journal'] = df['journal'].fillna("Unknown")

# Publications per year
plt.figure(figsize=(12,6))
sns.countplot(x='publish_year', data=df, palette='viridis',
              order=sorted(df['publish_year'].unique()))
plt.title('Number of Publications per Year')
plt.xlabel('Year')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/publications_per_year.png")
plt.close()

# Top 10 journals
top_journals = df['journal'].value_counts().head(10)
plt.figure(figsize=(12,6
