#Database connection and table creation for the task management application.
import sqlite3 #imports Python's SQLite library.

def get_connection(): 
    connection = sqlite3.connect("tasks.db") #connects to your database. and task.db is your database file.
    connection.row_factory = sqlite3.Row #lets us access database results by column name.
    return connection #gives the connection back to the application.

def create_table(): #This creates a table with two columns:
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            title TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
    print("Database and tasks table created!")