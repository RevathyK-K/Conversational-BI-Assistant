
import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('vibe.db')
cursor = conn.cursor()

# Create the performance_reviews table
cursor.execute("""
CREATE TABLE IF NOT EXISTS performance_reviews (
    review_id INTEGER PRIMARY KEY,
    employee_id INTEGER,
    reviewer_id INTEGER,
    review_date TEXT,
    rating INTEGER,
    comments TEXT
)
""")

# Open the CSV file and insert data into the table
with open('performance_reviews.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cursor.execute("INSERT INTO performance_reviews (review_id, employee_id, reviewer_id, review_date, rating, comments) VALUES (?, ?, ?, ?, ?, ?)", row)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Data from performance_reviews.csv has been loaded into the performance_reviews table in vibe.db")
