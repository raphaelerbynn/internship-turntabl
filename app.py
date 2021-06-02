import random

from flask import Flask, render_template

app = Flask(__name__, template_folder='')

colors = ['000000', 'FF0000', '00FF00', '0000FF', 'FFFF00', '00FFFF', 'FF00FF']


@app.route('/change_color')
def change():
    rand_color = random.randint(0, len(colors)-1)
    return render_template('changesColor.html', color=colors[rand_color])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
