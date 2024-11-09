import sqlite3
import os

class Database:
    def __init__(self, db_file='karyotype_data.sqlite'):
        self.db_file = db_file
        self.conn = None
        self.create_tables()

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_file)
        return self.conn

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_tables(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS karyotype_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT NOT NULL,
            analysis_result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        conn.commit()
        self.close()

    def insert_analysis(self, image_path, analysis_result):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO karyotype_analysis (image_path, analysis_result)
        VALUES (?, ?)
        ''', (image_path, analysis_result))

        conn.commit()
        self.close()

    def get_all_analyses(self):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM karyotype_analysis ORDER BY timestamp DESC')
        analyses = cursor.fetchall()

        self.close()
        return analyses

    def get_analysis_by_id(self, analysis_id):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM karyotype_analysis WHERE id = ?', (analysis_id,))
        analysis = cursor.fetchone()

        self.close()
        return analysis

