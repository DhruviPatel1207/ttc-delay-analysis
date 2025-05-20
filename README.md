# TTC Subway Delay Analysis

This project analyzes Toronto Transit Commission (TTC) subway delay data to uncover patterns in service disruptions. The goal is to identify stations with frequent or lengthy delays, analyze monthly trends, and generate actionable insights for improving transit efficiency.

# Tools & Technologies Used

- Python – for data cleaning and transformation (pandas, numpy)
- SQLite – for structured storage and SQL querying
- Power BI – for interactive dashboards and visualizations
- Jupyter Notebook – for exploratory data analysis

# Project Structure

- `data/` – raw and cleaned datasets  
- `notebooks/` – Jupyter notebooks for EDA and analysis  
- `scripts/` – Python scripts for processing and SQL setup  
- `ttc_delays.db` – SQLite database file  
- `README.md` – project overview  

# Key Features

- Identifies top 10 delay-prone stations
- Analyzes average delays by month and station
- Filters delay types for targeted insights
- SQL integration for efficient querying

# Insights

- Delay patterns peak mid-year
- Interchange stations like Finch and Kennedy report the highest delays
- Raw CSV data was cleaned and reshaped for analysis

# How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/ttc-delay-analysis.git
   
3. Open the Jupyter notebooks or connect to `ttc_delays.db` to explore the data.

4. Use Power BI to visualize trends using the cleaned dataset or SQL outputs.

