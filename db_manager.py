import sqlite3

def create_db():
    # Step 1: Connect to the SQLite database (or create a new one if it doesn't exist)
    conn = sqlite3.connect('emaildb.sqlite3')
    # Step 2: Create a cursor object
    cursor = conn.cursor()
    # Step 3: Define an SQL command to create the table
    create_table_sql = '''
    CREATE TABLE IF NOT EXISTS mytable (
    id INTEGER PRIMARY KEY,
    subject TEXT,
    sender_name TEXT,
    sender_email TEXT,
    receiver_name TEXT,
    receiver_email TEXT,
    attachment_name TEXT,
    content_type TEXT,
    datetime TEXT
)'''

    # Step 4: Execute the SQL command to create the table
    cursor.execute(create_table_sql)

    # Step 5: Commit the changes and close the database connection
    conn.commit()
    conn.close()

    print("Database and table created successfully.")


def store_data(data_dict):
    # Connect to the SQLite database
    conn = sqlite3.connect('emaildb.sqlite3')
    cursor = conn.cursor()

    # Define data to be inserted
    data_to_insert = (
        data_dict['subject'],
        data_dict['sender_name'],
        data_dict['sender_email'],
        data_dict['receiver_name'],
        data_dict['receiver_email'],
        data_dict['attachment_name'], 
        data_dict['content_type'], 
        data_dict['datetime'], 
    )

    # Insert data into the table
    insert_sql = '''
    INSERT INTO mytable (subject, sender_name, sender_email, receiver_name, receiver_email, attachment_name, content_type, datetime)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    cursor.execute(insert_sql, data_to_insert)

    # Commit the changes and close the database connection
    conn.commit()
    conn.close()
    print("Data inserted in db successfully.")

