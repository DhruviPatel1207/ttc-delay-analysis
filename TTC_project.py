import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns

# Path to the folder containing your files
folder_path = "D:/Dhruvi/FY/Project/TTC_subway_delay_data/"

# List all the Excel files in the folder
file_names = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# Initialize an empty list to store the data
data_frames = []

# Loop through each file and read it
for file_name in file_names:
    file_path = os.path.join(folder_path, file_name)
    data = pd.read_excel(file_path)  # Read the Excel file
    
    # Drop columns that are unnamed
    data = data.loc[:, ~data.columns.str.contains('^Unnamed')]
    
    # Add the data to the list
    data_frames.append(data)

# Combine all data into one DataFrame
combined_data = pd.concat(data_frames, ignore_index=True)

# Check the first few rows of the combined data
print(combined_data.head())

# Check for missing values in the combined data
print(combined_data.isnull().sum())

# Fill missing values with 0
combined_data.fillna(0, inplace=True)

# Check the result
print(combined_data.isnull().sum())

# Convert "Date" and "Time" columns to datetime format
combined_data['Date'] = pd.to_datetime(combined_data['Date'])
combined_data['Time'] = pd.to_datetime(combined_data['Time'], format='%H:%M').dt.time

# Check the updated data types
#print(combined_data.dtypes)

# Summary statistics for numerical columns
print(combined_data.describe())

# Convert 'Date' to datetime for proper plotting
combined_data['Date'] = pd.to_datetime(combined_data['Date'])

# Plot 'Min Delay' over time
plt.figure(figsize=(10, 6))
plt.plot(combined_data['Date'], combined_data['Min Delay'], color='blue', alpha=0.5)
plt.title('Subway Delay Over Time')
plt.xlabel('Date')
plt.ylabel('Delay (Minutes)')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.grid(True)
plt.show()

# Aggregate delays per station
station_delays = combined_data.groupby('Station')['Min Delay'].sum().sort_values(ascending=False)

# Plot top 20 stations with the highest delays
plt.figure(figsize=(12, 6))
station_delays.head(20).plot(kind='bar', color='red', alpha=0.7)
plt.title('Top 20 Stations with Most Delay')
plt.xlabel('Station')
plt.ylabel('Total Delay (Minutes)')
plt.xticks(rotation=90)
plt.grid(axis='y')
plt.show()

# Define valid subway lines (based on TTC)
valid_lines = ['YU', 'BD', 'SHP', 'SRT']  # YU = Yonge-University, BD = Bloor-Danforth, SHP = Sheppard, SRT = Scarborough RT

# Filter dataset to include only subway lines
subway_data = combined_data[combined_data['Line'].isin(valid_lines)]

# Group by Line and calculate average delay
delay_by_line = subway_data.groupby('Line')['Min Delay'].agg(['mean', 'count']).reset_index()

# Rename columns
delay_by_line.columns = ['Line', 'Avg Delay (Minutes)', 'Number of Delays']

# Sort by average delay
delay_by_line = delay_by_line.sort_values(by='Avg Delay (Minutes)', ascending=False)

# Plot
plt.figure(figsize=(8, 5))
sns.barplot(data=delay_by_line, x='Line', y='Avg Delay (Minutes)', palette='Blues_r')
plt.title('Average Delay by Subway Line')
plt.xlabel('Subway Line')
plt.ylabel('Avg Delay (Minutes)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Extract year from the Date column
combined_data['Year'] = combined_data['Date'].dt.year

# Aggregate total delay per year
annual_delays = combined_data.groupby('Year')['Min Delay'].sum().reset_index()

# Plot annual delay trends
plt.figure(figsize=(10, 5))
plt.bar(annual_delays['Year'], annual_delays['Min Delay'], color='blue', alpha=0.7)
plt.title('Annual Subway Delay Trends')
plt.xlabel('Year')
plt.ylabel('Total Delay (Minutes)')
plt.xticks(annual_delays['Year'])
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Extract Year and Month
combined_data['Year'] = combined_data['Date'].dt.year
combined_data['Month'] = combined_data['Date'].dt.month

#Aggregate Delays by Year and Month
monthly_delays = combined_data.groupby(['Year', 'Month'])['Min Delay'].mean().reset_index()

#Plot the Trends
plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_delays, x="Month", y="Min Delay", hue="Year", marker="o")

