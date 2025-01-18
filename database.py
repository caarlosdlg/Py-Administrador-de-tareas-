import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.create_table()

    def create_table(self):
        query = '''CREATE TABLE IF NOT EXISTS tasks
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   title TEXT NOT NULL,
                   description TEXT,
                   due_date TEXT,
                   priority TEXT,
                   status TEXT DEFAULT 'pendiente')'''
        self.conn.execute(query)
        self.conn.commit()

    def add_task(self, title, description, due_date, priority):
        query = '''INSERT INTO tasks (title, description, due_date, priority)
                  VALUES (?, ?, ?, ?)'''
        self.conn.execute(query, (title, description, due_date, priority))
        self.conn.commit()

    def get_all_tasks(self):
        query = "SELECT * FROM tasks"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def update_task(self, task_id, title, description, due_date, priority, status):
        query = '''UPDATE tasks 
                  SET title=?, description=?, due_date=?, priority=?, status=?
                  WHERE id=?'''
        self.conn.execute(query, (title, description, due_date, priority, status, task_id))
        self.conn.commit()

    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id=?"
        self.conn.execute(query, (task_id,))
        self.conn.commit()

    def get_tasks_by_priority(self, priority):
        query = "SELECT * FROM tasks WHERE priority=?"
        cursor = self.conn.execute(query, (priority,))
        return cursor.fetchall()

    def get_tasks_by_date(self, date):
        query = "SELECT * FROM tasks WHERE due_date=?"
        cursor = self.conn.execute(query, (date,))
        return cursor.fetchall()
