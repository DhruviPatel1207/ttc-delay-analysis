import sqlite3
import pandas as pd

# Connect to the existing database
conn = sqlite3.connect('ttc_delays.db')

#Query 1: Top 10 stations with most delay
query1 = '''
SELECT Station, SUM("Min Delay") AS Total_Delay
FROM delays
GROUP BY Station
ORDER BY Total_Delay DESC
LIMIT 10;
'''
top_station_delays = pd.read_sql_query(query1, conn)
print("Top 10 stations by total delay:\n", top_station_delays)

top_station_delays.to_csv("top_station_delays.csv", index=False)


# Query 2: Average delay by subway line
query2 = '''
SELECT Line, AVG("Min Delay") AS Avg_Delay
FROM delays
WHERE Line IN ('YU', 'BD', 'SHP', 'SRT')
GROUP BY Line
ORDER BY Avg_Delay DESC;
'''
avg_delay_by_line = pd.read_sql_query(query2, conn)
print("\nAverage delay by subway line:\n", avg_delay_by_line)

avg_delay_by_line.to_csv("avg_delay_by_line.csv", index=False)

#Query 3: Average delay based on wheter it is a weekday oe weekend
query3 = '''
SELECT "Day Type", AVG("Min Delay") AS Avg_Delay
FROM delays
GROUP BY "Day Type"
ORDER BY Avg_Delay DESC;
'''
avg_delay_by_day = pd.read_sql_query(query3, conn)
print("\nAverage delay by day:\n",avg_delay_by_day )

avg_delay_by_day.to_csv("avg_delay_by_day.csv", index=False)

#Query 4: Delays by time of the day
query4 = '''
SELECT strftime('%H', "Time") AS Hour, AVG("Min Delay") AS Avg_Delay
FROM delays
GROUP BY Hour
ORDER BY Hour;
'''
average_delay_by_time_of_day = pd.read_sql_query(query4, conn)
print("\nAverage delay by time of the day:\n", average_delay_by_time_of_day)

average_delay_by_time_of_day.to_csv("average_delay_by_time_of_day.csv", index=False)

# Query 5: Number of delays by day of the week
query5 = '''
SELECT "Day of Week", COUNT(*) AS Total_Delays
FROM delays
GROUP BY "Day of Week"
ORDER BY Total_Delays DESC;
'''
delay_by_dayofweek = pd.read_sql_query(query5, conn)
print("\nNumber of delays by day of the week:\n", delay_by_dayofweek)

delay_by_dayofweek.to_csv("delay_by_dayofweek.csv", index=False)


# Query 6: Average delay over time by month
query6 = '''
SELECT strftime('%Y-%m', "Date") AS Month, AVG("Min Delay") AS Avg_Delay
FROM delays
GROUP BY Month
ORDER BY Month;
'''
avg_delay_by_month = pd.read_sql_query(query6, conn)
print("\nAverage delay by month:\n", avg_delay_by_month)

avg_delay_by_month.to_csv("avg_delay_by_month.csv", index=False)

# Query 7: Stations with highest average delay
query7 = '''
SELECT Station, AVG("Min Delay") AS Avg_Delay
FROM delays
GROUP BY Station
ORDER BY Avg_Delay DESC
LIMIT 10;
'''
highest_avg_delay_stations = pd.read_sql_query(query7, conn)
print("\nTop 10 stations with highest average delay:\n", highest_avg_delay_stations)

highest_avg_delay_stations.to_csv("highest_avg_delay_stations.csv", index=False)

# Query 8: Number of delays by day of the week
query8 = '''
SELECT "Day of Week", COUNT(*) AS Total_Delays
FROM delays
GROUP BY "Day of Week"
ORDER BY Total_Delays DESC;
'''
delay_by_dayofweek = pd.read_sql_query(query8, conn)
print("\nNumber of delays by day of the week:\n", delay_by_dayofweek)

delay_by_dayofweek.to_csv("delay_by_dayofweek.csv", index=False)

# Close the connection after all queries
conn.close()

