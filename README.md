# TTC Subway Delay Analysis

This project analyzes Toronto Transit Commission (TTC) subway delay data to uncover patterns in service disruptions. The goal is to identify stations with frequent or lengthy delays, analyze monthly trends, and generate actionable insights for improving transit efficiency.

# Tools & Technologies Used

- **Python** – for data cleaning and SQL query execution (`TTC_project.py`, `ttc_SQL_queries.py`)
- **SQLite** – used as the relational database to store and query structured delay data (`ttc_delays.db`)
- **Power BI** – for creating interactive data visualizations (`TTC__project.pbix`)

# Project Files

- `TTC_project.py` – main data processing and analysis script
- `ttc_SQL_queries.py` – reusable SQL query functions
- `ttc_delays.db` – SQLite database file with processed delay data
- `TTC__project.pbix` – Power BI dashboard for visual insights

# Key Features

- Identifies top stations with highest total delays
- Analyzes average delays by month using SQL queries
- Visualizes delay patterns interactively in Power BI
- Organizes data in SQLite for efficient and scalable analysis

# How to Run

1. Clone the repository:
   git clone https://github.com/yourusername/ttc-delay-analysis.git
   
3. Open `TTC_project.py` to run data processing logic.

4. Explore the data using SQLite tools or the queries in `ttc_SQL_queries.py`.

5. Open `TTC__project.pbix` in Power BI Desktop to view and interact with the dashboard.

