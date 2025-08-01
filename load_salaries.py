
import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('vibe.db')
cursor = conn.cursor()

# Create the salaries table
cursor.execute("""
CREATE TABLE IF NOT EXISTS salaries (
    salary_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    salary_amount REAL,
    from_date TEXT,
    to_date TEXT
)
""")

# Open the CSV file and insert data into the table
with open('salaries.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO salaries (salary_id, employee_id, salary_amount, from_date, to_date) VALUES (?, ?, ?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from salaries.csv has been loaded into the salaries table in vibe.db")
