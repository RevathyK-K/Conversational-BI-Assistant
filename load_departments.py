
import sqlite3
import csv

# Connect to or create the database
conn = sqlite3.connect('vibe.db')
cursor = conn.cursor()

# Create the departments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY,
    department_name TEXT,
    location TEXT
)
""")

# Open the CSV file and insert data into the table
with open('departments.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO departments (department_id, department_name, location) VALUES (?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from departments.csv has been loaded into the departments table in vibe.db")
