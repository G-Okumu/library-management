import sqlite3

CONN = sqlite3.connect('DB/library.db')
CURSOR = CONN.cursor()

# method to execute the schema

def execute_schema(file_path):
    with open(file_path, 'r') as file:
        read_sql_script = file.read() # Reading the file
        
    # Execute the sql Queries or DDLs
    try:
        CURSOR.executescript(read_sql_script)
        CONN.commit()
        print("Schema created successfully")
        
    except sqlite3.Error as error:
        print(f"Error {error} Occured")