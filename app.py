from flask import Flask, render_template

import mysql.connector
# Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="pagina_peliculas"
)
cursor = conexion.cursor()

app = Flask(__name__)

nombre = "Martin Fierro"

def listar_clientes():
    query = "SELECT * FROM Reviews"
    cursor.execute(query)
    reviews = cursor.fetchall()






@app.route('/')
def home():
    return render_template('index.html')

@app.route('/menu2.html')
def menu2():
    return render_template('menu2.html')

@app.route('/reseñas.html')
def resenas():
    query = "SELECT usuarios.nombre_usuario, reseñas.calificación, reseñas.comentario, reseñas.fecha_resena FROM reseñas JOIN usuarios usuarios ON reseñas.id_usuario = usuarios.id_usuari o WHERE reseñas.id_pelicula = 1;"
    cursor.execute(query)
    reseñas = cursor.fetchall()
    return render_template('reseñas.html', reseñas=reseñas)

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


