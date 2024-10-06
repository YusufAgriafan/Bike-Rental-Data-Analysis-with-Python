# Bike Rental Data Analysis with Python - Dicoding

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)

## Overview

This project is focused on performing data analysis and visualization on a bike rental dataset. The project includes data wrangling, exploratory data analysis (EDA), and the creation of an interactive dashboard using Streamlit. The primary goal is to gain insights into bike rental trends using various analysis techniques and visualizations.

## Project Structure

- `data/`: Directory containing the raw CSV data files.
- `notebook.ipynb`: This file is used to perform data analysis.
- `dashboard.py`: Used to create dashboards of data analysis results.
- `README.md`: This documentation file.

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/YusufAgriafan/Bike-Rental-Data-Analysis-with-Python.git
```

2. Go to the project directory

```
cd Bike-Rental-Data-Analysis-with-Python
```

3. Install the required Python packages by running:

```
pip install -r requirements.txt
```

## Usage

1. **Data Wrangling**: Use the notebook.ipynb to clean, prepare, and explore the data. This includes tasks such as handling missing values, merging datasets (`day_data.csv` and `hour_data.csv`), and transforming columns as needed for analysis.

2. **Exploratory Data Analysis (EDA)**: Perform exploratory data analysis to gain insights into the bike rental trends. This is done within the Jupyter notebook where you can visualize the data using various charts and statistical summaries.

3. **Visualization**: Run the Streamlit dashboard to interactively explore the data:

```
cd Bike-Rental-Data-Analysis-with-Python
```
```
streamlit run dashboard.py
```

Access the dashboard in your web browser at `http://localhost:8501`.

## Data Sources

The project uses E-Commerce Public Dataset from [Belajar Analisis Data dengan Python's Final Project](https://drive.google.com/file/d/1RaBmV6Q6FYWU4HWZs80Suqd7KQC34diQ/view) offered by [Dicoding](https://www.dicoding.com/).
