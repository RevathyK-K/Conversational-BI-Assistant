
import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('vibe.db')
cursor = conn.cursor()

# Create the employees table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    employee_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone_number TEXT,
    job_title TEXT,
    department_id INTEGER,
    manager_id INTEGER
)
""")

# Open the CSV file and insert data into the table
with open('employees.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO employees (employee_id, first_name, last_name, email, phone_number, job_title, department_id, manager_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from employees.csv has been loaded into the employees table in vibe.db")
