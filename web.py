from datetime import date
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__, template_folder='')


details = {
    'fname': [],
    'lname': [],
    'age': [],
    'year_employed': [],
    'email': [],
    'residence': [],
    'id': []
}


@app.route('/')
def hello():
    return 'hello world..............'


def thank(name):
    return 'Hello! %s' % name


@app.route('/check/<int:num>')
def whole(num):
    return '%d is a whole num' % num


@app.route('/check/<float:num>')
def decimal(num):
    return '%f is a decimal num' % num


@app.route('/admin')
def admin():

    return render_template('adminPage.html', details=details)


@app.route('/<guest>')
def hello_guest(guest):
    return 'hello %s, this is guest user page' % guest


@app.route('/user/<person>')
def user(person):
    if person == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_guest', guest=person))


@app.route('/fillform')
def login0():
    return render_template('employeeInput.html')


@app.route('/loggedin')
def successful_login():
    return render_template('submitted.html')


@app.route('/fillform', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        user_name = request.form['name']
        user_yearborn = request.form['yearborn']
        user_yearemployed = request.form['yearemployed']
        user_mail = request.form['mail']
        user_res = request.form['res']

        space = ' '
        if space in user_name:
            user_name_list = user_name.split()
            user_fname = user_name_list[0]
            user_lname = user_name_list[len(user_name_list) - 1]
            details['fname'].append(user_fname)
            details['lname'].append(user_lname)
        else:
            details['fname'].append(user_name)
            details['lname'].append(None)

        # calc age
        user_age = date.today().year - int(user_yearborn)

        # calc id
        id_num = len(details['fname'])
        user_id = "EMP/"+user_yearemployed+"/"+str(id_num)

        details['age'].append(user_age)
        details['year_employed'].append(user_yearemployed)
        details['email'].append(user_mail)
        details['residence'].append(user_res)
        details['id'].append(user_id)

        print(details)
        return redirect(url_for('successful_login', user=user_id))


@app.route('/admin0')
def delete():
    i = 0
    print(i)
    return render_template('adminPage.html', i=i, details=details)


app.add_url_rule('/thankyou/<name>', 'With parameter', thank)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
