import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='')


def insert_data(data):
    connection = sqlite3.connect('test_input.db')
    create_table_query = """CREATE TABLE IF NOT EXISTS details(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
    )"""

    insert_query = """INSERT INTO details(id, name, email)
                        VALUES(?, ?, ?)"""
    #
    delete_query = """DELETE FROM details"""
    cursor = connection.cursor()
    #
    cursor.execute(create_table_query)
    cursor.execute(insert_query, data)
    # cursor.execute(delete_query)
    connection.commit()

    if connection:
        connection.close()
    return 1


@app.route('/login')
def login_page():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    try:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            id_num = request.form['id']

            data = (id_num, name, email)

            insert_data(data)
            return render_template('submitted_to_database.html')
    except sqlite3.IntegrityError:
        print('ID already exists')
        return render_template('submitted_to_database.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
