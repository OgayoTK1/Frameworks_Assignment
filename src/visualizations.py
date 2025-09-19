import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure images folder exists
os.makedirs("images", exist_ok=True)

# Load the cleaned metadata
df = pd.read_csv("data/metadata_cleaned.csv")

# Strip column names to remove accidental spaces
df.columns = df.columns.str.strip()

# Rename 'year' column to 'publish_year' to keep consistent naming
df.rename(columns={'year': 'publish_year'}, inplace=True)

# -----------------------------
# 1. Number of publications per year
# -----------------------------
plt.figure(figsize=(12, 6))
sns.countplot(
    x='publish_year',
    data=df,
    palette='viridis',
    order=sorted(df['publish_year'].dropna().unique()),
    legend=False  # Fix FutureWarning in Seaborn v0.14+
)
plt.title('Number of Publications per Year')
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/publications_per_year.png")
plt.close()

# -----------------------------
# 2. Top 10 Journals by Publication Count
# -----------------------------
# Avoid inplace chained assignment warning
df['journal'] = df['journal'].fillna("Unknown")
top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(12, 6))
sns.barplot(
    x=top_journals.values,
    y=top_journals.index,
    palette='magma',
    legend=False  # Fix FutureWarning
)
plt.title('Top 10 Journals by Publication Count')
plt.xlabel('Number of Publications')
plt.ylabel('Journal')

# Add value labels
for index, value in enumerate(top_journals.values):
    plt.text(value + 0.5, index, str(value))

plt.tight_layout()
plt.savefig("images/top_journals.png")
plt.close()

# -----------------------------
# 3. Top 10 Authors by Publication Count (first author)
# -----------------------------
# Avoid inplace chained assignment warning
df['authors'] = df['authors'].fillna("Unknown")
top_authors = (
    df['authors']
    .apply(lambda x: str(x).split(";")[0].strip())
    .value_counts()
    .head(10)
)

plt.figure(figsize=(12, 6))
sns.barplot(
    x=top_authors.values,
    y=top_authors.index,
    palette='plasma',
    legend=False  # Fix FutureWarning
)
plt.title('Top 10 Authors by Publication Count (First Author)')
plt.xlabel('Number of Publications')
plt.ylabel('Author')

# Add value labels
for index, value in enumerate(top_authors.values):
    plt.text(value + 0.5, index, str(value))

plt.tight_layout()
plt.savefig("images/top_authors.png")
plt.close()

print("✅ Visualizations generated and saved in the images/ folder.")
