import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_cleaning import load_and_clean_data

# Load data
df = load_and_clean_data("../data/metadata.csv")

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (sample metadata.csv)")

# Sidebar filters
year_range = st.slider("Select Year Range", 2018, 2023, (2020, 2021))
filtered_df = df[(df["year"] >= year_range[0]) & (df["year"] <= year_range[1])]

# Publications by year
st.subheader("Publications by Year")
year_counts = filtered_df["year"].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis", ax=ax)
ax.set_title("Top 10 Journals")
st.pyplot(fig)

# Data preview
st.subheader("Sample Data")
st.write(filtered_df.head(20))

