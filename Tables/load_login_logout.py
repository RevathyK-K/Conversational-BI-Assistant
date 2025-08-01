
import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('vibe.db')
cursor = conn.cursor()

# Create the login_logout table
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_logout (
    log_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    login_timestamp TEXT,
    logout_timestamp TEXT
)
""")

# Open the CSV file and insert data into the table
with open('login_logout.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO login_logout (log_id, employee_id, login_timestamp, logout_timestamp) VALUES (?, ?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from login_logout.csv has been loaded into the login_logout table in vibe.db")
