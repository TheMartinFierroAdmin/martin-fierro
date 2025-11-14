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

@app.route('/reseñas.html')  # Nueva ruta para la tabla
def peliculas_reseñas():
    # Consulta todas las películas
    cursor.execute("SELECT id_pelicula, titulo FROM peliculas")
    peliculas_data = cursor.fetchall()  # Lista de tuplas: [(id, titulo), ...]
    
    # Para cada película, obtener sus calificaciones
    reseñas = []
    for pelicula in peliculas_data:
        id_pelicula = pelicula[0]
        cursor.execute("SELECT calificación FROM reseñas WHERE id_pelicula = %s", (id_pelicula,))
        calificaciones = cursor.fetchall()  # Lista de tuplas: [(calif,), ...]
        # Convierte a lista simple de floats
        reseñas.append([calif[0] for calif in calificaciones])
    
    # Extrae solo los títulos para el template
    peliculas = [p[1] for p in peliculas_data]
    
    return render_template('reseñas.html', peliculas=peliculas, reseñas=reseñas)

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


