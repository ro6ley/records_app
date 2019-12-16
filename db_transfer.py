import csv
from datetime import datetime
import psycopg2


# create table
SQL_STRING = """
CREATE TABLE IF NOT EXISTS entries (
    id INT PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    temperature VARCHAR (50) NOT NULL,
    duration VARCHAR (50) NOT NULL
)
"""

conn = psycopg2.connect(dbname="records_app", user='demouser', password='demouser', host='localhost')
conn.autocommit = True

cur = conn.cursor()
# create table
cur.execute(SQL_STRING)

with open('task_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("Skipping row with column titles")
            line_count += 1
        else:
            cur.execute(
                "INSERT INTO entries (id, timestamp, temperature, duration) VALUES (%s, %s, %s, %s);", 
                (row[0], row[1], row[2], row[3])
            ) 
            line_count += 1
    print(f'Processed {line_count} entries.')
