import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY,
                description TEXT,
                datetime TEXT,
                recurring TEXT
            )
        ''')
        self.conn.commit()

    def add_reminder(self, reminder):
        self.cur.execute('''
            INSERT INTO reminders (description, datetime, recurring)
            VALUES (?, ?, ?)
        ''', (reminder.description, str(reminder.datetime), str(reminder.recurring)))
        self.conn.commit()

    def get_reminders(self):
        self.cur.execute('SELECT * FROM reminders')
        return self.cur.fetchall()