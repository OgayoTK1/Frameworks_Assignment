import pandas as pd

def load_and_clean_data(filepath="../data/metadata.csv"):
    """Load metadata and clean missing values"""
    df = pd.read_csv(filepath)

    # Drop rows without titles (essential info)
    df = df.dropna(subset=["title"])

    # Convert publish_time to datetime
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year

    # Fill missing journals/authors with placeholder
    df["journal"] = df["journal"].fillna("Unknown")
    df["authors"] = df["authors"].fillna("Unknown")

    # Add word count for abstracts
    df["abstract_word_count"] = df["abstract"].fillna("").apply(lambda x: len(x.split()))

    return df

