**CORD-19 Dataset Analysis**

This project provides a comprehensive analysis of the COVID-19 Open Research Dataset (CORD-19) using Python and Streamlit. The project demonstrates data cleaning, exploration, visualization, and building an interactive dashboard for COVID-19 research papers.

**Overview**

The CORD-19 dataset is a collection of scholarly articles about COVID-19 and related coronavirus research. This project explores the dataset to understand publication trends, leading journals, and authors, while ensuring clean and accurate data for analysis.

**Features**

Data Exploration: Load and explore the CORD-19 metadata.

Data Cleaning: Handle missing values, standardize columns, and derive additional features.

Visualizations: Generate charts for:

Publications per year

Top journals by publication count

Top authors by publication count

Interactive Dashboard: Streamlit application with multiple tabs for insights and data exploration.

Files

streamlit_app.py – Main Streamlit application

explore_data.py – Initial data exploration script

clean_data.py – Data cleaning script

visualizations.py – Script to generate static visualizations

metadata.csv – Original CORD-19 metadata

metadata_cleaned.csv – Cleaned dataset

images/*.png – Generated visualization images

**Installation**

Clone the repository:

git clone https://github.com/OgayoTK1/Frameworks_Assignment.git
cd Frameworks_Assignment

**
Install required packages:**

pip install pandas matplotlib seaborn streamlit pillow


**Download the CORD-19 metadata:**

wget https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-05-01/metadata.csv

Usage
Run Data Analysis Scripts

Explore the data:

python3 explore_data.py


Clean the data:

python3 clean_data.py


Generate visualizations:

python3 visualizations.py

Run Streamlit Application
streamlit run streamlit_app.py

**Dataset Information**

Source: CORD-19 Dataset by Allen Institute for AI

Columns:

title

abstract

publish_time

publish_year

authors

journal

source_x

abstract_word_count

Data Cleaning Highlights:

Standardized column names and types

Filled missing values in authors and journal with "Unknown"

Derived publish_year from publish_time

**Key Findings**

Significant surge in COVID-19 publications in 2020, peaking in 2021, stabilizing in 2022

Top journals include Lancet, Nature, JAMA, BMJ, NEJM, Pediatrics

Consistent first authors are identifiable, showing leading researchers in the field

Overall data quality is high, with minimal missing values in critical fields

Date range is automatically calculated from the dataset, ensuring accuracy

Technologies & Tools

Python 3.11 – Core programming language

pandas – Data manipulation and cleaning

matplotlib & seaborn – Visualization and statistical plots

Streamlit – Interactive web application framework

Pillow – Image handling

Learning Objectives Achieved

Extract meaningful insights from large-scale, real-world datasets

Implement robust data cleaning and preprocessing workflows

Design and generate static and interactive visualizations

Build and deploy an interactive dashboard with Streamlit

Communicate analytical findings effectively to stakeholders

**Deployment**

Streamlit Cloud deployment: Live App Link

Static images are generated in the images/ folder for reproducibility

License

This project is for educational purposes. The CORD-19 dataset is provided by the Allen Institute for AI under its respective license terms.

Acknowledgments

Allen Institute for AI for providing the CORD-19 dataset

Streamlit for enabling fast, interactive web application development

All contributors to open-source Python libraries utilized in this project
**Summary Insights**

This section highlights the most critical insights from the CORD-19 dataset, providing actionable and high-level information for researchers, analysts, and decision-makers.

**Publication Trends**

COVID-19 research exploded in 2020, peaked in 2021, and stabilized in 2022.

Yearly publication counts reflect a rapid response by the scientific community to the pandemic.

Top Journals

Leading journals publishing COVID-19 research include Lancet, Nature, JAMA, BMJ, NEJM, and Pediatrics.

These journals dominate high-impact research dissemination.

Authors & Research Leaders

First-author analysis identifies consistent contributors and leading researchers.

Patterns of prolific authors indicate research hubs and collaborative networks.

**Data Quality & Completeness**

Minimal missing values for critical fields (authors, journal, publish_year).

Cleaned data ensures reliable analysis and reproducibility.

**Dataset Coverage**

Papers from 2019–2022 are included, covering the initial outbreak and subsequent global research surge.

Abstract word counts and publication dates are accurately processed for trend analysis.

**Visualization Insights**

Publications per Year: Clear spike in publications during 2020–2021.

Top Journals: Bar charts highlight leading publishers.

Top Authors: Bar charts show top contributors and first-author prominence.

Interactive Dashboard Highlights

Users can filter by year range and journals.

Interactive charts allow quick exploration of trends and insights.

Downloadable dataset and images support further offline analysis.

**Visual Summary**: All charts and figures are stored in the images/ folder and displayed dynamically in the Streamlit app. Users can access visualizations for quick reference, comparison, and reporting purposes.
