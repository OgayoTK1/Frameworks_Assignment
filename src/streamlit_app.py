import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Set page configuration
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
    return pd.read_csv("metadata_cleaned.csv")

df = load_data()

# Sidebar
st.sidebar.header("Dataset Overview")
st.sidebar.metric("Total Papers", len(df))
st.sidebar.metric("Date Range", f"{df['publish_year'].min()} - {df['publish_year'].max()}")
st.sidebar.metric("Unique Journals", df['journal'].nunique())

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "📈 Visualizations", "🔍 Data Explorer", "📋 Raw Data"])

with tab1:
    st.header("Dataset Overview")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Publications", len(df))
        st.metric("Unique Authors", df['authors'].nunique())
    
    with col2:
        st.metric("Unique Journals", df['journal'].nunique())
        st.metric("Years Covered", df['publish_year'].max() - df['publish_year'].min() + 1)
    
    with col3:
        st.metric("Papers with PDF", df['has_pdf_parse'].sum())
        st.metric("Papers with XML", df['has_pmc_xml_parse'].sum())
    
    st.subheader("Data Quality")
    st.write("Missing values per column:")
    missing_data = df.isnull().sum()
    st.bar_chart(missing_data[missing_data > 0])

with tab2:
    st.header("Data Visualizations")
    
    # Publications per year
    st.subheader("Publications per Year")
    try:
        img1 = Image.open("publications_per_year.png")
        st.image(img1, caption="Number of publications by year")
    except FileNotFoundError:
        st.error("Visualization file not found. Please run the visualization script first.")
    
    # Top journals
    st.subheader("Top Journals")
    try:
        img2 = Image.open("top_journals.png")
        st.image(img2, caption="Top 10 journals by publication count")
    except FileNotFoundError:
        st.error("Visualization file not found. Please run the visualization script first.")
    
    # Top authors
    st.subheader("Top Authors")
    try:
        img3 = Image.open("top_authors.png")
        st.image(img3, caption="Top 10 authors by publication count")
    except FileNotFoundError:
        st.error("Visualization file not found. Please run the visualization script first.")

with tab3:
    st.header("Data Explorer")
    
    # Filter by year
    year_range = st.slider(
        "Select year range",
        min_value=int(df['publish_year'].min()),
        max_value=int(df['publish_year'].max()),
        value=(int(df['publish_year'].min()), int(df['publish_year'].max()))
    )
    
    # Filter by journal
    journals = st.multiselect(
        "Select journals",
        options=df['journal'].unique(),
        default=df['journal'].value_counts().head(5).index.tolist()
    )
    
    # Apply filters
    filtered_df = df[
        (df['publish_year'] >= year_range[0]) & 
        (df['publish_year'] <= year_range[1])
    ]
    
    if journals:
        filtered_df = filtered_df[filtered_df['journal'].isin(journals)]
    
    st.write(f"Filtered dataset: {len(filtered_df)} papers")
    
    # Show filtered data summary
    if len(filtered_df) > 0:
        st.subheader("Filtered Data Summary")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("Top 5 journals in filtered data:")
            st.write(filtered_df['journal'].value_counts().head())
        
        with col2:
            st.write("Publications by year in filtered data:")
            st.write(filtered_df['publish_year'].value_counts().sort_index())

with tab4:
    st.header("Raw Data")
    st.write("First 1000 rows of the dataset:")
    st.dataframe(df.head(1000))
    
    # Download button
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download full dataset as CSV",
        data=csv,
        file_name="cord19_metadata.csv",
        mime="text/csv"
    )

# Footer
st.markdown("---")
st.markdown("Data source: [CORD-19 Dataset](https://www.semanticscholar.org/cord19)")

