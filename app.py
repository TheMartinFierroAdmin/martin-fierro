from flask import Flask, render_template

app = Flask(__name__)

nombre = "Martin Fierro"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu2.html')
def menu2():
    return render_template('menu2.html')

@app.route('/reseñas.html')
def resenas():
    return render_template('reseñas.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/usuarios.html')
def usuarios():
    return render_template('usuarios.html')

@app.route('/iniciosesion.html')
def iniciosesion():
    return render_template('iniciosesion.html')

@app.route('/mis_reseñas.html')
def mis_reseñas():
    return render_template('mis_reseñas.html')



if __name__ == '__main__':
    app.run(debug=True)


import mysql.connector
# Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="pagina_peliculas"
)
cursor = conexion.cursor()