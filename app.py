from flask import Flask, render_template

app = Flask(__name__)



if __name__ == '__main__':
    app.run(debug=True)

nombre = "Martin Fierro"

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('templates/menu2.html')
def index():
    return render_template('menu2.html')

@app.route('templates/reseñas.html')
def index():
    return render_template('reseñas.html')

@app.route('templates/index.html')
def index():
    return render_template('index.html')

@app.route('templates/index.html')
def index():
    return render_template('index.html')

@app.route('templates/index.html')
def index():
    return render_template('index.html')

@app.route('templates/index.html')
def index():
    return render_template('index.html')

