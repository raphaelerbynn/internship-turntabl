import sqlite3
from flask import Flask, render_template

try:
    class Database:
        def __init__(self):
            self.query = """CREATE TABLE IF NOT EXISTS Applicants(
                    f_name TEXT NOT NULL,
                    m_name TEXT ,
                    l_name TEXT NOT NULL,
                    gender TEXT NOT NULL,
                    email TEXT PRIMARY KEY NOT NULL,
                    telephone TEXT,
                    year_of_graduation INTEGER NOT NULL,
                    school TEXT,
                    application_type TEXT NOT NULL,
                    upload_resume BLOB NOT NULL
                )"""

            self.insert_query = """INSERT INTO Applicants 
                    (f_name, m_name, l_name, 
                    gender, email, telephone, year_of_graduation, 
                    school, application_type, upload_resume)
                    
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

            self.clear_all_query = """DELETE FROM Applicants"""

            self.get_data_query = """SELECT * FROM Applicants"""

        def create_table(self):
            self.open_connection()
            self.cursor.execute(self.query)
            self.close_connection()
            return 0

        def set_data_to_admin(self, data):
            self.open_connection()

            self.close_connection()

        def insert_data_to_db(self, data):
            self.open_connection()
            self.cursor.execute(self.insert_query, data)
            self.connection.commit()
            self.close_connection()
            return 0

        def get_data(self):
            self.open_connection()
            self.cursor.execute(self.get_data_query)
            result = self.cursor.fetchall()
            self.close_connection()
            return result

        def clear_db(self):
            self.open_connection()
            self.cursor.execute(self.clear_all_query)
            self.connection.commit()
            self.close_connection()

        def close_connection(self):
            if self.connection:
                self.connection.close()

        def open_connection(self):
            self.connection = sqlite3.connect("Applicants.db")
            self.cursor = self.connection.cursor()


    db = Database()
    data = db.get_data()
    print(data)
    # db.create_table()
    # db.clear_db()
    # db.insert_data_to_db(("Ralph", "Ato", "Akoto", "F", "ralph@gmail.com", "+233544000950", "2022", "UCC", "TLC", " "))

    app = Flask(__name__, template_folder='')


    @app.route('/')
    def send_to_admin():
        return render_template('adminPage.html', details=data)



    if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')


except sqlite3.IntegrityError:
    print("Email already exists")
