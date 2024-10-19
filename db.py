import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('rules.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the schema for the rules table
create_table_query = '''
CREATE TABLE IF NOT EXISTS rules (
    id INTEGER PRIMARY KEY,
    rule_string TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

# Execute the query to create the table
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()