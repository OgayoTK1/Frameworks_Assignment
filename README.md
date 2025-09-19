# CORD-19 Dataset Analysis

This project provides a comprehensive analysis of the COVID-19 Open Research Dataset (CORD-19) using Python and Streamlit.

## Overview

The CORD-19 dataset is a collection of scholarly articles about COVID-19 and related coronavirus research. This project demonstrates basic data analysis skills by exploring the dataset and creating visualizations to understand publication trends.

## Features

- **Data Exploration**: Load and explore the CORD-19 metadata
- **Data Cleaning**: Handle missing values and prepare data for analysis
- **Visualizations**: Create meaningful charts showing:
  - Publications per year
  - Top journals by publication count
  - Top authors by publication count
- **Interactive Dashboard**: Streamlit web application with multiple tabs for data exploration

## Files

- `streamlit_app.py` - Main Streamlit application
- `explore_data.py` - Initial data exploration script
- `clean_data.py` - Data cleaning script
- `create_visualizations.py` - Script to generate static visualizations
- `metadata.csv` - Original CORD-19 metadata (downloaded)
- `metadata_cleaned.csv` - Cleaned dataset
- `*.png` - Generated visualization images

## Installation

1. Clone this repository:
```bash
git clone https://github.com/OgayoTK1/Frameworks_Assignment.git
cd Frameworks_Assignment
```

2. Install required packages:
```bash
pip install pandas matplotlib seaborn streamlit
```

3. Download the CORD-19 metadata:
```bash
wget https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-05-01/metadata.csv
```

## Usage

### Run Data Analysis Scripts

1. Explore the data:
```bash
python3 explore_data.py
```

2. Clean the data:
```bash
python3 clean_data.py
```

3. Generate visualizations:
```bash
python3 create_visualizations.py
```

### Run Streamlit Application

```bash
streamlit run streamlit_app.py
```

The application will be available at `http://localhost:8501`

## Dataset Information

- **Source**: COVID-19 Open Research Dataset (CORD-19)
- **Version**: 2020-05-01
- **Size**: ~57,688 papers after cleaning
- **Time Range**: 1951-2021
- **Columns**: cord_uid, source_x, title, doi, license, abstract, publish_time, authors, journal, has_pdf_parse, has_pmc_xml_parse, publish_year

## Key Findings

- The dataset contains research papers spanning 70 years (1951-2021)
- Significant increase in COVID-19 related publications in 2020
- Top journals include major medical and virology publications
- Data quality is generally good with minimal missing values in key fields

## Technologies Used

- **Python 3.11**
- **pandas** - Data manipulation and analysis
- **matplotlib** - Static visualizations
- **seaborn** - Statistical data visualization
- **Streamlit** - Interactive web application framework

## Learning Objectives Achieved

✅ Practice loading and exploring a real-world dataset  
✅ Learn basic data cleaning techniques  
✅ Create meaningful visualizations  
✅ Build a simple interactive web application  
✅ Present data insights effectively  

## License

This project is for educational purposes. The CORD-19 dataset is provided by the Allen Institute for AI under their respective license terms.

## Acknowledgments

- Allen Institute for AI for providing the CORD-19 dataset
  

