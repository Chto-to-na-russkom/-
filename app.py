from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ves = float(request.form['ves'])
        ves1 = round(ves * 0.378, 2)
        ves2 = round(ves * 0.907, 2)
        ves3 = round(ves * 0.377, 2)
        ves4 = round(ves * 2.364, 2)
        ves5 = round(ves * 0.916, 2)
        ves6 = round(ves * 0.889, 2)
        ves7 = round(ves * 1.125, 2)
        return render_template('index.html', volume=ves1, volume1=ves2, volume2=ves3, volume3=ves4,  volume4=ves5, volume5=ves6, volume6=ves7)
    return render_template('index.html')


if __name__ == '__main__':
   app.run('localhost', 4449)