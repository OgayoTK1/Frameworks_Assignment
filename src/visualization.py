import matplotlib.pyplot as plt
import seaborn as sns

def plot_publications_per_year(df):
    year_counts = df["year"].value_counts().sort_index()
    plt.figure(figsize=(8,5))
    plt.bar(year_counts.index, year_counts.values, color="skyblue")
    plt.title("Publications by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Papers")
    plt.show()

def plot_top_journals(df, n=10):
    top_journals = df["journal"].value_counts().head(n)
    plt.figure(figsize=(8,5))
    sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
    plt.title(f"Top {n} Journals Publishing COVID-19 Research")
    plt.xlabel("Number of Papers")
    plt.ylabel("Journal")
    plt.show()

def plot_sources_distribution(df):
    source_counts = df["source_x"].fillna("Unknown").value_counts()
    plt.figure(figsize=(8,5))
    sns.barplot(y=source_counts.index, x=source_counts.values, palette="Set2")
    plt.title("Distribution of Papers by Source")
    plt.xlabel("Number of Papers")
    plt.ylabel("Source")
    plt.show()

