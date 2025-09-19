import os
import streamlit as st
import pandas as pd
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="CORD-19 Dataset Analysis",
    page_icon="🦠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🦠 CORD-19 Dataset Analysis")
st.markdown("""
This application provides an analysis of the COVID-19 Open Research Dataset (CORD-19).
The dataset contains metadata about COVID-19 and coronavirus-related research papers.
""")

# Load data
@st.cache_data
def load_data():
    file_path = os.path.join("data", "metadata_cleaned.csv")
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        df['publish_year'] = df['publish_year'].astype(int)
        df['authors'] = df['authors'].fillna("Unknown")
        df['journal'] = df['journal'].fillna("Unknown")
        return df
    else:
        return None

df = load_data()
if df is None:
    st.error("❌ Dataset not found! Please place `metadata_cleaned.csv` inside the `data/` folder.")
    st.stop()

# Date range
min_year = df['publish_year'].min()
max_year = df['publish_year'].max()

# Sidebar
st.sidebar.header("Dataset Overview")
st.sidebar.metric("Total Papers", len(df))
st.sidebar.metric("Date Range", f"{min_year} - {max_year}")
st.sidebar.metric("Unique Authors", df['authors'].nunique())
st.sidebar.metric("Unique Journals", df['journal'].nunique())

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview", "📈 Visualizations", "🔍 Data Explorer", "📋 Raw Data"
])

# Tab 1: Overview
with tab1:
    st.header("Dataset Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Publications", len(df))
        st.metric("Unique Authors", df['authors'].nunique())
    with col2:
        st.metric("Unique Journals", df['journal'].nunique())
    with col3:
        if "has_pdf_parse" in df.columns:
            st.metric("Papers with PDF", df['has_pdf_parse'].sum())
        if "has_pmc_xml_parse" in df.columns:
            st.metric("Papers with XML", df['has_pmc_xml_parse'].sum())
    st.subheader("Data Quality")
    missing_data = df.isnull().sum()
    if missing_data.sum() > 0:
        st.bar_chart(missing_data[missing_data > 0])
    else:
        st.success("No missing values detected!")

# Tab 2: Visualizations
with tab2:
    st.header("Data Visualizations")
    def load_image(filename):
        path = os.path.join("images", filename)
        return Image.open(path) if os.path.exists(path) else None

    st.subheader("Publications per Year")
    img1 = load_image("publications_per_year.png")
    if img1: st.image(img1, caption="Number of publications by year")

    st.subheader("Top Journals")
    img2 = load_image("top_journals.png")
    if img2: st.image(img2, caption="Top 10 journals by publication count")

    st.subheader("Top Authors")
    img3 = load_image("top_authors.png")
    if img3: st.image(img3, caption="Top 10 authors by publication count")

# Tab 3: Data Explorer
with tab3:
    st.header("Data Explorer")
    year_range = st.slider("Select year range", int(min_year), int(max_year), (int(min_year), int(max_year)))
    journals = st.multiselect(
        "Select journals",
        options=df['journal'].dropna().unique(),
        default=df['journal'].value_counts().head(5).index.tolist()
    )
    filtered_df = df[(df['publish_year'] >= year_range[0]) & (df['publish_year'] <= year_range[1])]
    if journals:
        filtered_df = filtered_df[filtered_df['journal'].isin(journals)]
    st.write(f"Filtered dataset: {len(filtered_df)} papers")
    if not filtered_df.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.write("Top 5 journals in filtered data:")
            st.write(filtered_df['journal'].value_counts().head())
        with col2:
            st.write("Publications by year in filtered data:")
            st.write(filtered_df['publish_year'].value_counts().sort_index())
    else:
        st.warning("No data matches the selected filters.")

# Tab 4: Raw Data
with tab4:
    st.header("Raw Data")
    st.dataframe(df.head(1000))
    csv = df.to_csv(index=False)
    st.download_button("Download full dataset as CSV", csv, "cord19_metadata.csv", "text/csv")

# Footer
st.markdown("---")
st.markdown("Data source: [CORD-19 Dataset](https://www.semanticscholar.org/cord19)")
st.markdown("Developed by Ogayo Andrew | [GitHub](https://github.com/OgayoTK1)")
st.markdown("© 2024 All rights reserved.")