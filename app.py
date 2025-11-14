from flask import Flask, render_template

import mysql.connector
# Conexión a la base de datos
conexion = mysql.connector.connect(
host="localhost",
user="root",
password="root",
database="pagina_peliculas2"
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
def peliculas_reseñas():
    # Consulta que une películas y reseñas para obtener título, comentario y calificación
    query = """
    SELECT p.titulo, r.comentario, r.calificación
    FROM peliculas p
    JOIN reseñas r ON p.id_pelicula = r.id_pelicula
    ORDER BY p.titulo  # Opcional: ordena por título de película
    """
    cursor.execute(query)
    reseñas_data = cursor.fetchall()  # Lista de tuplas: [(titulo, comentario, calif), ...]
    
    return render_template('reseñas.html', reseñas_data=reseñas_data)


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