plt.title("Average Subway Delay Trends by Month (Annual Comparison)")
plt.xlabel("Month")
plt.ylabel("Average Delay (Minutes)")
plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(title="Year")
plt.grid(True)
plt.show()


# Dictionary to clean up inconsistent line names
line_mapping = {
    'YU/BD': 'YU', 'YU / BD': 'YU', 'YU-BD': 'YU', 'BLOOR DANFORTH LINES': 'BD', 
    'YUS': 'YU', 'B/D': 'BD', 'BD LINE': 'BD', '999': None, 'YONGE/UNIVERSITY/BLOOR': 'YU',
    'BD/YU': 'BD', 'Y/BD': 'YU', 'YU/BD LINES': 'YU', 'YU & BD': 'YU', 'YUS AND BD': 'YU', 
    'YUS/BD': 'YU', 'YU/BD LINE': 'YU', 'LINE 2 SHUTTLE': 'SRT', 'BLOOR DANFORTH': 'BD', 
    'SHEP': 'SHP', 'LINE 1': 'YU', 'ONGE-UNIVERSITY AND BL': 'YU', 'YU/BD/SHP': 'YU', 
    'BD/ YUS': 'BD', 'BD/ YU': 'BD'
}

# Replace the invalid line names with the correct ones
combined_data['Line'] = combined_data['Line'].replace(line_mapping)

# Filter out any rows where 'Line' is null or invalid (e.g., 999 or non-relevant lines)
valid_lines = ['YU', 'BD', 'SHP', 'SRT']
subway_data = combined_data[combined_data['Line'].isin(valid_lines)]

# Check the unique values after cleaning
print(subway_data['Line'].unique())

# Group by 'Line' and calculate the average delay
delays_by_line = subway_data.groupby('Line')['Min Delay'].mean().reset_index()

# Sort the lines by average delay (descending)
delays_by_line = delays_by_line.sort_values(by='Min Delay', ascending=False)

# Plot the results
plt.figure(figsize=(8, 5))
sns.barplot(data=delays_by_line, x='Line', y='Min Delay', palette='Blues_r')
plt.xlabel('Subway Line')
plt.ylabel('Average Delay (Minutes)')
plt.title('Average Subway Delay by Line')
plt.xticks(rotation=0)  # Keep subway lines readable
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Compare delays between weekends and weekdays
# Extract day of the week from the 'Date' column (0 = Monday, 6 = Sunday)
combined_data['Day of Week'] = combined_data['Date'].dt.dayofweek

# Create a new column to categorize as 'Weekend' or 'Weekday'
combined_data['Day Type'] = combined_data['Day of Week'].apply(lambda x: 'Weekend' if x >= 5 else 'Weekday')

# Group by 'Day Type' and calculate average delay
weekday_weekend_delays = combined_data.groupby('Day Type')['Min Delay'].mean().reset_index()

# Plot the results
plt.figure(figsize=(8, 5))
sns.barplot(data=weekday_weekend_delays, x='Day Type', y='Min Delay', palette='viridis')
plt.title('Average Subway Delay: Weekend vs Weekday')
plt.xlabel('Day Type')
plt.ylabel('Average Delay (Minutes)')
plt.grid(axis='y')
plt.show()

import sqlite3

# Connect to (or create) a SQLite database file
conn = sqlite3.connect('ttc_delays.db')

# Export the combined_data DataFrame to a table named 'delays'
combined_data.to_sql('delays', conn, if_exists='replace', index=False)

# Close the database connection
conn.close()
