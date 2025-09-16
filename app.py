import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Set page configuration
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")

# Load cleaned data
df = pd.read_csv('cleaned_metadata.csv')

# App title and description
st.title("CORD-19 Data Explorer")
st.write("Explore patterns in COVID-19 research papers from the CORD-19 dataset.")

# Sidebar for interactive elements
st.sidebar.header("Filter Options")
year_range = st.sidebar.slider(
    "Select Year Range",
    int(df['year'].min()),
    int(df['year'].max()),
    (2020, 2021)
)

# Filter data based on year range
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Display sample data
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'publish_time', 'abstract']].head(10))

# Visualization: Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_title('Number of Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Papers')
st.pyplot(fig)

# Visualization: Top journals
st.subheader("Top 10 Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_journals.values, y=top_journals.index, palette='viridis', ax=ax)
ax.set_title('Top 10 Journals Publishing COVID-19 Research')
ax.set_xlabel('Number of Papers')
ax.set_ylabel('Journal')
st.pyplot(fig)

# Visualization: Word cloud
st.subheader("Word Cloud of Titles")
titles = filtered_df['title'].dropna().str.lower()
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(titles))
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
ax.set_title('Word Cloud of Paper Titles')
st.pyplot(fig)

# Visualization: Paper counts by source
st.subheader("Paper Counts by Source")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x=source_counts.values, y=source_counts.index, palette='magma', ax=ax)
ax.set_title('Paper Counts by Source')
ax.set_xlabel('Number of Papers')
ax.set_ylabel('Source')
st.pyplot(fig)
