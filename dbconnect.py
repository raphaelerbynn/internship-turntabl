import sqlite3

connection = sqlite3.connect('employees.db')
cursor = connection.cursor()

create_table_query = """ CREATE TABLE IF NOT EXISTS emp_details(
                              id INTEGER,
                              first_name TEXT NOT NULL,
                              last_name TEX NOT NULL,
                              age TEXT NOT NULL,
                              year_employed TEXT NOT NULL,
                              email TEXT NOT NULL,
                              residence TEXT NOT NULL
                    ) """