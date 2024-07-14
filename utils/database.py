import sqlite3

class Database:
    def __init__(self, db_file):
        """
        Initialize the database connection and cursor.
        Create tables if they do not exist.
        """
        self.conn = sqlite3.connect(db_file)  # Connect to the SQLite database
        self.cur = self.conn.cursor()  # Create a cursor object to interact with the database
        self.create_tables()  # Ensure the necessary tables are created

    def create_tables(self):
        """
        Create the reminders table if it does not already exist.
        The table includes columns for id, description, datetime, and recurring status.
        """
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY,
                description TEXT,
                datetime TEXT,
                recurring TEXT
            )
        ''')
        self.conn.commit()  # Commit the changes to the database

    def add_reminder(self, reminder):
        """
        Add a new reminder to the database.
        Parameters:
            reminder (Reminder): The reminder object to add to the database.
        """
        self.cur.execute('''
            INSERT INTO reminders (description, datetime, recurring)
            VALUES (?, ?, ?)
        ''', (reminder.description, str(reminder.datetime), str(reminder.recurring)))
        self.conn.commit()  # Commit the changes to the database

    def get_reminders(self):
        """
        Retrieve all reminders from the database.
        Returns:
            list: A list of tuples representing all reminders in the database.
        """
        self.cur.execute('SELECT * FROM reminders')
        return self.cur.fetchall()  # Fetch and return all results from the query
